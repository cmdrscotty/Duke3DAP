from BaseClasses import Region

from ..base_classes import D3DLevel


class E4L1(D3DLevel):
    name = "It's Impossible"
    levelnum = 0
    volumenum = 3
    keys = ["Red"]
    location_defs = [
        {"id": 4, "mp": True, "name": "MP 4 Tripbomb", "type": "sprite"},
        {"id": 47, "mp": True, "name": "MP 47 Freezethrower", "type": "sprite"},
        {"id": 53, "mp": True, "name": "MP 53 Night Vision Goggles", "type": "sprite"},
        {"id": 54, "mp": True, "name": "MP 54 Holo Duke", "type": "sprite"},
        {"id": 56, "mp": True, "name": "MP 56 Pipebombs", "type": "sprite"},
        {"id": 135, "name": "135 Red Key Card", "type": "sprite"},
        {"id": 136, "mp": True, "name": "MP 136 Blue Key Card", "type": "sprite"},
        {"id": 149, "mp": True, "name": "MP 149 Tripbomb", "type": "sprite"},
        {"id": 150, "mp": True, "name": "MP 150 Tripbomb", "type": "sprite"},
        {"id": 151, "mp": True, "name": "MP 151 Pipebombs", "type": "sprite"},
        {"id": 152, "name": "152 Steroids", "type": "sprite"},
        {"id": 170, "mp": True, "name": "MP 170 Atomic Health", "type": "sprite"},
        {"id": 192, "mp": True, "name": "MP 192 Atomic Health", "type": "sprite"},
        {"id": 373, "mp": True, "name": "MP 373 RPG", "type": "sprite"},
        {"id": 407, "mp": True, "name": "MP 407 Medkit", "type": "sprite"},
        {"id": 419, "mp": True, "name": "MP 419 Armor", "type": "sprite"},
        {"id": 539, "mp": True, "name": "MP 539 Shotgun", "type": "sprite"},
        {"id": 540, "mp": True, "name": "MP 540 Chaingun", "type": "sprite"},
        {"id": 544, "name": "544 Shotgun", "type": "sprite"},
        {"id": 545, "name": "545 Chaingun", "type": "sprite"},
        {"id": 562, "mp": True, "name": "MP 562 Pipebombs", "type": "sprite"},
        {"id": 563, "mp": True, "name": "MP 563 Atomic Health", "type": "sprite"},
        {"id": 633, "mp": True, "name": "MP 633 Shrinker", "type": "sprite"},
        {"id": 634, "mp": True, "name": "MP 634 Armor", "type": "sprite"},
        {"id": 655, "mp": True, "name": "MP 655 Devastator", "type": "sprite"},
        {"id": 674, "mp": True, "name": "MP 674 Pipebombs", "type": "sprite"},
        {"id": 839, "mp": True, "name": "MP 839 Steroids", "type": "sprite"},
        {"id": 840, "mp": True, "name": "MP 840 Jetpack", "type": "sprite"},
        {"id": 116, "name": "Secret 1", "type": "sector"},
        {"id": 221, "name": "Secret 2", "type": "sector"},
        {"id": 232, "name": "Secret 3", "type": "sector"},
        {"id": 270, "name": "Secret 4", "type": "sector"},
        {"id": 274, "name": "Secret 5", "type": "sector"},
        {"id": 388, "name": "Secret 6", "type": "sector"},
        {"id": 414, "name": "Secret 7", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
