from BaseClasses import Region

from ..base_classes import D3DLevel


class E1L3(D3DLevel):
    name = "Death Row"
    levelnum = 2
    volumenum = 0
    keys = ["Blue", "Red", "Yellow"]
    location_defs = [
        {"name": "Control Room Secret Atomic Health", "id": 48, "type": "sprite"},
        {"name": "Control Room Vent Armor", "id": 79, "type": "sprite"},
        {"name": "Electric Chair Medkit", "id": 160, "type": "sprite"},
        {
            "name": "Cell Black 01 Broken Wall Atomic Health",
            "id": 185,
            "type": "sprite",
        },
        {"name": "Electric Chair Shotgun", "id": 236, "type": "sprite"},
        {"name": "Control Room Secret Pipebombs", "id": 269, "type": "sprite"},
        {"name": "Submarine Gate Scuba Gear", "id": 280, "type": "sprite"},
        {"name": "Gear Room Atomic Health", "id": 367, "type": "sprite"},
        {"name": "Cell BLock 01 RPG", "id": 411, "type": "sprite"},
        {"name": "MP Outside Medkit", "id": 413, "type": "sprite", "mp": True},
        {"name": "Yellow Key Card", "id": 485, "type": "sprite"},
        {"name": "Outside Hidden Tunnel Atomic Health 1", "id": 488, "type": "sprite"},
        {"name": "Outside Hidden Tunnel Atomic Health 2", "id": 489, "type": "sprite"},
        {"name": "Outside Hidden Tunnel Atomic Health 3", "id": 490, "type": "sprite"},
        {"name": "Submarine Engine Room Medkit", "id": 504, "type": "sprite"},
        {"name": "Underwater Pipebombs", "id": 532, "type": "sprite"},
        {"name": "Chapel Chaingun", "id": 564, "type": "sprite"},
        {"name": "MP Showers Shotgun", "id": 598, "type": "sprite"},
        {"name": "Showers Protective Boots", "id": 606, "type": "sprite"},
        {
            "name": "Hanged Monk Atomic Health",
            "id": 642,
            "type": "sprite",
            "sprite_type": "monk",
        },
        {"name": "Gallery Holo Duke", "id": 672, "type": "sprite"},
        {"name": "Chapel Rafters Armor", "id": 676, "type": "sprite"},
        {"name": "Chapel Rafters Atomic Health", "id": 677, "type": "sprite"},
        {"name": "Gear Room Night Vision Goggles", "id": 697, "type": "sprite"},
        {"name": "Blue Key Card", "id": 699, "type": "sprite"},
        {
            "name": "Submarine Gate Hidden Night Vision Goggles",
            "id": 803,
            "type": "sprite",
        },
        {"name": "Breakable Canyon Wall Steroids", "id": 813, "type": "sprite"},
        {"name": "Outside Pipebombs", "id": 847, "type": "sprite"},
        {"name": "Red Key Card", "id": 851, "type": "sprite"},
        {"name": "Gear Room RPG", "id": 856, "type": "sprite"},
        {
            "name": "MP Cell Block 01 Broken Wall Holo Duke",
            "id": 870,
            "type": "sprite",
            "mp": True,
        },
        {"name": "Control Room Chaingun", "id": 899, "type": "sprite"},
        {"name": "Chapel Window Steroids", "id": 902, "type": "sprite"},
        {"name": "MP Cell Block 02 Jetpack", "id": 903, "type": "sprite", "mp": True},
        {"name": "Outside Hidden Tunnel", "id": 76, "type": "sector"},
        {"name": "Electric Chair", "id": 296, "type": "sector"},
        {"name": "Chapel Rafters", "id": 304, "type": "sector"},
        {"name": "Chapel Window", "id": 317, "type": "sector"},
        {"name": "Behind Bed", "id": 379, "type": "sector"},
        {"name": "Submarine Engine Room", "id": 387, "type": "sector"},
        {"name": "Submarine Gate Hidden Alcove", "id": 393, "type": "sector"},
        {"name": "Breakable Canyon Wall", "id": 401, "type": "sector"},
        {"name": "Control Room Right Alcove", "id": 424, "type": "sector"},
        {"name": "Control Room Left Alcove", "id": 426, "type": "sector"},
        {"name": "Exit", "id": 0, "type": "exit"},
    ]
