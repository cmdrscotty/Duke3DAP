from BaseClasses import Region

from ..base_classes import D3DLevel


class E3L6(D3DLevel):
    name = "Rabid Transit"
    levelnum = 5
    volumenum = 2
    keys = ["Red"]
    location_defs = [
        {"id": 1, "name": "1 Steroids", "type": "sprite"},
        {"id": 8, "name": "8 Red Key Card", "type": "sprite"},
        {"id": 20, "name": "20 Freezethrower", "type": "sprite"},
        {"id": 21, "name": "21 Pipebombs", "type": "sprite"},
        {"id": 53, "name": "53 Atomic Health", "type": "sprite"},
        {"id": 91, "name": "91 Shrinker", "type": "sprite"},
        {"id": 92, "name": "92 Atomic Health", "type": "sprite"},
        {"id": 140, "name": "140 Devastator", "type": "sprite"},
        {"id": 283, "name": "283 Night Vision Goggles", "type": "sprite"},
        {"id": 296, "name": "296 Blue Key Card", "type": "sprite"},
        {"id": 333, "name": "333 Shotgun", "type": "sprite"},
        {"id": 334, "name": "334 Chaingun", "type": "sprite"},
        {"id": 339, "name": "339 Holo Duke", "type": "sprite"},
        {"id": 342, "name": "342 Pipebombs", "type": "sprite"},
        {"id": 361, "name": "361 Armor", "type": "sprite"},
        {"id": 362, "name": "362 Medkit", "type": "sprite"},
        {"id": 364, "name": "364 Atomic Health", "type": "sprite"},
        {"id": 365, "name": "365 Chaingun", "type": "sprite"},
        {"id": 366, "name": "366 Atomic Health", "type": "sprite"},
        {"id": 367, "name": "367 RPG", "type": "sprite"},
        {"id": 368, "name": "368 Medkit", "type": "sprite"},
        {"id": 385, "name": "385 Tripbomb", "type": "sprite"},
        {"id": 386, "name": "386 Tripbomb", "type": "sprite"},
        {"id": 387, "name": "387 Tripbomb", "type": "sprite"},
        {"id": 388, "name": "388 Tripbomb", "type": "sprite"},
        {"id": 389, "name": "389 Tripbomb", "type": "sprite"},
        {
            "id": 411,
            "mp": True,
            "name": "MP 411 Night Vision Goggles",
            "type": "sprite",
        },
        {"id": 429, "name": "429 Devastator", "type": "sprite"},
        {"id": 472, "name": "472 Atomic Health", "type": "sprite"},
        {"id": 6, "name": "Secret 1", "type": "sector"},
        {"id": 132, "name": "Secret 2", "type": "sector"},
        {"id": 149, "name": "Secret 3", "type": "sector"},
        {"id": 163, "name": "Secret 4", "type": "sector"},
        {"id": 172, "name": "Secret 5", "type": "sector"},
        {"id": 182, "name": "Secret 6", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
