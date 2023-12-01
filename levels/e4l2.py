from BaseClasses import Region

from ..base_classes import D3DLevel


class E4L2(D3DLevel):
    name = "Duke-Burger"
    levelnum = 1
    volumenum = 3
    keys = ["Red"]
    location_defs = [
        {"id": 59, "mp": True, "name": "MP 59 Tripbomb", "type": "sprite"},
        {"id": 75, "mp": True, "name": "MP 75 RPG", "type": "sprite"},
        {"id": 98, "mp": True, "name": "MP 98 Pipebombs", "type": "sprite"},
        {"id": 101, "mp": True, "name": "MP 101 Steroids", "type": "sprite"},
        {"id": 102, "mp": True, "name": "MP 102 Medkit", "type": "sprite"},
        {"id": 125, "mp": True, "name": "MP 125 Freezethrower", "type": "sprite"},
        {"id": 140, "mp": True, "name": "MP 140 Pipebombs", "type": "sprite"},
        {"id": 150, "mp": True, "name": "MP 150 Tripbomb", "type": "sprite"},
        {"id": 151, "mp": True, "name": "MP 151 Tripbomb", "type": "sprite"},
        {"id": 198, "name": "198 Red Key Card", "type": "sprite"},
        {"id": 217, "mp": True, "name": "MP 217 Armor", "type": "sprite"},
        {"id": 354, "mp": True, "name": "MP 354 Armor", "type": "sprite"},
        {"id": 355, "mp": True, "name": "MP 355 Medkit", "type": "sprite"},
        {"id": 413, "mp": True, "name": "MP 413 Atomic Health", "type": "sprite"},
        {"id": 414, "mp": True, "name": "MP 414 Pipebombs", "type": "sprite"},
        {"id": 416, "name": "416 RPG", "type": "sprite"},
        {"id": 417, "mp": True, "name": "MP 417 Shotgun", "type": "sprite"},
        {"id": 418, "mp": True, "name": "MP 418 Chaingun", "type": "sprite"},
        {"id": 423, "mp": True, "name": "MP 423 Steroids", "type": "sprite"},
        {"id": 563, "name": "563 Holo Duke", "type": "sprite"},
        {"id": 595, "mp": True, "name": "MP 595 Devastator", "type": "sprite"},
        {"id": 663, "mp": True, "name": "MP 663 Shrinker", "type": "sprite"},
        {"id": 664, "mp": True, "name": "MP 664 Blue Key Card", "type": "sprite"},
        {
            "id": 679,
            "mp": True,
            "name": "MP 679 Night Vision Goggles",
            "type": "sprite",
        },
        {"id": 748, "mp": True, "name": "MP 748 Freezethrower", "type": "sprite"},
        {"id": 102, "name": "Secret 1", "type": "sector"},
        {"id": 311, "name": "Secret 2", "type": "sector"},
        {"id": 313, "name": "Secret 3", "type": "sector"},
        {"id": 321, "name": "Secret 4", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
