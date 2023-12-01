from BaseClasses import Region

from ..base_classes import D3DLevel


class E4L11(D3DLevel):
    name = "Area 51"
    levelnum = 10
    volumenum = 3
    keys = ["Red"]
    location_defs = [
        {"id": 50, "name": "50 Atomic Health", "type": "sprite"},
        {"id": 90, "name": "90 Pipebombs", "type": "sprite"},
        {"id": 94, "mp": True, "name": "MP 94 Pipebombs", "type": "sprite"},
        {"id": 109, "mp": True, "name": "MP 109 Chaingun", "type": "sprite"},
        {"id": 112, "mp": True, "name": "MP 112 Steroids", "type": "sprite"},
        {"id": 198, "name": "198 Devastator", "type": "sprite"},
        {"id": 234, "name": "234 Night Vision Goggles", "type": "sprite"},
        {"id": 252, "name": "252 Night Vision Goggles", "type": "sprite"},
        {"id": 254, "name": "254 Pipebombs", "type": "sprite"},
        {"id": 258, "name": "258 Holo Duke", "type": "sprite"},
        {"id": 275, "name": "275 Pipebombs", "type": "sprite"},
        {"id": 294, "name": "294 Tripbomb", "type": "sprite"},
        {"id": 295, "name": "295 Tripbomb", "type": "sprite"},
        {"id": 297, "name": "297 Holo Duke", "type": "sprite"},
        {"id": 298, "name": "298 Atomic Health", "type": "sprite"},
        {"id": 299, "name": "299 Steroids", "type": "sprite"},
        {"id": 300, "name": "300 Tripbomb", "type": "sprite"},
        {"id": 301, "name": "301 Medkit", "type": "sprite"},
        {"id": 302, "mp": True, "name": "MP 302 Atomic Health", "type": "sprite"},
        {"id": 304, "name": "304 Armor", "type": "sprite"},
        {"id": 306, "name": "306 Shotgun", "type": "sprite"},
        {"id": 308, "name": "308 Atomic Health", "type": "sprite"},
        {"id": 311, "name": "311 Blue Key Card", "type": "sprite"},
        {"id": 335, "name": "335 Chaingun", "type": "sprite"},
        {"id": 469, "name": "469 Red Key Card", "type": "sprite"},
        {"id": 513, "name": "513 Armor", "type": "sprite"},
        {"id": 558, "name": "558 Jetpack", "type": "sprite"},
        {"id": 560, "name": "560 Shrinker", "type": "sprite"},
        {"id": 561, "mp": True, "name": "MP 561 Jetpack", "type": "sprite"},
        {"id": 568, "name": "568 RPG", "type": "sprite"},
        {"id": 584, "name": "584 Shotgun", "type": "sprite"},
        {"id": 610, "name": "610 Medkit", "type": "sprite"},
        {"id": 637, "name": "637 Scuba Gear", "type": "sprite"},
        {"id": 656, "name": "656 Freezethrower", "type": "sprite"},
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
