from BaseClasses import Region

from ..base_classes import D3DLevel


class E4L4(D3DLevel):
    name = "Babe Land"
    levelnum = 3
    volumenum = 3
    keys = ["Red"]
    location_defs = [
        {"id": 6, "name": "6 RPG", "type": "sprite"},
        {"id": 9, "name": "9 Chaingun", "type": "sprite"},
        {"id": 19, "name": "19 Protective Boots", "type": "sprite"},
        {"id": 56, "name": "56 Red Key Card", "type": "sprite"},
        {"id": 101, "name": "101 Pipebombs", "type": "sprite"},
        {"id": 184, "mp": True, "name": "MP 184 Protective Boots", "type": "sprite"},
        {"id": 190, "name": "190 Pipebombs", "type": "sprite"},
        {"id": 191, "name": "191 Jetpack", "type": "sprite"},
        {"id": 200, "name": "200 Holo Duke", "type": "sprite"},
        {"id": 204, "name": "204 Night Vision Goggles", "type": "sprite"},
        {"id": 205, "name": "205 Holo Duke", "type": "sprite"},
        {"id": 210, "name": "210 Pipebombs", "type": "sprite"},
        {"id": 213, "mp": True, "name": "MP 213 Medkit", "type": "sprite"},
        {"id": 214, "name": "214 Night Vision Goggles", "type": "sprite"},
        {"id": 215, "name": "215 Armor", "type": "sprite"},
        {"id": 218, "name": "218 Steroids", "type": "sprite"},
        {"id": 220, "name": "220 Medkit", "type": "sprite"},
        {"id": 229, "name": "229 Shrinker", "type": "sprite"},
        {"id": 230, "name": "230 Freezethrower", "type": "sprite"},
        {"id": 231, "name": "231 Atomic Health", "type": "sprite"},
        {"id": 232, "name": "232 RPG", "type": "sprite"},
        {"id": 233, "name": "233 Devastator", "type": "sprite"},
        {"id": 234, "name": "234 Chaingun", "type": "sprite"},
        {"id": 235, "name": "235 Shotgun", "type": "sprite"},
        {"id": 236, "name": "236 Chaingun", "type": "sprite"},
        {"id": 238, "name": "238 RPG", "type": "sprite"},
        {"id": 245, "name": "245 Atomic Health", "type": "sprite"},
        {"id": 246, "name": "246 Shotgun", "type": "sprite"},
        {"id": 445, "name": "445 Blue Key Card", "type": "sprite"},
        {"id": 634, "name": "634 Armor", "type": "sprite"},
        {"id": 656, "name": "656 Tripmine", "type": "sprite"},
        {"id": 657, "name": "657 Tripmine", "type": "sprite"},
        {"id": 668, "name": "668 Scuba Gear", "type": "sprite"},
        {"id": 694, "name": "694 Atomic Health", "type": "sprite"},
        {"id": 755, "name": "755 Shrinker", "type": "sprite"},
        {"id": 90, "name": "Secret 1", "type": "sector"},
        {"id": 193, "name": "Secret 2", "type": "sector"},
        {"id": 200, "name": "Secret 3", "type": "sector"},
        {"id": 336, "name": "Secret 4", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
