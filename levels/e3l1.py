from BaseClasses import Region

from ..base_classes import D3DLevel


class E3L1(D3DLevel):
    name = "Raw Meat"
    levelnum = 0
    volumenum = 2
    keys = ["Red"]
    location_defs = [
        {"id": 78, "mp": True, "name": "MP 78 Jetpack", "type": "sprite"},
        {"id": 115, "mp": True, "name": "MP 115 Chaingun", "type": "sprite"},
        {"id": 116, "mp": True, "name": "MP 116 Atomic Health", "type": "sprite"},
        {"id": 161, "mp": True, "name": "MP 161 Atomic Health", "type": "sprite"},
        {"id": 305, "mp": True, "name": "MP 305 Freezethrower", "type": "sprite"},
        {"id": 308, "mp": True, "name": "MP 308 Atomic Health", "type": "sprite"},
        {"id": 309, "mp": True, "name": "MP 309 Pipebombs", "type": "sprite"},
        {"id": 389, "mp": True, "name": "MP 389 Steroids", "type": "sprite"},
        {"id": 452, "mp": True, "name": "MP 452 Blue Key Card", "type": "sprite"},
        {"id": 457, "name": "457 Red Key Card", "type": "sprite"},
        {"id": 492, "mp": True, "name": "MP 492 Shotgun", "type": "sprite"},
        {"id": 497, "mp": True, "name": "MP 497 Shrinker", "type": "sprite"},
        {"id": 499, "mp": True, "name": "MP 499 Steroids", "type": "sprite"},
        {"id": 500, "mp": True, "name": "MP 500 Medkit", "type": "sprite"},
        {"id": 524, "mp": True, "name": "MP 524 RPG", "type": "sprite"},
        {"id": 536, "mp": True, "name": "MP 536 Jetpack", "type": "sprite"},
        {"id": 543, "mp": True, "name": "MP 543 Pipebombs", "type": "sprite"},
        {"id": 561, "mp": True, "name": "MP 561 Atomic Health", "type": "sprite"},
        {"id": 564, "mp": True, "name": "MP 564 Armor", "type": "sprite"},
        {"id": 569, "mp": True, "name": "MP 569 Tripbomb", "type": "sprite"},
        {
            "id": 570,
            "mp": True,
            "name": "MP 570 Night Vision Goggles",
            "type": "sprite",
        },
        {"id": 574, "name": "574 Shotgun", "type": "sprite"},
        {"id": 575, "name": "575 Chaingun", "type": "sprite"},
        {"id": 577, "name": "577 Medkit", "type": "sprite"},
        {"id": 608, "mp": True, "name": "MP 608 Devastator", "type": "sprite"},
        {"id": 609, "mp": True, "name": "MP 609 Holo Duke", "type": "sprite"},
        {"id": 624, "mp": True, "name": "MP 624 Pipebombs", "type": "sprite"},
        {"id": 632, "mp": True, "name": "MP 632 Scuba Gear", "type": "sprite"},
        {"id": 636, "mp": True, "name": "MP 636 Armor", "type": "sprite"},
        {
            "id": 656,
            "mp": True,
            "name": "MP 656 Night Vision Goggles",
            "type": "sprite",
        },
        {"id": 135, "name": "Secret 1", "type": "sector"},
        {"id": 137, "name": "Secret 2", "type": "sector"},
        {"id": 161, "name": "Secret 3", "type": "sector"},
        {"id": 287, "name": "Secret 4", "type": "sector"},
        {"id": 332, "name": "Secret 5", "type": "sector"},
        {"id": 338, "name": "Secret 6", "type": "sector"},
        {"id": 344, "name": "Secret 7", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
