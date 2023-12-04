from typing import Dict

from ..base_classes import ItemDef
from ..id import net_id
from ..levels import all_levels

automap_base_id = 1600
unlock_base_id = 1700
key_card_base_id = 1800

# Filled step by step below for readability
item_groups = {}

dynamic_level_items = {}

for level in all_levels:
    # automap
    automap = ItemDef(
        f"{level.prefix} Automap",
        net_id(automap_base_id),
        "automap",
        {"levelnum": level.levelnum, "volumenum": level.volumenum},
        persistent=True,
        unique=True,
    )
    automap_base_id += 1
    dynamic_level_items[automap.name] = automap

    # unlock
    unlock = ItemDef(
        f"{level.prefix} Unlock",
        net_id(unlock_base_id),
        "map",
        {},
        persistent=True,
        unique=True,
        progression=True,
    )
    unlock_base_id += 1
    dynamic_level_items[unlock.name] = unlock

    # key cards
    for color in level.keys:
        if color == "Blue":
            flags = 1
        elif color == "Red":
            flags = 2
        elif color == "Yellow":
            flags = 4
        else:
            continue
        key_card = ItemDef(
            f"{level.prefix} {color} Key Card",
            net_id(key_card_base_id),
            "key",
            {"flags": flags, "levelnum": level.levelnum, "volumenum": level.volumenum},
            persistent=True,
            unique=True,
            progression=True,
        )
        key_card_base_id += 1
        dynamic_level_items[key_card.name] = key_card

goal_items = {
    "Exit": ItemDef(
        "Exit", net_id(100), "goal", {}, silent=True, persistent=True, progression=True
    ),
    "Secret": ItemDef(
        "Secret",
        net_id(101),
        "goal",
        {},
        silent=True,
        persistent=True,
        progression=True,
    ),
}

junk_items = {
    "Nothing": ItemDef("Nothing", net_id(0), "filler", {}, silent=True),
    "Pity Heal": ItemDef(
        "Pity Heal",
        net_id(403),
        "health",
        {"heal": 1, "overheal": True},
    ),
}

