from BaseClasses import Region

from ..base_classes import D3DLevel


class E3L7(D3DLevel):
    name = "Fahrenheit"
    levelnum = 6
    volumenum = 2
    keys = ["Red"]
    location_defs = [
        {"id": 39, "name": "39 Shotgun", "type": "sprite"},
        {"id": 60, "name": "60 Night Vision Goggles", "type": "sprite"},
        {"id": 77, "mp": True, "name": "MP 77 Jetpack", "type": "sprite"},
        {"id": 80, "name": "80 Freezethrower", "type": "sprite"},
        {"id": 88, "name": "88 Medkit", "type": "sprite"},
        {"id": 89, "name": "89 Holo Duke", "type": "sprite"},
        {"id": 134, "name": "134 Blue Key Card", "type": "sprite"},
        {"id": 192, "name": "192 Medkit", "type": "sprite"},
        {"id": 202, "name": "202 Armor", "type": "sprite"},
        {"id": 203, "mp": True, "name": "MP 203 Jetpack", "type": "sprite"},
        {"id": 259, "name": "259 Atomic Health", "type": "sprite"},
        {"id": 268, "name": "268 Pipebombs", "type": "sprite"},
        {"id": 294, "name": "294 Devastator", "type": "sprite"},
        {"id": 295, "name": "295 Red Key Card", "type": "sprite"},
        {"id": 299, "name": "299 Chaingun", "type": "sprite"},
        {"id": 334, "name": "334 Medkit", "type": "sprite"},
        {"id": 335, "name": "335 Steroids", "type": "sprite"},
        {"id": 344, "name": "344 Shrinker", "type": "sprite"},
        {"id": 347, "name": "347 Tripbomb", "type": "sprite"},
        {"id": 348, "name": "348 Tripbomb", "type": "sprite"},
        {"id": 368, "name": "368 RPG", "type": "sprite"},
        {"id": 422, "name": "422 Medkit", "type": "sprite"},
        {"id": 426, "name": "426 RPG", "type": "sprite"},
        {"id": 429, "name": "429 Atomic Health", "type": "sprite"},
        {"id": 430, "name": "430 Atomic Health", "type": "sprite"},
        {"id": 431, "name": "431 Shotgun", "type": "sprite"},
        {"id": 432, "name": "432 Yellow Key Card", "type": "sprite"},
        {"id": 111, "name": "Secret 1", "type": "sector"},
        {"id": 133, "name": "Secret 2", "type": "sector"},
        {"id": 176, "name": "Secret 3", "type": "sector"},
        {"id": 179, "name": "Secret 4", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
