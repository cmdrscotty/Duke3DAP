from BaseClasses import Region

from ..base_classes import D3DLevel


class E4L1(D3DLevel):
    name = "It's Impossible"
    levelnum = 0
    volumenum = 3
    keys = ["Red"]
    location_defs = [
        {"id": 4, "name": "4 Tripmine", "type": "sprite"},
        {"id": 47, "name": "47 Freezethrower", "type": "sprite"},
        {"id": 53, "name": "53 Night Vision Goggles", "type": "sprite"},
        {"id": 54, "name": "54 Holo Duke", "type": "sprite"},
        {"id": 56, "name": "56 Pipebombs", "type": "sprite"},
        {"id": 135, "name": "135 Red Key Card", "type": "sprite"},
        {"id": 136, "name": "136 Blue Key Card", "type": "sprite"},
        {"id": 149, "name": "149 Tripmine", "type": "sprite"},
        {"id": 150, "name": "150 Tripmine", "type": "sprite"},
        {"id": 151, "name": "151 Pipebombs", "type": "sprite"},
        {"id": 152, "mp": True, "name": "MP 152 Steroids", "type": "sprite"},
        {"id": 170, "name": "170 Atomic Health", "type": "sprite"},
        {"id": 192, "name": "192 Atomic Health", "type": "sprite"},
        {"id": 373, "name": "373 RPG", "type": "sprite"},
        {"id": 407, "name": "407 Medkit", "type": "sprite"},
        {"id": 419, "name": "419 Armor", "type": "sprite"},
        {"id": 539, "name": "539 Shotgun", "type": "sprite"},
        {"id": 540, "name": "540 Chaingun", "type": "sprite"},
        {"id": 544, "mp": True, "name": "MP 544 Shotgun", "type": "sprite"},
        {"id": 545, "mp": True, "name": "MP 545 Chaingun", "type": "sprite"},
        {"id": 562, "name": "562 Pipebombs", "type": "sprite"},
        {"id": 563, "name": "563 Atomic Health", "type": "sprite"},
        {"id": 633, "name": "633 Shrinker", "type": "sprite"},
        {"id": 634, "name": "634 Armor", "type": "sprite"},
        {"id": 655, "name": "655 Devastator", "type": "sprite"},
        {"id": 674, "name": "674 Pipebombs", "type": "sprite"},
        {"id": 839, "name": "839 Steroids", "type": "sprite"},
        {"id": 840, "name": "840 Jetpack", "type": "sprite"},
        {"id": 116, "name": "Secret 1", "type": "sector"},
        {"id": 221, "name": "Secret 2", "type": "sector"},
        {"id": 232, "name": "Secret 3", "type": "sector"},
        {"id": 270, "name": "Secret 4", "type": "sector"},
        {"id": 274, "name": "Secret 5", "type": "sector"},
        {"id": 388, "name": "Secret 6", "type": "sector"},
        {"id": 414, "name": "Secret 7", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
