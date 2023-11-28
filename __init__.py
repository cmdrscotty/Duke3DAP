import io
import json
from pathlib import Path
from typing import List, Optional

from BaseClasses import MultiWorld, Region
from worlds.AutoWorld import World

from .base_classes import D3DLevel, LocationDef
from .id import GAME_ID, local_id, net_id
from .items import all_items, item_groups
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

    def __init__(self, world: MultiWorld, player: int):
        self.included_levels: List[D3DLevel] = []
        self.rules = Rules(world, player)

        super().__init__(world, player)

    @classmethod
    def local_id(cls, ap_id: int) -> int:
        return local_id(ap_id)

    @classmethod
    def net_id(cls, short_id: int) -> int:
        return net_id(short_id)

    item_name_to_id = {
        name: net_id(loc_id) for name, loc_id in game_ids["items"].items()
    }
    location_name_to_id = {
        name: net_id(loc_id) for name, loc_id in game_ids["locations"].items()
    }
    item_groups = item_groups
    id_checksum = game_ids["checksum"]

    def use_location(self, location: Optional[LocationDef] = None) -> bool:
        """
        Specify if a certain location should be included, based on world settings
        """
        if location is None:
            return False
        return not location.mp_only

    def create_regions(self):
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)
        for level in self.included_levels:
            level.set_world(self)
            level_region = level.make_region()
            menu_region.connect(level_region, self.rules.level(level))
