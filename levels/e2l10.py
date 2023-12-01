from BaseClasses import Region

from ..base_classes import D3DLevel


class E2L10(D3DLevel):
    name = "Spin Cycle"
    levelnum = 9
    volumenum = 1
    keys = ["Red"]
    location_defs = [
        {"id": 36, "mp": True, "name": "MP 36 Shrinker", "type": "sprite"},
        {"id": 37, "mp": True, "name": "MP 37 Freezethrower", "type": "sprite"},
        {"id": 38, "mp": True, "name": "MP 38 RPG", "type": "sprite"},
        {"id": 39, "mp": True, "name": "MP 39 Chaingun", "type": "sprite"},
        {"id": 61, "mp": True, "name": "MP 61 Medkit", "type": "sprite"},
        {"id": 141, "name": "141 Holo Duke", "type": "sprite"},
        {"id": 142, "name": "142 Jetpack", "type": "sprite"},
        {"id": 143, "name": "143 Night Vision Goggles", "type": "sprite"},
        {"id": 144, "name": "144 Jetpack", "type": "sprite"},
        {"id": 162, "mp": True, "name": "MP 162 Atomic Health", "type": "sprite"},
        {"id": 179, "mp": True, "name": "MP 179 Medkit", "type": "sprite"},
        {"id": 199, "mp": True, "name": "MP 199 Atomic Health", "type": "sprite"},
        {"id": 206, "mp": True, "name": "MP 206 Shotgun", "type": "sprite"},
        {"id": 207, "mp": True, "name": "MP 207 Pipebombs", "type": "sprite"},
        {"id": 210, "mp": True, "name": "MP 210 Shotgun", "type": "sprite"},
        {"id": 211, "mp": True, "name": "MP 211 Shrinker", "type": "sprite"},
        {"id": 224, "mp": True, "name": "MP 224 Armor", "type": "sprite"},
        {
            "id": 225,
            "mp": True,
            "name": "MP 225 Night Vision Goggles",
            "type": "sprite",
        },
        {"id": 226, "mp": True, "name": "MP 226 Medkit", "type": "sprite"},
        {"id": 257, "mp": True, "name": "MP 257 Holo Duke", "type": "sprite"},
        {"id": 258, "mp": True, "name": "MP 258 Devastator", "type": "sprite"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
