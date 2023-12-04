import io
import json
import math
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

# Compatibility across Python versions
try:
    from importlib.resources import files
except ImportError:
    from importlib_resources import files  # noqa

from BaseClasses import ItemClassification, MultiWorld, Region
from worlds.AutoWorld import World

from . import resources
from .base_classes import D3DItem, D3DLevel, LocationDef
from .id import GAME_ID, local_id, net_id
from .items import all_items, item_groups
from .levels import all_episodes
from .options import Duke3DOptions
from .rules import Rules

with files(resources).joinpath("id_map.json").open() as id_file:
    game_ids = json.load(id_file)


class D3DWorld(World):
    """
    Duke Nukem 3D Randomizer
    """

    game = "Duke Nukem 3D"
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
        # Filled later from options
        self.fuel_per_pickup: Dict[str, int] = {}

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
        self.included_levels += episode.levels[: episode.maxlevel]
        if len(episode.levels) > 0:
            self.starting_levels.append(episode.levels[0])

    def generate_early(self) -> None:
        # difficulty settings
        self.fuel_per_pickup = {
            "Jetpack": self.get_option("fuel_per_jetpack"),
            "Scuba Gear": self.get_option("fuel_per_scuba_gear"),
            "Steroids": self.get_option("fuel_per_steroids"),
        }
        self.slot_data["settings"]["invinc"] = {
            # Index by invnum so they can be matched in-game
            0: self.fuel_per_pickup["Steroids"],
            2: self.fuel_per_pickup["Scuba Gear"],
            4: self.fuel_per_pickup["Jetpack"],
        }

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
        self.slot_data["settings"]["difficulty"] = self.get_option("skill_level")
        if self.get_option("unlock_abilities"):
            self.slot_data["settings"]["lock_crouch"] = True
            self.slot_data["settings"]["lock_jump"] = True
            self.slot_data["settings"]["lock_run"] = True
            self.slot_data["settings"]["lock_dive"] = True
        self.slot_data["settings"]["no_save"] = not self.get_option("allow_saving")

    def create_regions(self):
        self.used_locations = set()
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)
        for level in self.included_levels:
            level_region = level.create_region(self)
            # debug find missing locations
            # for loc in level.location_defs:
            #     loc_name = f'{level.prefix} {loc["name"]}'
            #     if loc_name not in level.used_locations:
            #         print(f"Missing location {loc_name}")
            #         menu_region.add_locations(
            #             {loc_name: self.location_name_to_id[loc_name]}
            #         )
            #         self.used_locations.add(loc_name)
            self.used_locations |= level.used_locations
            menu_region.connect(level_region, None, self.rules.level(level))
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

        goal_percentage = self.get_option("goal_percentage")
        if goal_percentage < 100:
            goal_counts["Exit"] = math.ceil(
                0.01 * goal_percentage * goal_counts["Exit"]
            )
            goal_counts["Secret"] = math.ceil(
                0.01 * goal_percentage * goal_counts["Secret"]
            )

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
        ret = D3DItem(item, classification, self.item_name_to_id[item], self.player)
        return ret

    def create_event(self, event_name: str) -> D3DItem:
        return D3DItem(event_name, ItemClassification.progression, None, self.player)

    def get_filler_item_name(self) -> str:
        return "Nothing"

    def create_junk(self, count: int) -> List[D3DItem]:
        difficulty = self.get_option("difficulty")
        if difficulty == self.options.difficulty.option_extreme:
            ratios = {
                "Nothing": 50,
                "Pity Heal": 150,
                "Medpak": 30,
                "Armor": 15,
                "Atomic Health": 5,
                # Oh, you got lucky!
                "Shrinker Capacity": 1,
                "Expander Capacity": 1,
                "First Aid Kit": 2,
            }
        elif difficulty == self.options.difficulty.option_hard:
            ratios = {
                "Pity Heal": 20,
                "Medpak": 40,
                "Armor": 40,
                "Atomic Health": 20,
                "RPG Capacity": 2,
                "Chaingun Capacity": 3,
                "Shrinker Capacity": 2,
                "Expander Capacity": 2,
                "First Aid Kit": 8,
                "Protective Boots": 4,
                # And some lucky additions!
                "Steroids Capacity": 1,
                "Devastator Capacity": 1,
                "Jetpack Capacity": 1,
            }
        elif difficulty == self.options.difficulty.option_medium:
            ratios = {
                "Medpak": 20,
                "Armor": 20,
                "Atomic Health": 20,
                "Pistol Capacity": 5,
                "RPG Capacity": 2,
                "Chaingun Capacity": 3,
                "Shrinker Capacity": 2,
                "Expander Capacity": 2,
                "Devastator Capacity": 1,
                "First Aid Kit": 10,
                "Protective Boots": 5,
                "Steroids Capacity": 3,
                # And some lucky additions!
                "Jetpack Capacity": 1,
                "Scuba Gear Capacity": 1,
            }
        else:
            ratios = {
                "Armor": 20,
                "Atomic Health": 30,
                "Pistol Capacity": 4,
                "RPG Capacity": 4,
                "Chaingun Capacity": 2,
                "Shrinker Capacity": 3,
                "Expander Capacity": 3,
                "Devastator Capacity": 2,
                "First Aid Kit": 15,
                "Protective Boots": 7,
                "Steroids Capacity": 5,
                "Jetpack Capacity": 2,
                "Scuba Gear Capacity": 2,
            }
        # create sample list
        pool = []
        for key, value in ratios.items():
            pool += [key] * value
        # and just generate items at the appropriate ratios
        return [
            self.create_item(self.multiworld.random.choice(pool)) for _ in range(count)
        ]

    def create_item_list(self, item_list: List[str]) -> List[D3DItem]:
        return [self.create_item(item) for item in item_list]

    # ToDo there has to be a way to reduce code duplication for these
    def generate_jetpack(self) -> Tuple[List[D3DItem], List[D3DItem]]:
        difficulty = self.get_option("difficulty")
        if difficulty == self.options.difficulty.option_extreme:
            required = 200
            total = 200
        elif difficulty == self.options.difficulty.option_hard:
            required = 200
            total = 300
        elif difficulty == self.options.difficulty.option_medium:
            required = 300
            total = 500
        else:
            required = 400
            total = 800
        required_cnt = math.ceil(float(required) / self.fuel_per_pickup["Jetpack"])
        total_cnt = math.ceil(float(total) / self.fuel_per_pickup["Jetpack"])

        # One base item and rest is capacity
        required_list = [self.create_item("Jetpack")] + [
            self.create_item("Jetpack Capacity") for _ in range(required_cnt - 1)
        ]
        # Fill pool with capacity up to total amount
        useful_list = [
            self.create_item("Jetpack Capacity")
            for _ in range(total_cnt - len(required_list))
        ]
        return required_list, useful_list

    def generate_scuba_gear(self) -> Tuple[List[D3DItem], List[D3DItem]]:
        difficulty = self.get_option("difficulty")
        if difficulty == self.options.difficulty.option_extreme:
            required = 400
            total = 400
        elif difficulty == self.options.difficulty.option_hard:
            required = 400
            total = 1000
        elif difficulty == self.options.difficulty.option_medium:
            required = 1250
            total = 2000
        else:
            required = 2000
            total = 3500
        required_cnt = math.ceil(float(required) / self.fuel_per_pickup["Scuba Gear"])
        total_cnt = math.ceil(float(total) / self.fuel_per_pickup["Scuba Gear"])

        # One base item and rest is capacity
        required_list = [self.create_item("Scuba Gear")] + [
            self.create_item("Scuba Gear Capacity") for _ in range(required_cnt - 1)
        ]
        # Fill pool with capacity up to total amount
        useful_list = [
            self.create_item("Scuba Gear Capacity")
            for _ in range(total_cnt - len(required_list))
        ]
        # If no level requires diving we just place all of them in the useful list, as we don't care if they
        # get discarded for seeds with very restricted available location slots
        need_dive = False
        for level in self.included_levels:
            if level.must_dive:
                need_dive = True
                break
        if need_dive:
            return required_list, useful_list
        else:
            return [], required_list + useful_list

    def generate_steroids(self) -> Tuple[List[D3DItem], List[D3DItem]]:
        difficulty = self.get_option("difficulty")
        if difficulty == self.options.difficulty.option_extreme:
            required = 0
            total = 0
        elif difficulty == self.options.difficulty.option_hard:
            required = 0
            total = 50
        elif difficulty == self.options.difficulty.option_medium:
            required = 100
            total = 200
        else:
            required = 150
            total = 300
        required_cnt = math.ceil(float(required) / self.fuel_per_pickup["Steroids"])
        total_cnt = math.ceil(float(total) / self.fuel_per_pickup["Steroids"])

        # Always need at least one in glitched logic!
        if self.get_option("glitch_logic") and required_cnt == 0:
            required_cnt = 1

        # One base item and rest is capacity
        required_list = [self.create_item("Steroids")] + [
            self.create_item("Steroids Capacity") for _ in range(required_cnt - 1)
        ]
        # Fill pool with capacity up to total amount
        useful_list = [
            self.create_item("Steroids Capacity")
            for _ in range(total_cnt - len(required_list))
        ]
        return required_list, useful_list

    def useful_items_per_difficulty(self) -> List[D3DItem]:
        difficulty = self.get_option("difficulty")
        if difficulty == self.options.difficulty.option_extreme:
            # Laughable, did you think you'd get anything?
            return []
        elif difficulty == self.options.difficulty.option_hard:
            # Provide some ammo capacity
            ret_items = {
                "Pistol Capacity": 2,
                "Shotgun Capacity": 2,
                "Chaingun Capacity": 2,
                "RPG Capacity": 2,
                "Pipebomb Capacity": 1,
                "Shrinker Capacity": 0,
                "Devastator Capacity": 3,
                "Tripmine Capacity": 2,
                "Freezethrower Capacity": 3,
                "Expander Capacity": 0,
            }
        elif difficulty == self.options.difficulty.option_medium:
            ret_items = {
                "Pistol Capacity": 4,
                "Shotgun Capacity": 4,
                "Chaingun Capacity": 3,
                "RPG Capacity": 5,
                "Pipebomb Capacity": 4,
                "Shrinker Capacity": 2,
                "Devastator Capacity": 5,
                "Tripmine Capacity": 4,
                "Freezethrower Capacity": 5,
                "Expander Capacity": 2,
            }
        else:
            ret_items = {
                "Pistol Capacity": 7,
                "Shotgun Capacity": 7,
                "Chaingun Capacity": 5,
                "RPG Capacity": 10,
                "Pipebomb Capacity": 6,
                "Shrinker Capacity": 5,
                "Devastator Capacity": 10,
                "Tripmine Capacity": 5,
                "Freezethrower Capacity": 8,
                "Expander Capacity": 5,
            }
        # Is there a good comprehension for this?
        ret = []
        for key, count in ret_items.items():
            ret += [self.create_item(key) for _ in range(count)]
        return ret

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
                ]
            )

        # ToDo support progressive items via toggle
        # Add progression items
        # Need access to at least 3 explosive weapons for some checks, and they might all have max capacity 1 (!)
        itempool += self.create_item_list(["RPG", "Pipebomb", "Tripmine", "Devastator"])
        # Get progression inventory based on difficulty settings
        required, useful = self.generate_jetpack()
        itempool += required
        useful_items += useful
        required, useful = self.generate_scuba_gear()
        itempool += required
        useful_items += useful
        required, useful = self.generate_steroids()
        itempool += required
        useful_items += useful

        # Can fail now if we don't even have enough slots for our required items
        if len(itempool) > len(used_locations):
            raise RuntimeError(
                "Not enough locations for all mandatory items with these settings!"
            )

        # Add one copy of each remaining weapon to the pool
        useful_items += self.create_item_list(
            ["Shotgun", "Chaingun", "Shrinker", "Freezethrower", "Microwave Expander"]
        )

        useful_items += self.useful_items_per_difficulty()

        if len(itempool) + len(useful_items) > len(used_locations):
            discarded = len(itempool) + len(useful_items) - len(used_locations)
            print(
                f"Had to discard {discarded} useful items from the pool: Not enough locations available"
            )

        # Add as much useful stuff as can fit
        # shuffle up the useful items so random ones get discarded if required
        self.multiworld.random.shuffle(useful_items)
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
            "seed": str(self.multiworld.seed),
        }

        with io.open(
            Path(output_directory) / f"AP_{self.multiworld.seed}.spworld",
            "w",
            encoding="utf-8",
        ) as out_file:
            out_file.write(json.dumps(out))
