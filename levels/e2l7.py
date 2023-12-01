from BaseClasses import Region

from ..base_classes import D3DLevel


class E2L7(D3DLevel):
    name = "Lunar Reactor"
    levelnum = 1
    volumenum = 6
    keys = ["Red"]
    location_defs = [
        {"id": 5, "mp": True, "name": "MP 5 Steroids", "type": "sprite"},
        {"id": 39, "mp": True, "name": "MP 39 Night Vision Goggles", "type": "sprite"},
        {"id": 50, "mp": True, "name": "MP 50 Atomic Health", "type": "sprite"},
        {"id": 51, "mp": True, "name": "MP 51 Atomic Health", "type": "sprite"},
        {"id": 77, "mp": True, "name": "MP 77 RPG", "type": "sprite"},
        {"id": 78, "mp": True, "name": "MP 78 Shotgun", "type": "sprite"},
        {"id": 109, "mp": True, "name": "MP 109 Armor", "type": "sprite"},
        {"id": 111, "mp": True, "name": "MP 111 Atomic Health", "type": "sprite"},
        {"id": 120, "mp": True, "name": "MP 120 Tripbomb", "type": "sprite"},
        {"id": 128, "mp": True, "name": "MP 128 Jetpack", "type": "sprite"},
        {"id": 129, "mp": True, "name": "MP 129 Pipebombs", "type": "sprite"},
        {"id": 132, "mp": True, "name": "MP 132 Holo Duke", "type": "sprite"},
        {"id": 142, "mp": True, "name": "MP 142 Freezethrower", "type": "sprite"},
        {"id": 147, "mp": True, "name": "MP 147 Shrinker", "type": "sprite"},
        {"id": 148, "mp": True, "name": "MP 148 Tripbomb", "type": "sprite"},
        {"id": 149, "mp": True, "name": "MP 149 Armor", "type": "sprite"},
        {"id": 154, "mp": True, "name": "MP 154 Pipebombs", "type": "sprite"},
        {"id": 158, "mp": True, "name": "MP 158 Atomic Health", "type": "sprite"},
        {"id": 160, "mp": True, "name": "MP 160 Chaingun", "type": "sprite"},
        {"id": 164, "mp": True, "name": "MP 164 Atomic Health", "type": "sprite"},
        {"id": 165, "mp": True, "name": "MP 165 Medkit", "type": "sprite"},
        {"id": 175, "mp": True, "name": "MP 175 Devastator", "type": "sprite"},
        {"id": 213, "mp": True, "name": "MP 213 RPG", "type": "sprite"},
        {"id": 882, "name": "882 Red Key Card", "type": "sprite"},
        {"id": 883, "mp": True, "name": "MP 883 Blue Key Card", "type": "sprite"},
        {"id": 954, "mp": True, "name": "MP 954 Shotgun", "type": "sprite"},
        {"id": 983, "name": "983 Yellow Key Card", "type": "sprite"},
        {
            "id": 992,
            "mp": True,
            "name": "MP 992 Night Vision Goggles",
            "type": "sprite",
        },
        {"id": 994, "mp": True, "name": "MP 994 Tripbomb", "type": "sprite"},
        {"id": 995, "mp": True, "name": "MP 995 Tripbomb", "type": "sprite"},
        {
            "id": 1028,
            "mp": True,
            "name": "MP 1028 Night Vision Goggles",
            "type": "sprite",
        },
        {"id": 1029, "mp": True, "name": "MP 1029 Tripbomb", "type": "sprite"},
        {"id": 1030, "mp": True, "name": "MP 1030 Tripbomb", "type": "sprite"},
        {"id": 1040, "mp": True, "name": "MP 1040 Protective Boots", "type": "sprite"},
        {"id": 1042, "mp": True, "name": "MP 1042 Atomic Health", "type": "sprite"},
        {"id": 181, "name": "Secret 1", "type": "sector"},
        {"id": 206, "name": "Secret 2", "type": "sector"},
        {"id": 330, "name": "Secret 3", "type": "sector"},
        {"id": 387, "name": "Secret 4", "type": "sector"},
        {"id": 390, "name": "Secret 5", "type": "sector"},
        {"id": 395, "name": "Secret 6", "type": "sector"},
        {"id": 396, "name": "Secret 7", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
