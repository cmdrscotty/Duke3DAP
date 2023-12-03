from BaseClasses import Region

from ..base_classes import D3DLevel


class E2L6(D3DLevel):
    name = "Tiberius Station"
    levelnum = 5
    volumenum = 1
    keys = ["Red"]
    location_defs = [
        {"id": 32, "name": "32 RPG", "type": "sprite"},
        {"id": 42, "name": "42 Protective Boots", "type": "sprite"},
        {"id": 43, "name": "43 Scuba Gear", "type": "sprite"},
        {"id": 45, "name": "45 Night Vision Goggles", "type": "sprite"},
        {"id": 46, "name": "46 Medkit", "type": "sprite"},
        {"id": 115, "name": "115 Jetpack", "type": "sprite"},
        {"id": 181, "name": "181 Medkit", "type": "sprite"},
        {"id": 346, "name": "346 Armor", "type": "sprite"},
        {"id": 347, "name": "347 Armor", "type": "sprite"},
        {"id": 348, "name": "348 Blue Key Card", "type": "sprite"},
        {"id": 430, "name": "430 Pipebombs", "type": "sprite"},
        {"id": 431, "name": "431 Pipebombs", "type": "sprite"},
        {"id": 490, "name": "490 Shrinker", "type": "sprite"},
        {"id": 507, "name": "507 Devastator", "type": "sprite"},
        {"id": 508, "name": "508 Shotgun", "type": "sprite"},
        {"id": 509, "name": "509 Holo Duke", "type": "sprite"},
        {"id": 526, "name": "526 Steroids", "type": "sprite"},
        {"id": 527, "name": "527 Atomic Health", "type": "sprite"},
        {"id": 540, "name": "540 Atomic Health", "type": "sprite"},
        {"id": 541, "name": "541 Atomic Health", "type": "sprite"},
        {"id": 544, "name": "544 RPG", "type": "sprite"},
        {"id": 545, "name": "545 Freezethrower", "type": "sprite"},
        {"id": 549, "name": "549 Medkit", "type": "sprite"},
        {"id": 551, "name": "551 Chaingun", "type": "sprite"},
        {"id": 567, "name": "567 Tripmine", "type": "sprite"},
        {"id": 568, "name": "568 Tripmine", "type": "sprite"},
        {"id": 607, "name": "607 Night Vision Goggles", "type": "sprite"},
        {"id": 608, "name": "608 Night Vision Goggles", "type": "sprite"},
        {
            "id": 609,
            "mp": True,
            "name": "MP 609 Night Vision Goggles",
            "type": "sprite",
        },
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
