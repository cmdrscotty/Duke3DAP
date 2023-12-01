from BaseClasses import Region

from ..base_classes import D3DLevel


class E3L6(D3DLevel):
    name = "Rabid Transit"
    levelnum = 5
    volumenum = 2
    keys = ["Red"]
    location_defs = [
        {"id": 1, "mp": True, "name": "MP 1 Steroids", "type": "sprite"},
        {"id": 8, "name": "8 Red Key Card", "type": "sprite"},
        {"id": 20, "mp": True, "name": "MP 20 Freezethrower", "type": "sprite"},
        {"id": 21, "mp": True, "name": "MP 21 Pipebombs", "type": "sprite"},
        {"id": 53, "mp": True, "name": "MP 53 Atomic Health", "type": "sprite"},
        {"id": 91, "mp": True, "name": "MP 91 Shrinker", "type": "sprite"},
        {"id": 92, "mp": True, "name": "MP 92 Atomic Health", "type": "sprite"},
        {"id": 140, "mp": True, "name": "MP 140 Devastator", "type": "sprite"},
        {
            "id": 283,
            "mp": True,
            "name": "MP 283 Night Vision Goggles",
            "type": "sprite",
        },
        {"id": 296, "mp": True, "name": "MP 296 Blue Key Card", "type": "sprite"},
        {"id": 333, "mp": True, "name": "MP 333 Shotgun", "type": "sprite"},
        {"id": 334, "mp": True, "name": "MP 334 Chaingun", "type": "sprite"},
        {"id": 339, "mp": True, "name": "MP 339 Holo Duke", "type": "sprite"},
        {"id": 342, "mp": True, "name": "MP 342 Pipebombs", "type": "sprite"},
        {"id": 361, "mp": True, "name": "MP 361 Armor", "type": "sprite"},
        {"id": 362, "mp": True, "name": "MP 362 Medkit", "type": "sprite"},
        {"id": 364, "mp": True, "name": "MP 364 Atomic Health", "type": "sprite"},
        {"id": 365, "mp": True, "name": "MP 365 Chaingun", "type": "sprite"},
        {"id": 366, "mp": True, "name": "MP 366 Atomic Health", "type": "sprite"},
        {"id": 367, "mp": True, "name": "MP 367 RPG", "type": "sprite"},
        {"id": 368, "mp": True, "name": "MP 368 Medkit", "type": "sprite"},
        {"id": 385, "mp": True, "name": "MP 385 Tripbomb", "type": "sprite"},
        {"id": 386, "mp": True, "name": "MP 386 Tripbomb", "type": "sprite"},
        {"id": 387, "mp": True, "name": "MP 387 Tripbomb", "type": "sprite"},
        {"id": 388, "mp": True, "name": "MP 388 Tripbomb", "type": "sprite"},
        {"id": 389, "mp": True, "name": "MP 389 Tripbomb", "type": "sprite"},
        {"id": 411, "name": "411 Night Vision Goggles", "type": "sprite"},
        {"id": 429, "mp": True, "name": "MP 429 Devastator", "type": "sprite"},
        {"id": 472, "mp": True, "name": "MP 472 Atomic Health", "type": "sprite"},
        {"id": 6, "name": "Secret 1", "type": "sector"},
        {"id": 132, "name": "Secret 2", "type": "sector"},
        {"id": 149, "name": "Secret 3", "type": "sector"},
        {"id": 163, "name": "Secret 4", "type": "sector"},
        {"id": 172, "name": "Secret 5", "type": "sector"},
        {"id": 182, "name": "Secret 6", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
