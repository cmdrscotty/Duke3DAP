from BaseClasses import Region

from ..base_classes import D3DLevel


class E3L1(D3DLevel):
    name = "Raw Meat"
    levelnum = 0
    volumenum = 2
    keys = ["Red"]
    location_defs = [
        {"id": 78, "name": "78 Jetpack", "type": "sprite"},
        {"id": 115, "name": "115 Chaingun", "type": "sprite"},
        {"id": 116, "name": "116 Atomic Health", "type": "sprite"},
        {"id": 161, "name": "161 Atomic Health", "type": "sprite"},
        {"id": 305, "name": "305 Freezethrower", "type": "sprite"},
        {"id": 308, "name": "308 Atomic Health", "type": "sprite"},
        {"id": 309, "name": "309 Pipebombs", "type": "sprite"},
        {"id": 389, "name": "389 Steroids", "type": "sprite"},
        {"id": 452, "name": "452 Blue Key Card", "type": "sprite"},
        {"id": 457, "name": "457 Red Key Card", "type": "sprite"},
        {"id": 492, "name": "492 Shotgun", "type": "sprite"},
        {"id": 497, "name": "497 Shrinker", "type": "sprite"},
        {"id": 499, "name": "499 Steroids", "type": "sprite"},
        {"id": 500, "name": "500 Medkit", "type": "sprite"},
        {"id": 524, "name": "524 RPG", "type": "sprite"},
        {"id": 536, "name": "536 Jetpack", "type": "sprite"},
        {"id": 543, "name": "543 Pipebombs", "type": "sprite"},
        {"id": 561, "name": "561 Atomic Health", "type": "sprite"},
        {"id": 564, "name": "564 Armor", "type": "sprite"},
        {"id": 569, "name": "569 Tripbomb", "type": "sprite"},
        {"id": 570, "name": "570 Night Vision Goggles", "type": "sprite"},
        {"id": 574, "mp": True, "name": "MP 574 Shotgun", "type": "sprite"},
        {"id": 575, "mp": True, "name": "MP 575 Chaingun", "type": "sprite"},
        {"id": 577, "mp": True, "name": "MP 577 Medkit", "type": "sprite"},
        {"id": 608, "name": "608 Devastator", "type": "sprite"},
        {"id": 609, "name": "609 Holo Duke", "type": "sprite"},
        {"id": 624, "name": "624 Pipebombs", "type": "sprite"},
        {"id": 632, "name": "632 Scuba Gear", "type": "sprite"},
        {"id": 636, "name": "636 Armor", "type": "sprite"},
        {"id": 656, "name": "656 Night Vision Goggles", "type": "sprite"},
        {"id": 135, "name": "Secret 1", "type": "sector"},
        {"id": 137, "name": "Secret 2", "type": "sector"},
        {"id": 161, "name": "Secret 3", "type": "sector"},
        {"id": 287, "name": "Secret 4", "type": "sector"},
        {"id": 332, "name": "Secret 5", "type": "sector"},
        {"id": 338, "name": "Secret 6", "type": "sector"},
        {"id": 344, "name": "Secret 7", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
