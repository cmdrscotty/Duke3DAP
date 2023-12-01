from BaseClasses import Region

from ..base_classes import D3DLevel


class E3L3(D3DLevel):
    name = "Flood Zone"
    levelnum = 2
    volumenum = 2
    keys = ["Red"]
    location_defs = [
        {"id": 1, "mp": True, "name": "MP 1 Jetpack", "type": "sprite"},
        {"id": 23, "name": "23 Night Vision Goggles", "type": "sprite"},
        {"id": 24, "name": "24 Night Vision Goggles", "type": "sprite"},
        {"id": 42, "mp": True, "name": "MP 42 Jetpack", "type": "sprite"},
        {"id": 50, "name": "50 Jetpack", "type": "sprite"},
        {"id": 63, "mp": True, "name": "MP 63 Jetpack", "type": "sprite"},
        {"id": 70, "name": "70 Freezethrower", "type": "sprite"},
        {"id": 71, "name": "71 Tripbomb", "type": "sprite"},
        {"id": 72, "name": "72 Tripbomb", "type": "sprite"},
        {"id": 73, "name": "73 Shrinker", "type": "sprite"},
        {"id": 95, "name": "95 Holo Duke", "type": "sprite"},
        {"id": 96, "mp": True, "name": "MP 96 Chaingun", "type": "sprite"},
        {"id": 97, "mp": True, "name": "MP 97 Devastator", "type": "sprite"},
        {"id": 98, "mp": True, "name": "MP 98 Shotgun", "type": "sprite"},
        {"id": 114, "name": "114 Atomic Health", "type": "sprite"},
        {"id": 168, "name": "168 Chaingun", "type": "sprite"},
        {"id": 171, "name": "171 Blue Key Card", "type": "sprite"},
        {"id": 172, "name": "172 Atomic Health", "type": "sprite"},
        {"id": 174, "name": "174 Armor", "type": "sprite"},
        {"id": 175, "name": "175 Scuba Gear", "type": "sprite"},
        {"id": 178, "name": "178 Scuba Gear", "type": "sprite"},
        {"id": 190, "name": "190 Atomic Health", "type": "sprite"},
        {"id": 193, "name": "193 Devastator", "type": "sprite"},
        {"id": 200, "name": "200 Medkit", "type": "sprite"},
        {"id": 204, "name": "204 RPG", "type": "sprite"},
        {"id": 223, "name": "223 Atomic Health", "type": "sprite"},
        {"id": 234, "name": "234 Pipebombs", "type": "sprite"},
        {"id": 254, "name": "254 Shotgun", "type": "sprite"},
        {"id": 256, "name": "256 Pipebombs", "type": "sprite"},
        {"id": 313, "name": "313 Steroids", "type": "sprite"},
        {"id": 372, "name": "372 Atomic Health", "type": "sprite"},
        {"id": 387, "name": "387 Medkit", "type": "sprite"},
        {"id": 392, "name": "392 Yellow Key Card", "type": "sprite"},
        {"id": 407, "name": "407 Red Key Card", "type": "sprite"},
        {"id": 448, "mp": True, "name": "MP 448 Scuba Gear", "type": "sprite"},
        {"id": 449, "mp": True, "name": "MP 449 Armor", "type": "sprite"},
        {"id": 450, "mp": True, "name": "MP 450 RPG", "type": "sprite"},
        {"id": 465, "name": "465 Chaingun", "type": "sprite"},
        {"id": 178, "name": "Secret 1", "type": "sector"},
        {"id": 221, "name": "Secret 2", "type": "sector"},
        {"id": 222, "name": "Secret 3", "type": "sector"},
        {"id": 232, "name": "Secret 4", "type": "sector"},
        {"id": 259, "name": "Secret 5", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
