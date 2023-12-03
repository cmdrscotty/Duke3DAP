from BaseClasses import Region

from ..base_classes import D3DLevel


class E4L3(D3DLevel):
    name = "Shop-N-Bag"
    levelnum = 2
    volumenum = 3
    keys = ["Red"]
    location_defs = [
        {"id": 18, "mp": True, "name": "MP 18 Chaingun", "type": "sprite"},
        {"id": 21, "name": "21 Pipebombs", "type": "sprite"},
        {"id": 32, "name": "32 Armor", "type": "sprite"},
        {"id": 39, "name": "39 Freezethrower", "type": "sprite"},
        {"id": 40, "name": "40 Pipebombs", "type": "sprite"},
        {"id": 41, "name": "41 Night Vision Goggles", "type": "sprite"},
        {"id": 116, "mp": True, "name": "MP 116 Shrinker", "type": "sprite"},
        {"id": 121, "name": "121 RPG", "type": "sprite"},
        {"id": 122, "mp": True, "name": "MP 122 Shotgun", "type": "sprite"},
        {"id": 126, "mp": True, "name": "MP 126 RPG", "type": "sprite"},
        {"id": 130, "name": "130 Devastator", "type": "sprite"},
        {"id": 131, "name": "131 Tripmine", "type": "sprite"},
        {"id": 132, "name": "132 Tripmine", "type": "sprite"},
        {"id": 133, "name": "133 Tripmine", "type": "sprite"},
        {"id": 134, "name": "134 Atomic Health", "type": "sprite"},
        {"id": 139, "name": "139 Medkit", "type": "sprite"},
        {"id": 148, "name": "148 Shotgun", "type": "sprite"},
        {"id": 158, "name": "158 Devastator", "type": "sprite"},
        {"id": 194, "name": "194 Atomic Health", "type": "sprite"},
        {"id": 228, "name": "228 Chaingun", "type": "sprite"},
        {"id": 264, "name": "264 Atomic Health", "type": "sprite"},
        {"id": 307, "name": "307 Blue Key Card", "type": "sprite"},
        {"id": 377, "name": "377 Yellow Key Card", "type": "sprite"},
        {"id": 396, "name": "396 Red Key Card", "type": "sprite"},
        {"id": 426, "name": "426 Pipebombs", "type": "sprite"},
        {"id": 442, "name": "442 Armor", "type": "sprite"},
        {"id": 445, "name": "445 Night Vision Goggles", "type": "sprite"},
        {"id": 446, "mp": True, "name": "MP 446 Jetpack", "type": "sprite"},
        {"id": 451, "mp": True, "name": "MP 451 Shotgun", "type": "sprite"},
        {"id": 452, "name": "452 Holo Duke", "type": "sprite"},
        {"id": 492, "name": "492 Steroids", "type": "sprite"},
        {"id": 542, "name": "542 Medkit", "type": "sprite"},
        {"id": 547, "name": "547 Steroids", "type": "sprite"},
        {"id": 549, "name": "549 Protective Boots", "type": "sprite"},
        {"id": 70, "name": "Secret 1", "type": "sector"},
        {"id": 176, "name": "Secret 2", "type": "sector"},
        {"id": 274, "name": "Secret 3", "type": "sector"},
        {"id": 344, "name": "Secret 4", "type": "sector"},
        {"id": 349, "name": "Secret 5", "type": "sector"},
        {"id": 362, "name": "Secret 6", "type": "sector"},
        {"id": 365, "name": "Secret 7", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
