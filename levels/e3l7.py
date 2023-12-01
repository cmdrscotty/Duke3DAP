from BaseClasses import Region

from ..base_classes import D3DLevel


class E3L7(D3DLevel):
    name = "Fahrenheit"
    levelnum = 6
    volumenum = 2
    keys = ["Red"]
    location_defs = [
        {"id": 39, "mp": True, "name": "MP 39 Shotgun", "type": "sprite"},
        {"id": 60, "mp": True, "name": "MP 60 Night Vision Goggles", "type": "sprite"},
        {"id": 77, "name": "77 Jetpack", "type": "sprite"},
        {"id": 80, "mp": True, "name": "MP 80 Freezethrower", "type": "sprite"},
        {"id": 88, "mp": True, "name": "MP 88 Medkit", "type": "sprite"},
        {"id": 89, "mp": True, "name": "MP 89 Holo Duke", "type": "sprite"},
        {"id": 134, "mp": True, "name": "MP 134 Blue Key Card", "type": "sprite"},
        {"id": 192, "mp": True, "name": "MP 192 Medkit", "type": "sprite"},
        {"id": 202, "mp": True, "name": "MP 202 Armor", "type": "sprite"},
        {"id": 203, "name": "203 Jetpack", "type": "sprite"},
        {"id": 259, "mp": True, "name": "MP 259 Atomic Health", "type": "sprite"},
        {"id": 268, "mp": True, "name": "MP 268 Pipebombs", "type": "sprite"},
        {"id": 294, "mp": True, "name": "MP 294 Devastator", "type": "sprite"},
        {"id": 295, "name": "295 Red Key Card", "type": "sprite"},
        {"id": 299, "mp": True, "name": "MP 299 Chaingun", "type": "sprite"},
        {"id": 334, "mp": True, "name": "MP 334 Medkit", "type": "sprite"},
        {"id": 335, "mp": True, "name": "MP 335 Steroids", "type": "sprite"},
        {"id": 344, "mp": True, "name": "MP 344 Shrinker", "type": "sprite"},
        {"id": 347, "mp": True, "name": "MP 347 Tripbomb", "type": "sprite"},
        {"id": 348, "mp": True, "name": "MP 348 Tripbomb", "type": "sprite"},
        {"id": 368, "mp": True, "name": "MP 368 RPG", "type": "sprite"},
        {"id": 422, "mp": True, "name": "MP 422 Medkit", "type": "sprite"},
        {"id": 426, "mp": True, "name": "MP 426 RPG", "type": "sprite"},
        {"id": 429, "mp": True, "name": "MP 429 Atomic Health", "type": "sprite"},
        {"id": 430, "mp": True, "name": "MP 430 Atomic Health", "type": "sprite"},
        {"id": 431, "mp": True, "name": "MP 431 Shotgun", "type": "sprite"},
        {"id": 432, "name": "432 Yellow Key Card", "type": "sprite"},
        {"id": 111, "name": "Secret 1", "type": "sector"},
        {"id": 133, "name": "Secret 2", "type": "sector"},
        {"id": 176, "name": "Secret 3", "type": "sector"},
        {"id": 179, "name": "Secret 4", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
