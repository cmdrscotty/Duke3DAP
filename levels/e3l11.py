from BaseClasses import Region

from ..base_classes import D3DLevel


class E3L11(D3DLevel):
    name = "Freeway"
    levelnum = 10
    volumenum = 2
    keys = ["Red"]
    location_defs = [
        {"id": 20, "mp": True, "name": "MP 20 Armor", "type": "sprite"},
        {"id": 21, "mp": True, "name": "MP 21 Night Vision Goggles", "type": "sprite"},
        {"id": 24, "mp": True, "name": "MP 24 Pipebombs", "type": "sprite"},
        {"id": 33, "mp": True, "name": "MP 33 Shotgun", "type": "sprite"},
        {"id": 61, "mp": True, "name": "MP 61 Tripbomb", "type": "sprite"},
        {"id": 62, "mp": True, "name": "MP 62 Tripbomb", "type": "sprite"},
        {"id": 72, "mp": True, "name": "MP 72 Steroids", "type": "sprite"},
        {"id": 73, "mp": True, "name": "MP 73 Steroids", "type": "sprite"},
        {"id": 81, "mp": True, "name": "MP 81 Pipebombs", "type": "sprite"},
        {"id": 211, "mp": True, "name": "MP 211 Jetpack", "type": "sprite"},
        {"id": 361, "mp": True, "name": "MP 361 RPG", "type": "sprite"},
        {"id": 363, "mp": True, "name": "MP 363 Atomic Health", "type": "sprite"},
        {"id": 364, "mp": True, "name": "MP 364 Armor", "type": "sprite"},
        {"id": 366, "mp": True, "name": "MP 366 Devastator", "type": "sprite"},
        {"id": 367, "mp": True, "name": "MP 367 Medkit", "type": "sprite"},
        {
            "id": 372,
            "mp": True,
            "name": "MP 372 Night Vision Goggles",
            "type": "sprite",
        },
        {"id": 376, "mp": True, "name": "MP 376 Atomic Health", "type": "sprite"},
        {"id": 377, "mp": True, "name": "MP 377 Atomic Health", "type": "sprite"},
        {"id": 378, "mp": True, "name": "MP 378 Medkit", "type": "sprite"},
        {"id": 379, "mp": True, "name": "MP 379 Armor", "type": "sprite"},
        {"id": 381, "mp": True, "name": "MP 381 Chaingun", "type": "sprite"},
        {"id": 384, "mp": True, "name": "MP 384 Pipebombs", "type": "sprite"},
        {"id": 386, "mp": True, "name": "MP 386 RPG", "type": "sprite"},
        {"id": 387, "mp": True, "name": "MP 387 Freezethrower", "type": "sprite"},
        {"id": 388, "mp": True, "name": "MP 388 Shrinker", "type": "sprite"},
        {"id": 390, "mp": True, "name": "MP 390 Freezethrower", "type": "sprite"},
        {"id": 394, "mp": True, "name": "MP 394 Shotgun", "type": "sprite"},
        {"id": 399, "name": "399 Jetpack", "type": "sprite"},
        {"id": 463, "mp": True, "name": "MP 463 Blue Key Card", "type": "sprite"},
        {"id": 465, "name": "465 Red Key Card", "type": "sprite"},
        {"id": 120, "name": "Secret 1", "type": "sector"},
        {"id": 148, "name": "Secret 2", "type": "sector"},
        {"id": 229, "name": "Secret 3", "type": "sector"},
        {"id": 242, "name": "Secret 4", "type": "sector"},
        {"id": 246, "name": "Secret 5", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
