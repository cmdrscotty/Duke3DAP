from BaseClasses import Region

from ..base_classes import D3DLevel


class E3L4(D3DLevel):
    name = "L.A. Rumble"
    levelnum = 3
    volumenum = 2
    keys = ["Red"]
    location_defs = [
        {"id": 59, "name": "59 Red Key Card", "type": "sprite"},
        {"id": 82, "name": "82 Atomic Health", "type": "sprite"},
        {"id": 114, "name": "114 Shrinker", "type": "sprite"},
        {"id": 135, "name": "135 Medkit", "type": "sprite"},
        {"id": 136, "name": "136 Devastator", "type": "sprite"},
        {"id": 137, "name": "137 Night Vision Goggles", "type": "sprite"},
        {"id": 244, "name": "244 Steroids", "type": "sprite"},
        {"id": 247, "mp": True, "name": "MP 247 Shotgun", "type": "sprite"},
        {"id": 248, "name": "248 Pipebombs", "type": "sprite"},
        {"id": 274, "name": "274 Chaingun", "type": "sprite"},
        {"id": 275, "name": "275 Shotgun", "type": "sprite"},
        {"id": 276, "name": "276 RPG", "type": "sprite"},
        {"id": 277, "name": "277 Atomic Health", "type": "sprite"},
        {"id": 283, "name": "283 RPG", "type": "sprite"},
        {"id": 336, "name": "336 Atomic Health", "type": "sprite"},
        {"id": 339, "name": "339 Jetpack", "type": "sprite"},
        {"id": 391, "name": "391 Medkit", "type": "sprite"},
        {"id": 442, "name": "442 Pipebombs", "type": "sprite"},
        {"id": 458, "name": "458 Armor", "type": "sprite"},
        {"id": 468, "name": "468 Holo Duke", "type": "sprite"},
        {"id": 475, "name": "475 Blue Key Card", "type": "sprite"},
        {"id": 500, "mp": True, "name": "MP 500 Jetpack", "type": "sprite"},
        {"id": 501, "mp": True, "name": "MP 501 Jetpack", "type": "sprite"},
        {"id": 502, "mp": True, "name": "MP 502 RPG", "type": "sprite"},
        {"id": 503, "mp": True, "name": "MP 503 Chaingun", "type": "sprite"},
        {"id": 506, "name": "506 Freezethrower", "type": "sprite"},
        {"id": 507, "mp": True, "name": "MP 507 Atomic Health", "type": "sprite"},
        {"id": 508, "mp": True, "name": "MP 508 Jetpack", "type": "sprite"},
        {"id": 509, "mp": True, "name": "MP 509 Pipebombs", "type": "sprite"},
        {"id": 511, "name": "511 Tripbomb", "type": "sprite"},
        {"id": 512, "name": "512 Tripbomb", "type": "sprite"},
        {"id": 513, "name": "513 Freezethrower", "type": "sprite"},
        {"id": 515, "name": "515 Medkit", "type": "sprite"},
        {"id": 166, "name": "Secret 1", "type": "sector"},
        {"id": 195, "name": "Secret 2", "type": "sector"},
        {"id": 205, "name": "Secret 3", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