weapons = {
    "Pistol Capacity": ItemDef(
        "Pistol Capacity",
        net_id(221),
        "ammo",
        {"weaponnum": 1, "capacity": 20, "ammo": 10},
        persistent=True,
    ),
    "Pistol Ammo": ItemDef(
        "Pistol Ammo",
        net_id(261),
        "ammo",
        {"weaponnum": 1, "ammo": 30},
    ),
    "Shotgun": ItemDef(
        "Shotgun",
        net_id(202),
        "weapon",
        {"weaponnum": 2, "ammo": 10},
        persistent=True,
        unique=True,
    ),
    "Shotgun Capacity": ItemDef(
        "Shotgun Capacity",
        net_id(222),
        "ammo",
        {"weaponnum": 2, "capacity": 10, "ammo": 5},
        persistent=True,
    ),
    "Progressive Shotgun": ItemDef(
        "Progressive Shotgun",
        net_id(242),
        "progressive",
        {"items": [202, 222]},
        silent=True,
        persistent=True,
    ),
    "Shotgun Ammo": ItemDef(
        "Shotgun Ammo",
        net_id(262),
        "ammo",
        {"weaponnum": 2, "ammo": 10},
    ),
    "Chaingun": ItemDef(
        "Chaingun",
        net_id(203),
        "weapon",
        {"weaponnum": 3, "ammo": 50},
        persistent=True,
        unique=True,
    ),
    "Chaingun Capacity": ItemDef(
        "Chaingun Capacity",
        net_id(223),
        "ammo",
        {"weaponnum": 3, "capacity": 50, "ammo": 25},
        persistent=True,
    ),
    "Progressive Chaingun": ItemDef(
        "Progressive Chaingun",
        net_id(243),
        "progressive",
        {"items": [203, 223]},
        silent=True,
        persistent=True,
    ),
    "Chaingun Ammo": ItemDef(
        "Chaingun Ammo",
        net_id(263),
        "ammo",
        {"weaponnum": 3, "ammo": 100},
    ),
    "RPG": ItemDef(
        "RPG",
        net_id(204),
        "weapon",
        {"weaponnum": 4, "ammo": 5},
        persistent=True,
        unique=True,
        progression=True,
    ),
    "RPG Capacity": ItemDef(
        "RPG Capacity",
        net_id(224),
        "ammo",
        {"weaponnum": 4, "capacity": 5, "ammo": 2},
        persistent=True,
    ),
    "Progressive RPG": ItemDef(
        "Progressive RPG",
        net_id(244),
        "progressive",
        {"items": [204, 224]},
        silent=True,
        persistent=True,
    ),
    "RPG Ammo": ItemDef(
        "RPG Ammo",
        net_id(264),
        "ammo",
        {"weaponnum": 4, "ammo": 10},
    ),
    "Pipebomb": ItemDef(
        "Pipebomb",
        net_id(205),
        "weapon",
        {"weaponnum": 5, "ammo": 2},
        persistent=True,
        unique=True,
        progression=True,
    ),
    "Pipebomb Capacity": ItemDef(
        "Pipebomb Capacity",
        net_id(225),
        "ammo",
        {"weaponnum": 5, "capacity": 3, "ammo": 1},
        persistent=True,
    ),
    "Progressive Pipebomb": ItemDef(
        "Progressive Pipebomb",
        net_id(245),
        "progressive",
        {"items": [205, 225]},
        silent=True,
        persistent=True,
    ),
    "Pipebomb Ammo": ItemDef(
        "Pipebomb Ammo",
        net_id(265),
        "ammo",
        {"weaponnum": 5, "ammo": 5},
    ),
    "Shrinker": ItemDef(
        "Shrinker",
        net_id(206),
        "weapon",
        {"weaponnum": 6, "ammo": 2},
        persistent=True,
        unique=True,
    ),
    "Shrinker Capacity": ItemDef(
        "Shrinker Capacity",
        net_id(226),
        "ammo",
        {"weaponnum": 6, "capacity": 3, "ammo": 1},
        persistent=True,
    ),
    "Progressive Shrinker": ItemDef(
        "Progressive Shrinker",
        net_id(246),
        "progressive",
        {"items": [206, 226]},
        silent=True,
        persistent=True,
    ),
    "Shrinker Ammo": ItemDef(
        "Shrinker Ammo",
        net_id(266),
        "ammo",
        {"weaponnum": 6, "ammo": 10},
    ),
    "Devastator": ItemDef(
        "Devastator",
        net_id(207),
        "weapon",
        {"weaponnum": 7, "ammo": 10},
        persistent=True,
        unique=True,
        progression=True,
    ),
    "Devastator Capacity": ItemDef(
        "Devastator Capacity",
        net_id(227),
        "ammo",
        {"weaponnum": 7, "capacity": 20, "ammo": 10},
        persistent=True,
    ),
    "Progressive Devastator": ItemDef(
        "Progressive Devastator",
        net_id(247),
        "progressive",
        {"items": [207, 227]},
        silent=True,
        persistent=True,
    ),
    "Devastator Ammo": ItemDef(
        "Devastator Ammo",
        net_id(267),
        "ammo",
        {"weaponnum": 7, "ammo": 25},
    ),
    "Tripmine": ItemDef(
        "Tripmine",
        net_id(208),
        "weapon",
        {"weaponnum": 8, "ammo": 1},
        persistent=True,
        unique=True,
        progression=True,
    ),
    "Tripmine Capacity": ItemDef(
        "Tripmine Capacity",
        net_id(228),
        "ammo",
        {"weaponnum": 8, "capacity": 1, "ammo": 1},
        persistent=True,
    ),
    "Progressive Tripmine": ItemDef(
        "Progressive Tripmine",
        net_id(248),
        "progressive",
        {"items": [208, 228]},
        silent=True,
        persistent=True,
    ),
    "Tripmines": ItemDef(
        "Tripmines",
        net_id(267),
        "ammo",
        {"weaponnum": 8, "ammo": 3},
    ),
    "Freezethrower": ItemDef(
        "Freezethrower",
        net_id(209),
        "weapon",
        {"weaponnum": 9, "ammo": 20},
        persistent=True,
        unique=True,
    ),
    "Freezethrower Capacity": ItemDef(
        "Freezethrower Capacity",
        net_id(229),
        "ammo",
        {"weaponnum": 9, "capacity": 40, "ammo": 20},
        persistent=True,
    ),
    "Progressive Freezethrower": ItemDef(
        "Progressive Freezethrower",
        net_id(249),
        "progressive",
        {"items": [209, 229]},
        silent=True,
        persistent=True,
    ),
    "Freezethrower Ammo": ItemDef(
        "Freezethrower Ammo",
        net_id(269),
        "ammo",
        {"weaponnum": 9, "ammo": 50},
    ),
    "Microwave Expander": ItemDef(
        "Microwave Expander",
        net_id(211),
        "weapon",
        {"weaponnum": 11, "ammo": 2},
        persistent=True,
        unique=True,
    ),
    "Expander Capacity": ItemDef(
        "Expander Capacity",
        net_id(231),
        "ammo",
        {"weaponnum": 11, "capacity": 3, "ammo": 2},
        persistent=True,
    ),
    "Progressive Expander": ItemDef(
        "Progressive Expander",
        net_id(251),
        "progressive",
        {"items": [211, 231]},
        silent=True,
        persistent=True,
    ),
    "Expander Ammo": ItemDef(
        "Expander Ammo",
        net_id(271),
        "ammo",
        {"weaponnum": 11, "ammo": 5},
    ),
}

item_groups["RPG"] = {"RPG", "Progressive RPG"}
item_groups["Pipebomb"] = {"Pipebomb", "Progressive Pipebomb"}
item_groups["Devastator"] = {"Devastator", "Progressive Devastator"}
item_groups["Tripmine"] = {"Tripmine", "Progressive Tripmine"}
item_groups["Explosives"] = {
    "RPG",
    "Pipebomb",
    "Devastator",
    "Tripmine",
    "Progressive RPG",
    "Progressive Pipebomb",
    "Progressive Devastator",
    "Progressive Tripmine",
}

