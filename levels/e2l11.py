from BaseClasses import Region

from ..base_classes import D3DLevel


class E2L11(D3DLevel):
    name = "Lunatic Fringe"
    levelnum = 1
    volumenum = 10
    keys = ["Red"]
    location_defs = [
        {"id": 28, "mp": True, "name": "MP 28 Shrinker", "type": "sprite"},
        {"id": 58, "mp": True, "name": "MP 58 Devastator", "type": "sprite"},
        {"id": 63, "name": "63 Night Vision Goggles", "type": "sprite"},
        {"id": 92, "mp": True, "name": "MP 92 Holo Duke", "type": "sprite"},
        {"id": 93, "mp": True, "name": "MP 93 RPG", "type": "sprite"},
        {"id": 96, "mp": True, "name": "MP 96 Armor", "type": "sprite"},
        {"id": 99, "name": "99 Jetpack", "type": "sprite"},
        {"id": 102, "mp": True, "name": "MP 102 Atomic Health", "type": "sprite"},
        {"id": 104, "mp": True, "name": "MP 104 Pipebombs", "type": "sprite"},
        {"id": 109, "mp": True, "name": "MP 109 Steroids", "type": "sprite"},
        {"id": 111, "mp": True, "name": "MP 111 Tripbomb", "type": "sprite"},
        {"id": 112, "mp": True, "name": "MP 112 Medkit", "type": "sprite"},
        {"id": 113, "name": "113 Shrinker", "type": "sprite"},
        {"id": 115, "mp": True, "name": "MP 115 Chaingun", "type": "sprite"},
        {"id": 123, "mp": True, "name": "MP 123 Shotgun", "type": "sprite"},
        {"id": 124, "mp": True, "name": "MP 124 Freezethrower", "type": "sprite"},
        {"id": 125, "mp": True, "name": "MP 125 Shotgun", "type": "sprite"},
        {"id": 127, "mp": True, "name": "MP 127 Pipebombs", "type": "sprite"},
        {"id": 180, "mp": True, "name": "MP 180 Atomic Health", "type": "sprite"},
        {"id": 181, "mp": True, "name": "MP 181 Atomic Health", "type": "sprite"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
