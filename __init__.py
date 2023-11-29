import io
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

from BaseClasses import ItemClassification, MultiWorld, Region
from worlds.AutoWorld import World

from .base_classes import D3DItem, D3DLevel, LocationDef
from .id import GAME_ID, local_id, net_id
from .items import all_items, item_groups
from .levels import all_levels
from .rules import Rules

with io.open(Path(__file__).parent / "resources" / "id_map.json", "r") as id_file:
    game_ids = json.load(id_file)


class D3DWorld(World):
    """
    Duke Nukem 3D Randomizer
    """

    game = "Duke3D"
    build_game_id = GAME_ID
    game_full_name = "Duke Nukem 3D"
    item_name_to_id = {
        name: net_id(loc_id) for name, loc_id in game_ids["items"].items()
    }
    location_name_to_id = {
        name: net_id(loc_id) for name, loc_id in game_ids["locations"].items()
    }
    item_groups = item_groups
    id_checksum = game_ids["checksum"]

    def __init__(self, world: MultiWorld, player: int):
        self.included_levels: List[D3DLevel] = [all_levels[0]]
        self.rules = Rules(world, player)
        self.used_locations: Set[str] = set()
        # Add the id checksum of our location and item ids for consistency check with clients
        self.slot_data: Dict[str, Any] = {"checksum": self.id_checksum}

        super().__init__(world, player)

    @classmethod
    def local_id(cls, ap_id: int) -> int:
        return local_id(ap_id)

    @classmethod
    def net_id(cls, short_id: int) -> int:
        return net_id(short_id)

    def use_location(self, location: Optional[LocationDef] = None) -> bool:
        """
        Specify if a certain location should be included, based on world settings
        """
        if location is None:
            return False
        return not location.mp_only

    def generate_early(self) -> None:
        # Initial level unlocks
        self.multiworld.start_inventory[self.player].value["E1L1 Unlock"] = 1

    def create_regions(self):
        self.used_locations = set()
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)
        for level in self.included_levels:
            level_region = level.create_region(self)
            self.used_locations |= level.used_locations
            menu_region.connect(level_region, self.rules.level(level))
        self.slot_data["locations"] = [
            self.location_name_to_id[loc] for loc in self.used_locations
        ]
        self.slot_data["levels"] = [
            self.item_name_to_id[level.unlock] for level in self.included_levels
        ]

        # ToDo dynamically determine goal count here somehow
        self.slot_data["goal"] = {
            self.item_name_to_id["Exit"]: 1,
            self.item_name_to_id["Secret"]: 8,
        }
        self.multiworld.completion_condition[self.player] = self.rules.count(
            "Exit", 1
        ) & self.rules.count("Secret", 8)

    def create_item(self, item: str) -> D3DItem:
        item_def = all_items.get(item)
        classification = (
            ItemClassification.progression
            if item_def.progression
            else ItemClassification.useful
            if item_def.persistent
            else ItemClassification.filler
        )
        return D3DItem(item, classification, self.item_name_to_id[item], self.player)

    def create_items(self):
        itempool = []
        used_locations = self.used_locations.copy()
        # Place goal items and level key cards
        for level in self.included_levels:
            for location in level.locations.values():
                if location.name in self.used_locations and location.type == "exit":
                    self.multiworld.get_location(
                        location.name, self.player
                    ).place_locked_item(self.create_item("Exit"))
                    used_locations.remove(location.name)
                elif location.name in self.used_locations and location.type == "sector":
                    self.multiworld.get_location(
                        location.name, self.player
                    ).place_locked_item(self.create_item("Secret"))
                    used_locations.remove(location.name)
            itempool += [self.create_item(item) for item in level.items]
            if level.unlock not in self.multiworld.start_inventory[self.player].value:
                itempool.append(self.create_item(level.unlock))

        # Add prog items and stuff
        # ToDo actual logic and filling

        # Add filler
        itempool += [
            self.create_item("Nothing")
            for _ in range(len(used_locations) - len(itempool))
        ]

        self.multiworld.itempool += itempool

    def fill_slot_data(self) -> Dict[str, Any]:
        return self.slot_data

    def generate_output(self, output_directory: str) -> None:
        """
        If we have a single player generation, also generate a single player .json file
        """
        if self.multiworld.players != 1:
            return

        out = {
            "data_package": {
                "data": {
                    "games": {
                        self.game: {
                            "item_name_to_id": self.item_name_to_id,
                            "location_name_to_id": self.location_name_to_id,
                        }
                    }
                }
            },
            "slot_data": self.slot_data,
            "location_to_item": {
                location.address: location.item.code
                for location in self.multiworld.get_filled_locations(self.player)
            },
            "start_inventory": [
                self.item_name_to_id[item]
                for item in self.multiworld.start_inventory[self.player].value.keys()
            ],
        }

        with io.open(
            Path(output_directory) / f"AP_{self.multiworld.seed}.spworld",
            "w",
            encoding="utf-8",
        ) as out_file:
            out_file.write(json.dumps(out))
