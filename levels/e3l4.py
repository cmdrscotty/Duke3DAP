from BaseClasses import Region

from ..base_classes import D3DLevel


class E3L4(D3DLevel):
    name = "L.A. Rumble"
    levelnum = 3
    volumenum = 2
    keys = ["Red"]
    location_defs = [
        {"id": 59, "name": "59 Red Key Card", "type": "sprite"},
        {"id": 82, "mp": True, "name": "MP 82 Atomic Health", "type": "sprite"},
        {"id": 114, "mp": True, "name": "MP 114 Shrinker", "type": "sprite"},
        {"id": 135, "mp": True, "name": "MP 135 Medkit", "type": "sprite"},
        {"id": 136, "mp": True, "name": "MP 136 Devastator", "type": "sprite"},
        {
            "id": 137,
            "mp": True,
            "name": "MP 137 Night Vision Goggles",
            "type": "sprite",
        },
        {"id": 244, "mp": True, "name": "MP 244 Steroids", "type": "sprite"},
        {"id": 247, "name": "247 Shotgun", "type": "sprite"},
        {"id": 248, "mp": True, "name": "MP 248 Pipebombs", "type": "sprite"},
        {"id": 274, "mp": True, "name": "MP 274 Chaingun", "type": "sprite"},
        {"id": 275, "mp": True, "name": "MP 275 Shotgun", "type": "sprite"},
        {"id": 276, "mp": True, "name": "MP 276 RPG", "type": "sprite"},
        {"id": 277, "mp": True, "name": "MP 277 Atomic Health", "type": "sprite"},
        {"id": 283, "mp": True, "name": "MP 283 RPG", "type": "sprite"},
        {"id": 336, "mp": True, "name": "MP 336 Atomic Health", "type": "sprite"},
        {"id": 339, "mp": True, "name": "MP 339 Jetpack", "type": "sprite"},
        {"id": 391, "mp": True, "name": "MP 391 Medkit", "type": "sprite"},
        {"id": 442, "mp": True, "name": "MP 442 Pipebombs", "type": "sprite"},
        {"id": 458, "mp": True, "name": "MP 458 Armor", "type": "sprite"},
        {"id": 468, "mp": True, "name": "MP 468 Holo Duke", "type": "sprite"},
        {"id": 475, "mp": True, "name": "MP 475 Blue Key Card", "type": "sprite"},
        {"id": 500, "name": "500 Jetpack", "type": "sprite"},
        {"id": 501, "name": "501 Jetpack", "type": "sprite"},
        {"id": 502, "name": "502 RPG", "type": "sprite"},
        {"id": 503, "name": "503 Chaingun", "type": "sprite"},
        {"id": 506, "mp": True, "name": "MP 506 Freezethrower", "type": "sprite"},
        {"id": 507, "name": "507 Atomic Health", "type": "sprite"},
        {"id": 508, "name": "508 Jetpack", "type": "sprite"},
        {"id": 509, "name": "509 Pipebombs", "type": "sprite"},
        {"id": 511, "mp": True, "name": "MP 511 Tripbomb", "type": "sprite"},
        {"id": 512, "mp": True, "name": "MP 512 Tripbomb", "type": "sprite"},
        {"id": 513, "mp": True, "name": "MP 513 Freezethrower", "type": "sprite"},
        {"id": 515, "mp": True, "name": "MP 515 Medkit", "type": "sprite"},
        {"id": 166, "name": "Secret 1", "type": "sector"},
        {"id": 195, "name": "Secret 2", "type": "sector"},
        {"id": 205, "name": "Secret 3", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
