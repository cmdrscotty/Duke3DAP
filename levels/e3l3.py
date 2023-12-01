from BaseClasses import Region

from ..base_classes import D3DLevel


class E3L3(D3DLevel):
    name = "Flood Zone"
    levelnum = 2
    volumenum = 2
    keys = ["Red"]
    location_defs = [
        {"id": 1, "name": "1 Jetpack", "type": "sprite"},
        {"id": 23, "mp": True, "name": "MP 23 Night Vision Goggles", "type": "sprite"},
        {"id": 24, "mp": True, "name": "MP 24 Night Vision Goggles", "type": "sprite"},
        {"id": 42, "name": "42 Jetpack", "type": "sprite"},
        {"id": 50, "mp": True, "name": "MP 50 Jetpack", "type": "sprite"},
        {"id": 63, "name": "63 Jetpack", "type": "sprite"},
        {"id": 70, "mp": True, "name": "MP 70 Freezethrower", "type": "sprite"},
        {"id": 71, "mp": True, "name": "MP 71 Tripbomb", "type": "sprite"},
        {"id": 72, "mp": True, "name": "MP 72 Tripbomb", "type": "sprite"},
        {"id": 73, "mp": True, "name": "MP 73 Shrinker", "type": "sprite"},
        {"id": 95, "mp": True, "name": "MP 95 Holo Duke", "type": "sprite"},
        {"id": 96, "name": "96 Chaingun", "type": "sprite"},
        {"id": 97, "name": "97 Devastator", "type": "sprite"},
        {"id": 98, "name": "98 Shotgun", "type": "sprite"},
        {"id": 114, "mp": True, "name": "MP 114 Atomic Health", "type": "sprite"},
        {"id": 168, "mp": True, "name": "MP 168 Chaingun", "type": "sprite"},
        {"id": 171, "mp": True, "name": "MP 171 Blue Key Card", "type": "sprite"},
        {"id": 172, "mp": True, "name": "MP 172 Atomic Health", "type": "sprite"},
        {"id": 174, "mp": True, "name": "MP 174 Armor", "type": "sprite"},
        {"id": 175, "mp": True, "name": "MP 175 Scuba Gear", "type": "sprite"},
        {"id": 178, "mp": True, "name": "MP 178 Scuba Gear", "type": "sprite"},
        {"id": 190, "mp": True, "name": "MP 190 Atomic Health", "type": "sprite"},
        {"id": 193, "mp": True, "name": "MP 193 Devastator", "type": "sprite"},
        {"id": 200, "mp": True, "name": "MP 200 Medkit", "type": "sprite"},
        {"id": 204, "mp": True, "name": "MP 204 RPG", "type": "sprite"},
        {"id": 223, "mp": True, "name": "MP 223 Atomic Health", "type": "sprite"},
        {"id": 234, "mp": True, "name": "MP 234 Pipebombs", "type": "sprite"},
        {"id": 254, "mp": True, "name": "MP 254 Shotgun", "type": "sprite"},
        {"id": 256, "mp": True, "name": "MP 256 Pipebombs", "type": "sprite"},
        {"id": 313, "mp": True, "name": "MP 313 Steroids", "type": "sprite"},
        {"id": 372, "mp": True, "name": "MP 372 Atomic Health", "type": "sprite"},
        {"id": 387, "mp": True, "name": "MP 387 Medkit", "type": "sprite"},
        {"id": 392, "name": "392 Yellow Key Card", "type": "sprite"},
        {"id": 407, "name": "407 Red Key Card", "type": "sprite"},
        {"id": 448, "name": "448 Scuba Gear", "type": "sprite"},
        {"id": 449, "name": "449 Armor", "type": "sprite"},
        {"id": 450, "name": "450 RPG", "type": "sprite"},
        {"id": 465, "mp": True, "name": "MP 465 Chaingun", "type": "sprite"},
        {"id": 178, "name": "Secret 1", "type": "sector"},
        {"id": 221, "name": "Secret 2", "type": "sector"},
        {"id": 222, "name": "Secret 3", "type": "sector"},
        {"id": 232, "name": "Secret 4", "type": "sector"},
        {"id": 259, "name": "Secret 5", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
