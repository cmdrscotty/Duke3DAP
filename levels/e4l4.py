from BaseClasses import Region

from ..base_classes import D3DLevel


class E4L4(D3DLevel):
    name = "Babe Land"
    levelnum = 3
    volumenum = 3
    keys = ["Red"]
    location_defs = [
        {"id": 6, "mp": True, "name": "MP 6 RPG", "type": "sprite"},
        {"id": 9, "mp": True, "name": "MP 9 Chaingun", "type": "sprite"},
        {"id": 19, "mp": True, "name": "MP 19 Protective Boots", "type": "sprite"},
        {"id": 56, "name": "56 Red Key Card", "type": "sprite"},
        {"id": 101, "mp": True, "name": "MP 101 Pipebombs", "type": "sprite"},
        {"id": 184, "name": "184 Protective Boots", "type": "sprite"},
        {"id": 190, "mp": True, "name": "MP 190 Pipebombs", "type": "sprite"},
        {"id": 191, "mp": True, "name": "MP 191 Jetpack", "type": "sprite"},
        {"id": 200, "mp": True, "name": "MP 200 Holo Duke", "type": "sprite"},
        {
            "id": 204,
            "mp": True,
            "name": "MP 204 Night Vision Goggles",
            "type": "sprite",
        },
        {"id": 205, "mp": True, "name": "MP 205 Holo Duke", "type": "sprite"},
        {"id": 210, "mp": True, "name": "MP 210 Pipebombs", "type": "sprite"},
        {"id": 213, "name": "213 Medkit", "type": "sprite"},
        {
            "id": 214,
            "mp": True,
            "name": "MP 214 Night Vision Goggles",
            "type": "sprite",
        },
        {"id": 215, "mp": True, "name": "MP 215 Armor", "type": "sprite"},
        {"id": 218, "mp": True, "name": "MP 218 Steroids", "type": "sprite"},
        {"id": 220, "mp": True, "name": "MP 220 Medkit", "type": "sprite"},
        {"id": 229, "mp": True, "name": "MP 229 Shrinker", "type": "sprite"},
        {"id": 230, "mp": True, "name": "MP 230 Freezethrower", "type": "sprite"},
        {"id": 231, "mp": True, "name": "MP 231 Atomic Health", "type": "sprite"},
        {"id": 232, "mp": True, "name": "MP 232 RPG", "type": "sprite"},
        {"id": 233, "mp": True, "name": "MP 233 Devastator", "type": "sprite"},
        {"id": 234, "mp": True, "name": "MP 234 Chaingun", "type": "sprite"},
        {"id": 235, "mp": True, "name": "MP 235 Shotgun", "type": "sprite"},
        {"id": 236, "mp": True, "name": "MP 236 Chaingun", "type": "sprite"},
        {"id": 238, "mp": True, "name": "MP 238 RPG", "type": "sprite"},
        {"id": 245, "mp": True, "name": "MP 245 Atomic Health", "type": "sprite"},
        {"id": 246, "mp": True, "name": "MP 246 Shotgun", "type": "sprite"},
        {"id": 445, "mp": True, "name": "MP 445 Blue Key Card", "type": "sprite"},
        {"id": 634, "mp": True, "name": "MP 634 Armor", "type": "sprite"},
        {"id": 656, "mp": True, "name": "MP 656 Tripbomb", "type": "sprite"},
        {"id": 657, "mp": True, "name": "MP 657 Tripbomb", "type": "sprite"},
        {"id": 668, "mp": True, "name": "MP 668 Scuba Gear", "type": "sprite"},
        {"id": 694, "mp": True, "name": "MP 694 Atomic Health", "type": "sprite"},
        {"id": 755, "mp": True, "name": "MP 755 Shrinker", "type": "sprite"},
        {"id": 90, "name": "Secret 1", "type": "sector"},
        {"id": 193, "name": "Secret 2", "type": "sector"},
        {"id": 200, "name": "Secret 3", "type": "sector"},
        {"id": 336, "name": "Secret 4", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
