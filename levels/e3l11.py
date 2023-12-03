from BaseClasses import Region

from ..base_classes import D3DLevel


class E3L11(D3DLevel):
    name = "Freeway"
    levelnum = 10
    volumenum = 2
    keys = ["Red"]
    location_defs = [
        {"id": 20, "name": "20 Armor", "type": "sprite"},
        {"id": 21, "name": "21 Night Vision Goggles", "type": "sprite"},
        {"id": 24, "name": "24 Pipebombs", "type": "sprite"},
        {"id": 33, "name": "33 Shotgun", "type": "sprite"},
        {"id": 61, "name": "61 Tripmine", "type": "sprite"},
        {"id": 62, "name": "62 Tripmine", "type": "sprite"},
        {"id": 72, "name": "72 Steroids", "type": "sprite"},
        {"id": 73, "name": "73 Steroids", "type": "sprite"},
        {"id": 81, "name": "81 Pipebombs", "type": "sprite"},
        {"id": 211, "name": "211 Jetpack", "type": "sprite"},
        {"id": 361, "name": "361 RPG", "type": "sprite"},
        {"id": 363, "name": "363 Atomic Health", "type": "sprite"},
        {"id": 364, "name": "364 Armor", "type": "sprite"},
        {"id": 366, "name": "366 Devastator", "type": "sprite"},
        {"id": 367, "name": "367 Medkit", "type": "sprite"},
        {"id": 372, "name": "372 Night Vision Goggles", "type": "sprite"},
        {"id": 376, "name": "376 Atomic Health", "type": "sprite"},
        {"id": 377, "name": "377 Atomic Health", "type": "sprite"},
        {"id": 378, "name": "378 Medkit", "type": "sprite"},
        {"id": 379, "name": "379 Armor", "type": "sprite"},
        {"id": 381, "name": "381 Chaingun", "type": "sprite"},
        {"id": 384, "name": "384 Pipebombs", "type": "sprite"},
        {"id": 386, "name": "386 RPG", "type": "sprite"},
        {"id": 387, "name": "387 Freezethrower", "type": "sprite"},
        {"id": 388, "name": "388 Shrinker", "type": "sprite"},
        {"id": 390, "name": "390 Freezethrower", "type": "sprite"},
        {"id": 394, "name": "394 Shotgun", "type": "sprite"},
        {"id": 399, "mp": True, "name": "MP 399 Jetpack", "type": "sprite"},
        {"id": 463, "name": "463 Blue Key Card", "type": "sprite"},
        {"id": 465, "name": "465 Red Key Card", "type": "sprite"},
        {"id": 120, "name": "Secret 1", "type": "sector"},
        {"id": 148, "name": "Secret 2", "type": "sector"},
        {"id": 229, "name": "Secret 3", "type": "sector"},
        {"id": 242, "name": "Secret 4", "type": "sector"},
        {"id": 246, "name": "Secret 5", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
