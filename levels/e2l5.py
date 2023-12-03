from BaseClasses import Region

from ..base_classes import D3DLevel


class E2L5(D3DLevel):
    name = "Occupied Territory"
    levelnum = 4
    volumenum = 1
    keys = ["Red"]
    location_defs = [
        {"id": 71, "name": "71 RPG", "type": "sprite"},
        {"id": 85, "name": "85 Armor", "type": "sprite"},
        {"id": 90, "mp": True, "name": "MP 90 Freezethrower", "type": "sprite"},
        {"id": 94, "name": "94 Pipebombs", "type": "sprite"},
        {"id": 95, "name": "95 Tripmine", "type": "sprite"},
        {"id": 96, "name": "96 Tripmine", "type": "sprite"},
        {"id": 97, "mp": True, "name": "MP 97 Pipebombs", "type": "sprite"},
        {"id": 110, "name": "110 Blue Key Card", "type": "sprite"},
        {"id": 299, "name": "299 Red Key Card", "type": "sprite"},
        {"id": 317, "name": "317 Atomic Health", "type": "sprite"},
        {"id": 346, "name": "346 Devastator", "type": "sprite"},
        {"id": 365, "name": "365 Chaingun", "type": "sprite"},
        {"id": 366, "name": "366 Medkit", "type": "sprite"},
        {"id": 367, "name": "367 Holo Duke", "type": "sprite"},
        {"id": 369, "mp": True, "name": "MP 369 Shrinker", "type": "sprite"},
        {"id": 370, "name": "370 Medkit", "type": "sprite"},
        {"id": 372, "name": "372 Shotgun", "type": "sprite"},
        {"id": 373, "name": "373 Steroids", "type": "sprite"},
        {"id": 376, "mp": True, "name": "MP 376 Jetpack", "type": "sprite"},
        {"id": 377, "name": "377 Pipebombs", "type": "sprite"},
        {"id": 378, "name": "378 Atomic Health", "type": "sprite"},
        {"id": 384, "name": "384 Atomic Health", "type": "sprite"},
        {"id": 386, "mp": True, "name": "MP 386 RPG", "type": "sprite"},
        {"id": 426, "name": "426 Night Vision Goggles", "type": "sprite"},
        {"id": 427, "name": "427 Night Vision Goggles", "type": "sprite"},
        {"id": 428, "name": "428 Night Vision Goggles", "type": "sprite"},
        {"id": 429, "name": "429 Armor", "type": "sprite"},
        {"id": 136, "name": "Secret 1", "type": "sector"},
        {"id": 185, "name": "Secret 2", "type": "sector"},
        {"id": 225, "name": "Secret 3", "type": "sector"},
        {"id": 238, "name": "Secret 4", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
        {"id": 9, "name": "Secret Exit", "type": "exit"},
    ]
