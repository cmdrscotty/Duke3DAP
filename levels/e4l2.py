from BaseClasses import Region

from ..base_classes import D3DLevel


class E4L2(D3DLevel):
    name = "Duke-Burger"
    levelnum = 1
    volumenum = 3
    keys = ["Red"]
    location_defs = [
        {"id": 59, "name": "59 Tripmine", "type": "sprite"},
        {"id": 75, "name": "75 RPG", "type": "sprite"},
        {"id": 98, "name": "98 Pipebombs", "type": "sprite"},
        {"id": 101, "name": "101 Steroids", "type": "sprite"},
        {"id": 102, "name": "102 Medkit", "type": "sprite"},
        {"id": 125, "name": "125 Freezethrower", "type": "sprite"},
        {"id": 140, "name": "140 Pipebombs", "type": "sprite"},
        {"id": 150, "name": "150 Tripmine", "type": "sprite"},
        {"id": 151, "name": "151 Tripmine", "type": "sprite"},
        {"id": 198, "name": "198 Red Key Card", "type": "sprite"},
        {"id": 217, "name": "217 Armor", "type": "sprite"},
        {"id": 354, "name": "354 Armor", "type": "sprite"},
        {"id": 355, "name": "355 Medkit", "type": "sprite"},
        {"id": 413, "name": "413 Atomic Health", "type": "sprite"},
        {"id": 414, "name": "414 Pipebombs", "type": "sprite"},
        {"id": 416, "mp": True, "name": "MP 416 RPG", "type": "sprite"},
        {"id": 417, "name": "417 Shotgun", "type": "sprite"},
        {"id": 418, "name": "418 Chaingun", "type": "sprite"},
        {"id": 423, "name": "423 Steroids", "type": "sprite"},
        {"id": 563, "mp": True, "name": "MP 563 Holo Duke", "type": "sprite"},
        {"id": 595, "name": "595 Devastator", "type": "sprite"},
        {"id": 663, "name": "663 Shrinker", "type": "sprite"},
        {"id": 664, "name": "664 Blue Key Card", "type": "sprite"},
        {"id": 679, "name": "679 Night Vision Goggles", "type": "sprite"},
        {"id": 748, "name": "748 Freezethrower", "type": "sprite"},
        {"id": 102, "name": "Secret 1", "type": "sector"},
        {"id": 311, "name": "Secret 2", "type": "sector"},
        {"id": 313, "name": "Secret 3", "type": "sector"},
        {"id": 321, "name": "Secret 4", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
