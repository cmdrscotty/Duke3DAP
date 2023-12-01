from BaseClasses import Region

from ..base_classes import D3DLevel


class E4L11(D3DLevel):
    name = "Area 51"
    levelnum = 10
    volumenum = 3
    keys = ["Red"]
    location_defs = [
        {"id": 50, "mp": True, "name": "MP 50 Atomic Health", "type": "sprite"},
        {"id": 90, "mp": True, "name": "MP 90 Pipebombs", "type": "sprite"},
        {"id": 94, "name": "94 Pipebombs", "type": "sprite"},
        {"id": 109, "name": "109 Chaingun", "type": "sprite"},
        {"id": 112, "name": "112 Steroids", "type": "sprite"},
        {"id": 198, "mp": True, "name": "MP 198 Devastator", "type": "sprite"},
        {
            "id": 234,
            "mp": True,
            "name": "MP 234 Night Vision Goggles",
            "type": "sprite",
        },
        {
            "id": 252,
            "mp": True,
            "name": "MP 252 Night Vision Goggles",
            "type": "sprite",
        },
        {"id": 254, "mp": True, "name": "MP 254 Pipebombs", "type": "sprite"},
        {"id": 258, "mp": True, "name": "MP 258 Holo Duke", "type": "sprite"},
        {"id": 275, "mp": True, "name": "MP 275 Pipebombs", "type": "sprite"},
        {"id": 294, "mp": True, "name": "MP 294 Tripbomb", "type": "sprite"},
        {"id": 295, "mp": True, "name": "MP 295 Tripbomb", "type": "sprite"},
        {"id": 297, "mp": True, "name": "MP 297 Holo Duke", "type": "sprite"},
        {"id": 298, "mp": True, "name": "MP 298 Atomic Health", "type": "sprite"},
        {"id": 299, "mp": True, "name": "MP 299 Steroids", "type": "sprite"},
        {"id": 300, "mp": True, "name": "MP 300 Tripbomb", "type": "sprite"},
        {"id": 301, "mp": True, "name": "MP 301 Medkit", "type": "sprite"},
        {"id": 302, "name": "302 Atomic Health", "type": "sprite"},
        {"id": 304, "mp": True, "name": "MP 304 Armor", "type": "sprite"},
        {"id": 306, "mp": True, "name": "MP 306 Shotgun", "type": "sprite"},
        {"id": 308, "mp": True, "name": "MP 308 Atomic Health", "type": "sprite"},
        {"id": 311, "mp": True, "name": "MP 311 Blue Key Card", "type": "sprite"},
        {"id": 335, "mp": True, "name": "MP 335 Chaingun", "type": "sprite"},
        {"id": 469, "name": "469 Red Key Card", "type": "sprite"},
        {"id": 513, "mp": True, "name": "MP 513 Armor", "type": "sprite"},
        {"id": 558, "mp": True, "name": "MP 558 Jetpack", "type": "sprite"},
        {"id": 560, "mp": True, "name": "MP 560 Shrinker", "type": "sprite"},
        {"id": 561, "name": "561 Jetpack", "type": "sprite"},
        {"id": 568, "mp": True, "name": "MP 568 RPG", "type": "sprite"},
        {"id": 584, "mp": True, "name": "MP 584 Shotgun", "type": "sprite"},
        {"id": 610, "mp": True, "name": "MP 610 Medkit", "type": "sprite"},
        {"id": 637, "mp": True, "name": "MP 637 Scuba Gear", "type": "sprite"},
        {"id": 656, "mp": True, "name": "MP 656 Freezethrower", "type": "sprite"},
        {"id": 690, "name": "690 Yellow Key Card", "type": "sprite"},
        {"id": 50, "name": "Secret 1", "type": "sector"},
        {"id": 54, "name": "Secret 2", "type": "sector"},
        {"id": 82, "name": "Secret 3", "type": "sector"},
        {"id": 293, "name": "Secret 4", "type": "sector"},
        {"id": 337, "name": "Secret 5", "type": "sector"},
        {"id": 440, "name": "Secret 6", "type": "sector"},
        {"id": 574, "name": "Secret 7", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
