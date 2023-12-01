from BaseClasses import Region

from ..base_classes import D3DLevel


class E4L3(D3DLevel):
    name = "Shop-N-Bag"
    levelnum = 2
    volumenum = 3
    keys = ["Red"]
    location_defs = [
        {"id": 18, "name": "18 Chaingun", "type": "sprite"},
        {"id": 21, "mp": True, "name": "MP 21 Pipebombs", "type": "sprite"},
        {"id": 32, "mp": True, "name": "MP 32 Armor", "type": "sprite"},
        {"id": 39, "mp": True, "name": "MP 39 Freezethrower", "type": "sprite"},
        {"id": 40, "mp": True, "name": "MP 40 Pipebombs", "type": "sprite"},
        {"id": 41, "mp": True, "name": "MP 41 Night Vision Goggles", "type": "sprite"},
        {"id": 116, "name": "116 Shrinker", "type": "sprite"},
        {"id": 121, "mp": True, "name": "MP 121 RPG", "type": "sprite"},
        {"id": 122, "name": "122 Shotgun", "type": "sprite"},
        {"id": 126, "name": "126 RPG", "type": "sprite"},
        {"id": 130, "mp": True, "name": "MP 130 Devastator", "type": "sprite"},
        {"id": 131, "mp": True, "name": "MP 131 Tripbomb", "type": "sprite"},
        {"id": 132, "mp": True, "name": "MP 132 Tripbomb", "type": "sprite"},
        {"id": 133, "mp": True, "name": "MP 133 Tripbomb", "type": "sprite"},
        {"id": 134, "mp": True, "name": "MP 134 Atomic Health", "type": "sprite"},
        {"id": 139, "mp": True, "name": "MP 139 Medkit", "type": "sprite"},
        {"id": 148, "mp": True, "name": "MP 148 Shotgun", "type": "sprite"},
        {"id": 158, "mp": True, "name": "MP 158 Devastator", "type": "sprite"},
        {"id": 194, "mp": True, "name": "MP 194 Atomic Health", "type": "sprite"},
        {"id": 228, "mp": True, "name": "MP 228 Chaingun", "type": "sprite"},
        {"id": 264, "mp": True, "name": "MP 264 Atomic Health", "type": "sprite"},
        {"id": 307, "mp": True, "name": "MP 307 Blue Key Card", "type": "sprite"},
        {"id": 377, "name": "377 Yellow Key Card", "type": "sprite"},
        {"id": 396, "name": "396 Red Key Card", "type": "sprite"},
        {"id": 426, "mp": True, "name": "MP 426 Pipebombs", "type": "sprite"},
        {"id": 442, "mp": True, "name": "MP 442 Armor", "type": "sprite"},
        {
            "id": 445,
            "mp": True,
            "name": "MP 445 Night Vision Goggles",
            "type": "sprite",
        },
        {"id": 446, "name": "446 Jetpack", "type": "sprite"},
        {"id": 451, "name": "451 Shotgun", "type": "sprite"},
        {"id": 452, "mp": True, "name": "MP 452 Holo Duke", "type": "sprite"},
        {"id": 492, "mp": True, "name": "MP 492 Steroids", "type": "sprite"},
        {"id": 542, "mp": True, "name": "MP 542 Medkit", "type": "sprite"},
        {"id": 547, "mp": True, "name": "MP 547 Steroids", "type": "sprite"},
        {"id": 549, "mp": True, "name": "MP 549 Protective Boots", "type": "sprite"},
        {"id": 70, "name": "Secret 1", "type": "sector"},
        {"id": 176, "name": "Secret 2", "type": "sector"},
        {"id": 274, "name": "Secret 3", "type": "sector"},
        {"id": 344, "name": "Secret 4", "type": "sector"},
        {"id": 349, "name": "Secret 5", "type": "sector"},
        {"id": 362, "name": "Secret 6", "type": "sector"},
        {"id": 365, "name": "Secret 7", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
