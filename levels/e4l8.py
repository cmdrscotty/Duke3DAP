from BaseClasses import Region

from ..base_classes import D3DLevel


class E4L8(D3DLevel):
    name = "Critical Mass"
    levelnum = 7
    volumenum = 3
    keys = ["Red", "Blue", "Yellow"]
    location_defs = [
        {"id": 313, "name": "313 Night Vision Goggles", "type": "sprite"},
        {"id": 323, "mp": True, "name": "MP 323 Jetpack", "type": "sprite"},
        {"id": 344, "name": "344 Freezethrower", "type": "sprite"},
        {"id": 351, "name": "351 Armor", "type": "sprite"},
        {"id": 352, "name": "352 Shotgun", "type": "sprite"},
        {"id": 386, "name": "386 Blue Key Card", "type": "sprite"},
        {"id": 456, "name": "456 Atomic Health", "type": "sprite"},
        {"id": 479, "name": "479 Medkit", "type": "sprite"},
        {"id": 532, "name": "532 Devastator", "type": "sprite"},
        {"id": 533, "name": "533 Atomic Health", "type": "sprite"},
        {"id": 538, "name": "538 Pipebombs", "type": "sprite"},
        {"id": 613, "name": "613 Armor", "type": "sprite"},
        {"id": 614, "name": "614 Atomic Health", "type": "sprite"},
        {"id": 648, "name": "648 Chaingun", "type": "sprite"},
        {"id": 713, "name": "713 Pipebombs", "type": "sprite"},
        {"id": 714, "name": "714 Shotgun", "type": "sprite"},
        {"id": 724, "name": "724 Holo Duke", "type": "sprite"},
        {"id": 733, "name": "733 Medkit", "type": "sprite"},
        {"id": 734, "name": "734 Steroids", "type": "sprite"},
        {"id": 735, "name": "735 Protective Boots", "type": "sprite"},
        {"id": 761, "name": "761 Atomic Health", "type": "sprite"},
        {"id": 762, "name": "762 Yellow Key Card", "type": "sprite"},
        {"id": 827, "name": "827 Shrinker", "type": "sprite"},
        {"id": 830, "name": "830 Chaingun", "type": "sprite"},
        {"id": 834, "name": "834 RPG", "type": "sprite"},
        {"id": 835, "name": "835 Tripbomb", "type": "sprite"},
        {"id": 836, "name": "836 Tripbomb", "type": "sprite"},
        {"id": 854, "name": "854 Red Key Card", "type": "sprite"},
        {"id": 863, "name": "863 Scuba Gear", "type": "sprite"},
        {"id": 864, "mp": True, "name": "MP 864 RPG", "type": "sprite"},
        {"id": 868, "mp": True, "name": "MP 868 Freezethrower", "type": "sprite"},
        {"id": 105, "name": "Secret 1", "type": "sector"},
        {"id": 116, "name": "Secret 2", "type": "sector"},
        {"id": 234, "name": "Secret 3", "type": "sector"},
        {"id": 240, "name": "Secret 4", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
