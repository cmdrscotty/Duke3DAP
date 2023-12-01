from BaseClasses import Region

from ..base_classes import D3DLevel


class E3L5(D3DLevel):
    name = "Movie Set"
    levelnum = 4
    volumenum = 2
    keys = ["Red"]
    location_defs = [
        {"id": 0, "mp": True, "name": "MP 0 Night Vision Goggles", "type": "sprite"},
        {"id": 9, "mp": True, "name": "MP 9 Atomic Health", "type": "sprite"},
        {"id": 24, "mp": True, "name": "MP 24 Night Vision Goggles", "type": "sprite"},
        {"id": 39, "mp": True, "name": "MP 39 Night Vision Goggles", "type": "sprite"},
        {"id": 40, "mp": True, "name": "MP 40 Atomic Health", "type": "sprite"},
        {"id": 41, "mp": True, "name": "MP 41 Jetpack", "type": "sprite"},
        {"id": 43, "mp": True, "name": "MP 43 Freezethrower", "type": "sprite"},
        {"id": 47, "mp": True, "name": "MP 47 Medkit", "type": "sprite"},
        {"id": 51, "mp": True, "name": "MP 51 Atomic Health", "type": "sprite"},
        {"id": 61, "mp": True, "name": "MP 61 Medkit", "type": "sprite"},
        {"id": 71, "name": "71 Yellow Key Card", "type": "sprite"},
        {"id": 80, "mp": True, "name": "MP 80 Atomic Health", "type": "sprite"},
        {"id": 81, "mp": True, "name": "MP 81 Devastator", "type": "sprite"},
        {"id": 105, "name": "105 Red Key Card", "type": "sprite"},
        {"id": 170, "mp": True, "name": "MP 170 Chaingun", "type": "sprite"},
        {"id": 257, "mp": True, "name": "MP 257 Armor", "type": "sprite"},
        {"id": 258, "mp": True, "name": "MP 258 Blue Key Card", "type": "sprite"},
        {"id": 261, "mp": True, "name": "MP 261 Holo Duke", "type": "sprite"},
        {"id": 267, "mp": True, "name": "MP 267 Shotgun", "type": "sprite"},
        {"id": 268, "mp": True, "name": "MP 268 Medkit", "type": "sprite"},
        {"id": 364, "mp": True, "name": "MP 364 Atomic Health", "type": "sprite"},
        {"id": 367, "mp": True, "name": "MP 367 RPG", "type": "sprite"},
        {"id": 371, "mp": True, "name": "MP 371 Steroids", "type": "sprite"},
        {"id": 380, "mp": True, "name": "MP 380 Pipebombs", "type": "sprite"},
        {"id": 415, "mp": True, "name": "MP 415 Pipebombs", "type": "sprite"},
        {"id": 416, "mp": True, "name": "MP 416 Tripbomb", "type": "sprite"},
        {"id": 417, "mp": True, "name": "MP 417 Tripbomb", "type": "sprite"},
        {"id": 418, "mp": True, "name": "MP 418 Shrinker", "type": "sprite"},
        {"id": 424, "mp": True, "name": "MP 424 Atomic Health", "type": "sprite"},
        {"id": 425, "mp": True, "name": "MP 425 Atomic Health", "type": "sprite"},
        {"id": 426, "mp": True, "name": "MP 426 Atomic Health", "type": "sprite"},
        {"id": 480, "mp": True, "name": "MP 480 Jetpack", "type": "sprite"},
        {"id": 487, "mp": True, "name": "MP 487 Chaingun", "type": "sprite"},
        {"id": 88, "name": "Secret 1", "type": "sector"},
        {"id": 149, "name": "Secret 2", "type": "sector"},
        {"id": 183, "name": "Secret 3", "type": "sector"},
        {"id": 195, "name": "Secret 4", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
