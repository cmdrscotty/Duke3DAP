from BaseClasses import Region

from ..base_classes import D3DLevel


class E3L2(D3DLevel):
    name = "Bank Roll"
    levelnum = 1
    volumenum = 2
    keys = ["Red"]
    location_defs = [
        {"id": 54, "mp": True, "name": "MP 54 Protective Boots", "type": "sprite"},
        {"id": 66, "mp": True, "name": "MP 66 Pipebombs", "type": "sprite"},
        {"id": 85, "mp": True, "name": "MP 85 Atomic Health", "type": "sprite"},
        {"id": 96, "mp": True, "name": "MP 96 Chaingun", "type": "sprite"},
        {"id": 106, "mp": True, "name": "MP 106 Pipebombs", "type": "sprite"},
        {"id": 223, "mp": True, "name": "MP 223 Holo Duke", "type": "sprite"},
        {"id": 265, "mp": True, "name": "MP 265 Medkit", "type": "sprite"},
        {"id": 354, "mp": True, "name": "MP 354 Jetpack", "type": "sprite"},
        {"id": 355, "name": "355 Red Key Card", "type": "sprite"},
        {"id": 424, "mp": True, "name": "MP 424 Shotgun", "type": "sprite"},
        {"id": 425, "mp": True, "name": "MP 425 RPG", "type": "sprite"},
        {"id": 440, "mp": True, "name": "MP 440 Blue Key Card", "type": "sprite"},
        {"id": 484, "mp": True, "name": "MP 484 Devastator", "type": "sprite"},
        {"id": 503, "mp": True, "name": "MP 503 Jetpack", "type": "sprite"},
        {"id": 506, "mp": True, "name": "MP 506 Steroids", "type": "sprite"},
        {"id": 507, "mp": True, "name": "MP 507 Freezethrower", "type": "sprite"},
        {"id": 511, "mp": True, "name": "MP 511 Shrinker", "type": "sprite"},
        {"id": 512, "mp": True, "name": "MP 512 Pipebombs", "type": "sprite"},
        {"id": 516, "mp": True, "name": "MP 516 Armor", "type": "sprite"},
        {"id": 517, "mp": True, "name": "MP 517 Atomic Health", "type": "sprite"},
        {"id": 518, "mp": True, "name": "MP 518 Tripbomb", "type": "sprite"},
        {"id": 519, "mp": True, "name": "MP 519 Tripbomb", "type": "sprite"},
        {"id": 533, "mp": True, "name": "MP 533 Medkit", "type": "sprite"},
        {"id": 537, "mp": True, "name": "MP 537 Protective Boots", "type": "sprite"},
        {"id": 539, "mp": True, "name": "MP 539 Atomic Health", "type": "sprite"},
        {"id": 17, "name": "Secret 1", "type": "sector"},
        {"id": 119, "name": "Secret 2", "type": "sector"},
        {"id": 190, "name": "Secret 3", "type": "sector"},
        {"id": 208, "name": "Secret 4", "type": "sector"},
        {"id": 235, "name": "Secret 5", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
