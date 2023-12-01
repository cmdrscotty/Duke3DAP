from BaseClasses import Region

from ..base_classes import D3DLevel


class E2L10(D3DLevel):
    name = "Spin Cycle"
    levelnum = 9
    volumenum = 1
    keys = ["Red"]
    location_defs = [
        {"id": 36, "name": "36 Shrinker", "type": "sprite"},
        {"id": 37, "name": "37 Freezethrower", "type": "sprite"},
        {"id": 38, "name": "38 RPG", "type": "sprite"},
        {"id": 39, "name": "39 Chaingun", "type": "sprite"},
        {"id": 61, "name": "61 Medkit", "type": "sprite"},
        {"id": 141, "mp": True, "name": "MP 141 Holo Duke", "type": "sprite"},
        {"id": 142, "mp": True, "name": "MP 142 Jetpack", "type": "sprite"},
        {
            "id": 143,
            "mp": True,
            "name": "MP 143 Night Vision Goggles",
            "type": "sprite",
        },
        {"id": 144, "mp": True, "name": "MP 144 Jetpack", "type": "sprite"},
        {"id": 162, "name": "162 Atomic Health", "type": "sprite"},
        {"id": 179, "name": "179 Medkit", "type": "sprite"},
        {"id": 199, "name": "199 Atomic Health", "type": "sprite"},
        {"id": 206, "name": "206 Shotgun", "type": "sprite"},
        {"id": 207, "name": "207 Pipebombs", "type": "sprite"},
        {"id": 210, "name": "210 Shotgun", "type": "sprite"},
        {"id": 211, "name": "211 Shrinker", "type": "sprite"},
        {"id": 224, "name": "224 Armor", "type": "sprite"},
        {"id": 225, "name": "225 Night Vision Goggles", "type": "sprite"},
        {"id": 226, "name": "226 Medkit", "type": "sprite"},
        {"id": 257, "name": "257 Holo Duke", "type": "sprite"},
        {"id": 258, "name": "258 Devastator", "type": "sprite"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
