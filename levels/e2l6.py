from BaseClasses import Region

from ..base_classes import D3DLevel


class E2L6(D3DLevel):
    name = "Tiberius Station"
    levelnum = 5
    volumenum = 1
    keys = ["Red"]
    location_defs = [
        {"id": 32, "mp": True, "name": "MP 32 RPG", "type": "sprite"},
        {"id": 42, "mp": True, "name": "MP 42 Protective Boots", "type": "sprite"},
        {"id": 43, "mp": True, "name": "MP 43 Scuba Gear", "type": "sprite"},
        {"id": 45, "mp": True, "name": "MP 45 Night Vision Goggles", "type": "sprite"},
        {"id": 46, "mp": True, "name": "MP 46 Medkit", "type": "sprite"},
        {"id": 115, "mp": True, "name": "MP 115 Jetpack", "type": "sprite"},
        {"id": 181, "mp": True, "name": "MP 181 Medkit", "type": "sprite"},
        {"id": 346, "mp": True, "name": "MP 346 Armor", "type": "sprite"},
        {"id": 347, "mp": True, "name": "MP 347 Armor", "type": "sprite"},
        {"id": 348, "mp": True, "name": "MP 348 Blue Key Card", "type": "sprite"},
        {"id": 430, "mp": True, "name": "MP 430 Pipebombs", "type": "sprite"},
        {"id": 431, "mp": True, "name": "MP 431 Pipebombs", "type": "sprite"},
        {"id": 490, "mp": True, "name": "MP 490 Shrinker", "type": "sprite"},
        {"id": 507, "mp": True, "name": "MP 507 Devastator", "type": "sprite"},
        {"id": 508, "mp": True, "name": "MP 508 Shotgun", "type": "sprite"},
        {"id": 509, "mp": True, "name": "MP 509 Holo Duke", "type": "sprite"},
        {"id": 526, "mp": True, "name": "MP 526 Steroids", "type": "sprite"},
        {"id": 527, "mp": True, "name": "MP 527 Atomic Health", "type": "sprite"},
        {"id": 540, "mp": True, "name": "MP 540 Atomic Health", "type": "sprite"},
        {"id": 541, "mp": True, "name": "MP 541 Atomic Health", "type": "sprite"},
        {"id": 544, "mp": True, "name": "MP 544 RPG", "type": "sprite"},
        {"id": 545, "mp": True, "name": "MP 545 Freezethrower", "type": "sprite"},
        {"id": 549, "mp": True, "name": "MP 549 Medkit", "type": "sprite"},
        {"id": 551, "mp": True, "name": "MP 551 Chaingun", "type": "sprite"},
        {"id": 567, "mp": True, "name": "MP 567 Tripbomb", "type": "sprite"},
        {"id": 568, "mp": True, "name": "MP 568 Tripbomb", "type": "sprite"},
        {
            "id": 607,
            "mp": True,
            "name": "MP 607 Night Vision Goggles",
            "type": "sprite",
        },
        {
            "id": 608,
            "mp": True,
            "name": "MP 608 Night Vision Goggles",
            "type": "sprite",
        },
        {"id": 609, "name": "609 Night Vision Goggles", "type": "sprite"},
        {"id": 610, "name": "610 Red Key Card", "type": "sprite"},
        {"id": 67, "name": "Secret 1", "type": "sector"},
        {"id": 72, "name": "Secret 2", "type": "sector"},
        {"id": 136, "name": "Secret 3", "type": "sector"},
        {"id": 145, "name": "Secret 4", "type": "sector"},
        {"id": 166, "name": "Secret 5", "type": "sector"},
        {"id": 258, "name": "Secret 6", "type": "sector"},
        {"id": 288, "name": "Secret 7", "type": "sector"},
        {"id": 309, "name": "Secret 8", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
