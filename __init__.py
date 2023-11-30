import io
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

from BaseClasses import ItemClassification, MultiWorld, Region
from worlds.AutoWorld import World

from .base_classes import D3DItem, D3DLevel, LocationDef
from .id import GAME_ID, local_id, net_id
from .items import all_items, item_groups
from .levels import all_episodes
from .options import Duke3DOptions
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
    item_name_groups = item_groups
    id_checksum = game_ids["checksum"]
    options_dataclass = Duke3DOptions
    options: Duke3DOptions

    def __init__(self, world: MultiWorld, player: int):
        self.included_levels: List[D3DLevel] = []
        self.starting_levels: List[D3DLevel] = []
        self.used_locations: Set[str] = set()
        # Add the id checksum of our location and item ids for consistency check with clients
        self.slot_data: Dict[str, Any] = {
            "checksum": self.id_checksum,
            "settings": {},
        }
        self.rules: Optional[Rules] = None

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
        if location.mp_only and not self.get_option("include_mp_items"):
            return False
        if (
            location.type == "sector"
            and self.get_option("goal") == self.options.goal.option_beat_all_levels
            and not self.get_option("include_secrets")
        ):
            return False
        return True

    def get_option(self, option_name: str) -> Any:
        return getattr(self.multiworld, option_name)[self.player].value

    def include_episode(self, episode_shorthand: str):
        """
        Adds levels for a selected episode option
        """
        episode_id = int(episode_shorthand[-1]) - 1
        episode = all_episodes[episode_id]
        self.included_levels += episode.levels
        if len(episode.levels) > 0:
            self.starting_levels.append(episode.levels[0])

    def generate_early(self) -> None:
        # Configure rules
        self.rules = Rules(self)

        # Generate level pool
        for episode_option in ("episode1", "episode2", "episode3", "episode4"):
            if self.get_option(episode_option):
                self.include_episode(episode_option)

        # Initial level unlocks
        for level in self.starting_levels:
            self.multiworld.start_inventory[self.player].value[level.unlock] = 1
        for level in self.included_levels:
            if self.get_option("area_maps") == self.options.area_maps.option_start_with:
                self.multiworld.start_inventory[self.player].value[level.map] = 1
        self.slot_data["settings"]["difficulty"] = self.get_option("difficulty")
        if self.get_option("unlock_abilities"):
            self.slot_data["settings"]["lock_crouch"] = True
            self.slot_data["settings"]["lock_jump"] = True
            self.slot_data["settings"]["lock_run"] = True
            self.slot_data["settings"]["lock_dive"] = True

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

        goal_exits = self.get_option("goal") in {
            self.options.goal.option_beat_all_levels,
            self.options.goal.option_both,
        }
        goal_secrets = self.get_option("goal") in {
            self.options.goal.option_collect_all_secrets,
            self.options.goal.option_both,
        }
        goal_counts = {"Exit": 0, "Secret": 0}
        for level in self.included_levels:
            for location in level.locations.values():
                if location.name not in self.used_locations:
                    continue
                if goal_exits and location.type == "exit":
                    goal_counts["Exit"] += 1
                elif goal_secrets and location.type == "sector":
                    goal_counts["Secret"] += 1

        # ToDo apply some dynamic percent scaling via slider?

        self.slot_data["goal"] = {
            self.item_name_to_id["Exit"]: goal_counts["Exit"],
            self.item_name_to_id["Secret"]: goal_counts["Secret"],
        }
        self.multiworld.completion_condition[self.player] = self.rules.count(
            "Exit", goal_counts["Exit"]
        ) & self.rules.count("Secret", goal_counts["Secret"])

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

    def create_event(self, event_name: str) -> D3DItem:
        return D3DItem(event_name, ItemClassification.progression, None, self.player)

    def get_filler_item_name(self) -> str:
        return "Nothing"

    def create_junk(self, count: int) -> List[D3DItem]:
        # ToDo actually do some balanced filling here of useful junk
        return [self.create_item(self.get_filler_item_name()) for _ in range(count)]

    def create_item_list(self, item_list: List[str]) -> List[D3DItem]:
        return [self.create_item(item) for item in item_list]

    def create_items(self):
        itempool = []  # Absolutely mandatory progression items
        useful_items = (
            []
        )  # Stuff that should be in the world if there's enough locations
        used_locations = self.used_locations.copy()
        # Place goal items and level key cards
        goal_exits = self.get_option("goal") in {
            self.options.goal.option_beat_all_levels,
            self.options.goal.option_both,
        }
        goal_secrets = self.get_option("goal") in {
            self.options.goal.option_collect_all_secrets,
            self.options.goal.option_both,
        }
        for level in self.included_levels:
            for location in level.locations.values():
                if (
                    goal_exits
                    and location.name in self.used_locations
                    and location.type == "exit"
                ):
                    self.multiworld.get_location(
                        location.name, self.player
                    ).place_locked_item(self.create_item("Exit"))
                    used_locations.remove(location.name)
                elif (
                    goal_secrets
                    and location.name in self.used_locations
                    and location.type == "sector"
                ):
                    self.multiworld.get_location(
                        location.name, self.player
                    ).place_locked_item(self.create_item("Secret"))
                    used_locations.remove(location.name)
            # create and fill event items
            for event in level.events:
                prefixed_event = f"{level.prefix} {event}"
                self.multiworld.get_location(
                    prefixed_event, self.player
                ).place_locked_item(self.create_event(prefixed_event))
            itempool += [self.create_item(item) for item in level.items]
            if level.unlock not in self.multiworld.start_inventory[self.player].value:
                itempool.append(self.create_item(level.unlock))
            if self.get_option("area_maps") == self.options.area_maps.option_unlockable:
                useful_items.append(self.create_item(level.map))

        if self.get_option("unlock_abilities"):
            itempool += self.create_item_list(
                [
                    "Jump",
                    "Sprint",
                    "Crouch",
                    "Scuba Gear",
                    "Scuba Gear Capacity",
                    "Scuba Gear Capacity",
                ]
            )

        # Add prog items and stuff
        # ToDo actual logic for filling
        itempool += self.create_item_list(
            ["Jetpack", "Jetpack Capacity", "RPG", "Pipebomb", "Tripmine"]
        )

        useful_items += self.create_item_list(["Shotgun"])

        # Add as much useful stuff as can fit
        itempool.extend(useful_items[: len(used_locations) - len(itempool)])

        # Add filler
        itempool += self.create_junk(len(used_locations) - len(itempool))

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
