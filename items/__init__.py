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
    "Nothing": ItemDef("Nothing", net_id(0), "goal", {}, silent=True),
}

weapons = {
    "Shotgun": ItemDef(
        "Shotgun",
        net_id(202),
        "weapon",
        {"weaponnum": 2, "ammo": 10},
        persistent=True,
        unique=True,
    ),
    "Chaingun": ItemDef(
        "Chaingun",
        net_id(203),
        "weapon",
        {"weaponnum": 3, "ammo": 50},
        persistent=True,
        unique=True,
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
    "Pipebomb": ItemDef(
        "Pipebomb",
        net_id(205),
        "weapon",
        {"weaponnum": 5, "ammo": 2},
        persistent=True,
        unique=True,
        progression=True,
    ),
    "Shrinker": ItemDef(
        "Shrinker",
        net_id(206),
        "weapon",
        {"weaponnum": 6, "ammo": 2},
        persistent=True,
        unique=True,
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
    "Tripmine": ItemDef(
        "Tripmine",
        net_id(208),
        "weapon",
        {"weaponnum": 8, "ammo": 1},
        persistent=True,
        unique=True,
        progression=True,
    ),
    "Freezethrower": ItemDef(
        "Freezethrower",
        net_id(209),
        "weapon",
        {"weaponnum": 9, "ammo": 20},
        persistent=True,
        unique=True,
    ),
    "Microwave Expander": ItemDef(
        "Microwave Expander",
        net_id(211),
        "weapon",
        {"weaponnum": 11, "ammo": 2},
        persistent=True,
        unique=True,
    ),
}

item_groups["explosives"] = {"RPG", "Pipebomb", "Devastator", "Tripmine"}

inventory_items = {
    "Steroids": ItemDef(
        "Steroids",
        net_id(300),
        "inventory",
        {"invnum": 0, "capacity": 40},
        persistent=True,
        unique=True,
        progression=True,
    ),
    "Steroids Capacity": ItemDef(
        "Steroids Capacity",
        net_id(320),
        "invcapacity",
        {"invnum": 0, "capacity": 40},
        persistent=True,
    ),
    "Progressive Steroids": ItemDef(
        "Progressive Steroids",
        net_id(340),
        "progressive",
        {"silent": True, "items": [300, 320]},
        persistent=True,
        progression=True,
    ),
    "Armor": ItemDef(
        "Armor",
        net_id(301),
        "inventory",
        {"invnum": 1, "capacity": 40, "max_capacity": 100},
    ),
    "Scube Gear": ItemDef(
        "Scube Gear",
        net_id(302),
        "inventory",
        {"invnum": 2, "capacity": 100},
        persistent=True,
        unique=True,
        progression=True,
    ),
    "Scuba Gear Capacity": ItemDef(
        "Scuba Gear Capacity",
        net_id(322),
        "invcapacity",
        {"invnum": 2, "capacity": 100},
        persistent=True,
    ),
    "Progressive Scuba Gear": ItemDef(
        "Progressive Scuba Gear",
        net_id(342),
        "progressive",
        {"silent": True, "items": [302, 322]},
        persistent=True,
        unique=True,
        progression=True,
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
        {"invnum": 4, "capacity": 100},
        persistent=True,
        unique=True,
        progression=True,
    ),
    "Jetpack Capacity": ItemDef(
        "Jetpack Capacity",
        net_id(324),
        "invcapacity",
        {"invnum": 4, "capacity": 100},
        persistent=True,
        progression=True,
    ),
    "Progressive Jetpack": ItemDef(
        "Progressive Jetpack",
        net_id(344),
        "progressive",
        {"silent": True, "items": [304, 324]},
        persistent=True,
        unique=True,
        progression=True,
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
        net_id(350),
        "ability",
        {"enables": "dive"},
        persistent=True,
        unique=True,
        progression=True,
    ),
    "Crouch": ItemDef(
        "Crouch",
        net_id(350),
        "ability",
        {"enables": "crouch"},
        persistent=True,
        unique=True,
        progression=True,
    ),
    "Sprint": ItemDef(
        "Sprint",
        net_id(350),
        "ability",
        {"enables": "run"},
        persistent=True,
        unique=True,
        progression=True,
    ),
}

all_items = {
    **junk_items,
    **goal_items,
    **weapons,
    **inventory_items,
    **abilities,
    **dynamic_level_items,
}
