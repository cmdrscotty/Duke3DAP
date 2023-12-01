from BaseClasses import Region

from ..base_classes import D3DLevel


class E2L5(D3DLevel):
    name = "Occupied Territory"
    levelnum = 4
    volumenum = 1
    keys = ["Red"]
    location_defs = [
        {"id": 71, "mp": True, "name": "MP 71 RPG", "type": "sprite"},
        {"id": 85, "mp": True, "name": "MP 85 Armor", "type": "sprite"},
        {"id": 90, "name": "90 Freezethrower", "type": "sprite"},
        {"id": 94, "mp": True, "name": "MP 94 Pipebombs", "type": "sprite"},
        {"id": 95, "mp": True, "name": "MP 95 Tripbomb", "type": "sprite"},
        {"id": 96, "mp": True, "name": "MP 96 Tripbomb", "type": "sprite"},
        {"id": 97, "name": "97 Pipebombs", "type": "sprite"},
        {"id": 110, "mp": True, "name": "MP 110 Blue Key Card", "type": "sprite"},
        {"id": 299, "name": "299 Red Key Card", "type": "sprite"},
        {"id": 317, "mp": True, "name": "MP 317 Atomic Health", "type": "sprite"},
        {"id": 346, "mp": True, "name": "MP 346 Devastator", "type": "sprite"},
        {"id": 365, "mp": True, "name": "MP 365 Chaingun", "type": "sprite"},
        {"id": 366, "mp": True, "name": "MP 366 Medkit", "type": "sprite"},
        {"id": 367, "mp": True, "name": "MP 367 Holo Duke", "type": "sprite"},
        {"id": 369, "name": "369 Shrinker", "type": "sprite"},
        {"id": 370, "mp": True, "name": "MP 370 Medkit", "type": "sprite"},
        {"id": 372, "mp": True, "name": "MP 372 Shotgun", "type": "sprite"},
        {"id": 373, "mp": True, "name": "MP 373 Steroids", "type": "sprite"},
        {"id": 376, "name": "376 Jetpack", "type": "sprite"},
        {"id": 377, "mp": True, "name": "MP 377 Pipebombs", "type": "sprite"},
        {"id": 378, "mp": True, "name": "MP 378 Atomic Health", "type": "sprite"},
        {"id": 384, "mp": True, "name": "MP 384 Atomic Health", "type": "sprite"},
        {"id": 386, "name": "386 RPG", "type": "sprite"},
        {
            "id": 426,
            "mp": True,
            "name": "MP 426 Night Vision Goggles",
            "type": "sprite",
        },
        {
            "id": 427,
            "mp": True,
            "name": "MP 427 Night Vision Goggles",
            "type": "sprite",
        },
        {
            "id": 428,
            "mp": True,
            "name": "MP 428 Night Vision Goggles",
            "type": "sprite",
        },
        {"id": 429, "mp": True, "name": "MP 429 Armor", "type": "sprite"},
        {"id": 136, "name": "Secret 1", "type": "sector"},
        {"id": 185, "name": "Secret 2", "type": "sector"},
        {"id": 225, "name": "Secret 3", "type": "sector"},
        {"id": 238, "name": "Secret 4", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
