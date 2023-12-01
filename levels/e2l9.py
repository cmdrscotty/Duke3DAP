from BaseClasses import Region

from ..base_classes import D3DLevel


class E2L9(D3DLevel):
    name = "Overlord"
    levelnum = 8
    volumenum = 1
    keys = ["Red"]
    location_defs = [
        {"id": 7, "mp": True, "name": "MP 7 RPG", "type": "sprite"},
        {"id": 8, "mp": True, "name": "MP 8 Armor", "type": "sprite"},
        {"id": 9, "mp": True, "name": "MP 9 Armor", "type": "sprite"},
        {"id": 10, "mp": True, "name": "MP 10 Pipebombs", "type": "sprite"},
        {"id": 12, "mp": True, "name": "MP 12 Medkit", "type": "sprite"},
        {"id": 13, "mp": True, "name": "MP 13 Medkit", "type": "sprite"},
        {"id": 14, "mp": True, "name": "MP 14 Night Vision Goggles", "type": "sprite"},
        {"id": 15, "mp": True, "name": "MP 15 Scuba Gear", "type": "sprite"},
        {"id": 16, "mp": True, "name": "MP 16 Atomic Health", "type": "sprite"},
        {"id": 39, "mp": True, "name": "MP 39 Armor", "type": "sprite"},
        {"id": 69, "mp": True, "name": "MP 69 Tripbomb", "type": "sprite"},
        {"id": 70, "mp": True, "name": "MP 70 Tripbomb", "type": "sprite"},
        {"id": 71, "mp": True, "name": "MP 71 Tripbomb", "type": "sprite"},
        {"id": 73, "mp": True, "name": "MP 73 Atomic Health", "type": "sprite"},
        {"id": 78, "mp": True, "name": "MP 78 Scuba Gear", "type": "sprite"},
        {"id": 81, "mp": True, "name": "MP 81 Night Vision Goggles", "type": "sprite"},
        {"id": 83, "mp": True, "name": "MP 83 Chaingun", "type": "sprite"},
        {"id": 84, "mp": True, "name": "MP 84 Atomic Health", "type": "sprite"},
        {"id": 86, "mp": True, "name": "MP 86 Atomic Health", "type": "sprite"},
        {"id": 93, "mp": True, "name": "MP 93 Shrinker", "type": "sprite"},
        {"id": 94, "mp": True, "name": "MP 94 Devastator", "type": "sprite"},
        {"id": 96, "mp": True, "name": "MP 96 RPG", "type": "sprite"},
        {"id": 100, "mp": True, "name": "MP 100 Freezethrower", "type": "sprite"},
        {"id": 102, "mp": True, "name": "MP 102 Shotgun", "type": "sprite"},
        {"id": 104, "mp": True, "name": "MP 104 Atomic Health", "type": "sprite"},
        {"id": 159, "mp": True, "name": "MP 159 Pipebombs", "type": "sprite"},
        {"id": 395, "mp": True, "name": "MP 395 Holo Duke", "type": "sprite"},
        {"id": 396, "mp": True, "name": "MP 396 Jetpack", "type": "sprite"},
        {"id": 413, "mp": True, "name": "MP 413 Medkit", "type": "sprite"},
        {"id": 415, "mp": True, "name": "MP 415 Atomic Health", "type": "sprite"},
        {"id": 424, "mp": True, "name": "MP 424 Pipebombs", "type": "sprite"},
        {"id": 425, "mp": True, "name": "MP 425 Pipebombs", "type": "sprite"},
        {"id": 203, "name": "Secret 1", "type": "sector"},
        {"id": 219, "name": "Secret 2", "type": "sector"},
        {"id": 225, "name": "Secret 3", "type": "sector"},
        {"id": 246, "name": "Secret 4", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
