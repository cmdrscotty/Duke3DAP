from BaseClasses import Region

from ..base_classes import D3DLevel


class E4L8(D3DLevel):
    name = "Critical Mass"
    levelnum = 7
    volumenum = 3
    keys = ["Red"]
    location_defs = [
        {
            "id": 313,
            "mp": True,
            "name": "MP 313 Night Vision Goggles",
            "type": "sprite",
        },
        {"id": 323, "name": "323 Jetpack", "type": "sprite"},
        {"id": 344, "mp": True, "name": "MP 344 Freezethrower", "type": "sprite"},
        {"id": 351, "mp": True, "name": "MP 351 Armor", "type": "sprite"},
        {"id": 352, "mp": True, "name": "MP 352 Shotgun", "type": "sprite"},
        {"id": 386, "mp": True, "name": "MP 386 Blue Key Card", "type": "sprite"},
        {"id": 456, "mp": True, "name": "MP 456 Atomic Health", "type": "sprite"},
        {"id": 479, "mp": True, "name": "MP 479 Medkit", "type": "sprite"},
        {"id": 532, "mp": True, "name": "MP 532 Devastator", "type": "sprite"},
        {"id": 533, "mp": True, "name": "MP 533 Atomic Health", "type": "sprite"},
        {"id": 538, "mp": True, "name": "MP 538 Pipebombs", "type": "sprite"},
        {"id": 613, "mp": True, "name": "MP 613 Armor", "type": "sprite"},
        {"id": 614, "mp": True, "name": "MP 614 Atomic Health", "type": "sprite"},
        {"id": 648, "mp": True, "name": "MP 648 Chaingun", "type": "sprite"},
        {"id": 713, "mp": True, "name": "MP 713 Pipebombs", "type": "sprite"},
        {"id": 714, "mp": True, "name": "MP 714 Shotgun", "type": "sprite"},
        {"id": 724, "mp": True, "name": "MP 724 Holo Duke", "type": "sprite"},
        {"id": 733, "mp": True, "name": "MP 733 Medkit", "type": "sprite"},
        {"id": 734, "mp": True, "name": "MP 734 Steroids", "type": "sprite"},
        {"id": 735, "mp": True, "name": "MP 735 Protective Boots", "type": "sprite"},
        {"id": 761, "mp": True, "name": "MP 761 Atomic Health", "type": "sprite"},
        {"id": 762, "name": "762 Yellow Key Card", "type": "sprite"},
        {"id": 827, "mp": True, "name": "MP 827 Shrinker", "type": "sprite"},
        {"id": 830, "mp": True, "name": "MP 830 Chaingun", "type": "sprite"},
        {"id": 834, "mp": True, "name": "MP 834 RPG", "type": "sprite"},
        {"id": 835, "mp": True, "name": "MP 835 Tripbomb", "type": "sprite"},
        {"id": 836, "mp": True, "name": "MP 836 Tripbomb", "type": "sprite"},
        {"id": 854, "name": "854 Red Key Card", "type": "sprite"},
        {"id": 863, "mp": True, "name": "MP 863 Scuba Gear", "type": "sprite"},
        {"id": 864, "name": "864 RPG", "type": "sprite"},
        {"id": 868, "name": "868 Freezethrower", "type": "sprite"},
        {"id": 105, "name": "Secret 1", "type": "sector"},
        {"id": 116, "name": "Secret 2", "type": "sector"},
        {"id": 234, "name": "Secret 3", "type": "sector"},
        {"id": 240, "name": "Secret 4", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
