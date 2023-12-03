from BaseClasses import Region

from ..base_classes import D3DLevel


class E3L10(D3DLevel):
    name = "Tier Drops"
    levelnum = 9
    volumenum = 2
    keys = ["Red"]
    location_defs = [
        {"id": 0, "name": "0 Shotgun", "type": "sprite"},
        {"id": 3, "name": "3 Shotgun", "type": "sprite"},
        {"id": 13, "name": "13 Tripmine", "type": "sprite"},
        {"id": 14, "name": "14 Tripmine", "type": "sprite"},
        {"id": 15, "name": "15 Tripmine", "type": "sprite"},
        {"id": 16, "name": "16 Armor", "type": "sprite"},
        {"id": 17, "name": "17 Night Vision Goggles", "type": "sprite"},
        {"id": 18, "name": "18 Medkit", "type": "sprite"},
        {"id": 21, "name": "21 Jetpack", "type": "sprite"},
        {"id": 30, "name": "30 Pipebombs", "type": "sprite"},
        {"id": 31, "name": "31 Pipebombs", "type": "sprite"},
        {"id": 38, "name": "38 Freezethrower", "type": "sprite"},
        {"id": 209, "name": "209 RPG", "type": "sprite"},
        {"id": 210, "name": "210 Armor", "type": "sprite"},
        {"id": 251, "name": "251 Chaingun", "type": "sprite"},
        {"id": 276, "name": "276 Shrinker", "type": "sprite"},
        {"id": 282, "name": "282 Devastator", "type": "sprite"},
        {"id": 283, "name": "283 Steroids", "type": "sprite"},
        {"id": 290, "name": "290 Holo Duke", "type": "sprite"},
        {"id": 314, "name": "314 Atomic Health", "type": "sprite"},
        {"id": 315, "name": "315 Atomic Health", "type": "sprite"},
        {"id": 316, "name": "316 Atomic Health", "type": "sprite"},
        {"id": 148, "name": "Secret 1", "type": "sector"},
        {"id": 156, "name": "Secret 2", "type": "sector"},
        {"id": 164, "name": "Secret 3", "type": "sector"},
        {"id": 172, "name": "Secret 4", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