inventory_items = {
    "Steroids": ItemDef(
        "Steroids",
        net_id(300),
        "inventory",
        {
            "invnum": 0,
            "capacity": 40,
        },  # use capacity from slot data if configured
        persistent=True,
        unique=True,
        progression=True,
    ),
    "Steroids Capacity": ItemDef(
        "Steroids Capacity",
        net_id(320),
        "invcapacity",
        {
            "invnum": 0,
            "capacity": 40,
        },  # use capacity from slot data if configured
        persistent=True,
    ),
    "Progressive Steroids": ItemDef(
        "Progressive Steroids",
        net_id(340),
        "progressive",
        {"items": [300, 320]},
        persistent=True,
        progression=True,
        silent=True,
    ),
    "Armor": ItemDef(
        "Armor",
        net_id(301),
        "armor",
        {"capacity": 40},
    ),
    "Sturdy Armor": ItemDef(
        "Sturdy Armor",
        net_id(321),
        "armor",
        {"capacity": 2, "maxcapacity": 2},
        persistent=True,
    ),
    "Scuba Gear": ItemDef(
        "Scuba Gear",
        net_id(302),
        "inventory",
        {
            "invnum": 2,
            "capacity": 400,
        },  # use capacity from slot data if configured
        persistent=True,
        unique=True,
        progression=True,
    ),
    "Scuba Gear Capacity": ItemDef(
        "Scuba Gear Capacity",
        net_id(322),
        "invcapacity",
        {
            "invnum": 2,
            "capacity": 400,
        },  # use capacity from slot data if configured
        persistent=True,
    ),
    "Progressive Scuba Gear": ItemDef(
        "Progressive Scuba Gear",
        net_id(342),
        "progressive",
        {"items": [302, 322]},
        persistent=True,
        progression=True,
        silent=True,
    ),
    "Holo Duke": ItemDef(
        "Holo Duke",
        net_id(303),
        "inventory",
        {"invnum": 3, "capacity": 600},
    ),
    "Jetpack": ItemDef(
        "Jetpack",
        net_id(304),
        "inventory",
        {
            "invnum": 4,
            "capacity": 100,
        },  # use capacity from slot data if configured
        persistent=True,
        unique=True,
        progression=True,
    ),
    "Jetpack Capacity": ItemDef(
        "Jetpack Capacity",
        net_id(324),
        "invcapacity",
        {
            "invnum": 4,
            "capacity": 100,
        },  # use capacity from slot data if configured
        persistent=True,
        progression=True,
    ),
    "Progressive Jetpack": ItemDef(
        "Progressive Jetpack",
        net_id(344),
        "progressive",
        {"items": [304, 324]},
        persistent=True,
        progression=True,
        silent=True,
    ),
    "Night Vision Goggles": ItemDef(
        "Night Vision Goggles",
        net_id(307),
        "inventory",
        {"invnum": 7, "capacity": 400, "max_capacity": 1600},
    ),
    "First Aid Kit": ItemDef(
        "First Aid Kit",
        net_id(309),
        "inventory",
        {"invnum": 9, "capacity": 35, "max_capacity": 100},
    ),
    "Protective Boots": ItemDef(
        "Protective Boots",
        net_id(310),
        "inventory",
        {"invnum": 10, "capacity": 100, "max_capacity": 300},
    ),
}

item_groups["Jetpack"] = {"Jetpack", "Jetpack Capacity", "Progressive Jetpack"}
item_groups["Steroids"] = {"Steroids", "Steroids Jetpack"}
item_groups["Scuba Gear"] = {
    "Scuba Gear",
    "Scuba Gear Capacity",
    "Progressive Scuba Gear",
}

abilities = {
    "Jump": ItemDef(
        "Jump",
        net_id(350),
        "ability",
        {"enables": "jump"},
        persistent=True,
        unique=True,
        progression=True,
    ),
    "Dive": ItemDef(
        "Dive",
        net_id(351),
        "ability",
        {"enables": "dive"},
        persistent=True,
        unique=True,
        progression=True,
    ),
    "Crouch": ItemDef(
        "Crouch",
        net_id(352),
        "ability",
        {"enables": "crouch"},
        persistent=True,
        unique=True,
        progression=True,
    ),
    "Sprint": ItemDef(
        "Sprint",
        net_id(353),
        "ability",
        {"enables": "run"},
        persistent=True,
        unique=True,
        progression=True,
    ),
}

healing_items = {
    "Atomic Health": ItemDef(
        "Atomic Health", net_id(400), "health", {"heal": 50, "overheal": True}
    ),
    "Medpak": ItemDef("Medpak", net_id(401), "health", {"heal": 30}),
    "Bandage": ItemDef("Bandage", net_id(402), "health", {"heal": 10}),
    "Ego Boost": ItemDef(
        "Ego Boost", net_id(403), "health", {"heal": 2, "capacity": 2}, persistent=True
    ),
}

all_items: Dict[str, ItemDef] = {
    **junk_items,
    **goal_items,
    **weapons,
    **inventory_items,
    **abilities,
    **dynamic_level_items,
    **healing_items,
}
