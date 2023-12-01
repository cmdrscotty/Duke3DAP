from BaseClasses import Region

from ..base_classes import D3DLevel


class E3L10(D3DLevel):
    name = "Tier Drops"
    levelnum = 9
    volumenum = 2
    keys = ["Red"]
    location_defs = [
        {"id": 0, "mp": True, "name": "MP 0 Shotgun", "type": "sprite"},
        {"id": 3, "mp": True, "name": "MP 3 Shotgun", "type": "sprite"},
        {"id": 13, "mp": True, "name": "MP 13 Tripbomb", "type": "sprite"},
        {"id": 14, "mp": True, "name": "MP 14 Tripbomb", "type": "sprite"},
        {"id": 15, "mp": True, "name": "MP 15 Tripbomb", "type": "sprite"},
        {"id": 16, "mp": True, "name": "MP 16 Armor", "type": "sprite"},
        {"id": 17, "mp": True, "name": "MP 17 Night Vision Goggles", "type": "sprite"},
        {"id": 18, "mp": True, "name": "MP 18 Medkit", "type": "sprite"},
        {"id": 21, "mp": True, "name": "MP 21 Jetpack", "type": "sprite"},
        {"id": 30, "mp": True, "name": "MP 30 Pipebombs", "type": "sprite"},
        {"id": 31, "mp": True, "name": "MP 31 Pipebombs", "type": "sprite"},
        {"id": 38, "mp": True, "name": "MP 38 Freezethrower", "type": "sprite"},
        {"id": 209, "mp": True, "name": "MP 209 RPG", "type": "sprite"},
        {"id": 210, "mp": True, "name": "MP 210 Armor", "type": "sprite"},
        {"id": 251, "mp": True, "name": "MP 251 Chaingun", "type": "sprite"},
        {"id": 276, "mp": True, "name": "MP 276 Shrinker", "type": "sprite"},
        {"id": 282, "mp": True, "name": "MP 282 Devastator", "type": "sprite"},
        {"id": 283, "mp": True, "name": "MP 283 Steroids", "type": "sprite"},
        {"id": 290, "mp": True, "name": "MP 290 Holo Duke", "type": "sprite"},
        {"id": 314, "mp": True, "name": "MP 314 Atomic Health", "type": "sprite"},
        {"id": 315, "mp": True, "name": "MP 315 Atomic Health", "type": "sprite"},
        {"id": 316, "mp": True, "name": "MP 316 Atomic Health", "type": "sprite"},
        {"id": 148, "name": "Secret 1", "type": "sector"},
        {"id": 156, "name": "Secret 2", "type": "sector"},
        {"id": 164, "name": "Secret 3", "type": "sector"},
        {"id": 172, "name": "Secret 4", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
