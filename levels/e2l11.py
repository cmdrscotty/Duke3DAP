from BaseClasses import Region

from ..base_classes import D3DLevel


class E2L11(D3DLevel):
    name = "Lunatic Fringe"
    levelnum = 10
    volumenum = 1
    keys = ["Red"]
    location_defs = [
        {"id": 28, "name": "28 Shrinker", "type": "sprite"},
        {"id": 58, "name": "58 Devastator", "type": "sprite"},
        {"id": 63, "mp": True, "name": "MP 63 Night Vision Goggles", "type": "sprite"},
        {"id": 92, "name": "92 Holo Duke", "type": "sprite"},
        {"id": 93, "name": "93 RPG", "type": "sprite"},
        {"id": 96, "name": "96 Armor", "type": "sprite"},
        {"id": 99, "mp": True, "name": "MP 99 Jetpack", "type": "sprite"},
        {"id": 102, "name": "102 Atomic Health", "type": "sprite"},
        {"id": 104, "name": "104 Pipebombs", "type": "sprite"},
        {"id": 109, "name": "109 Steroids", "type": "sprite"},
        {"id": 111, "name": "111 Tripmine", "type": "sprite"},
        {"id": 112, "name": "112 Medkit", "type": "sprite"},
        {"id": 113, "mp": True, "name": "MP 113 Shrinker", "type": "sprite"},
        {"id": 115, "name": "115 Chaingun", "type": "sprite"},
        {"id": 123, "name": "123 Shotgun", "type": "sprite"},
        {"id": 124, "name": "124 Freezethrower", "type": "sprite"},
        {"id": 125, "name": "125 Shotgun", "type": "sprite"},
        {"id": 127, "name": "127 Pipebombs", "type": "sprite"},
        {"id": 180, "name": "180 Atomic Health", "type": "sprite"},
        {"id": 181, "name": "181 Atomic Health", "type": "sprite"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
