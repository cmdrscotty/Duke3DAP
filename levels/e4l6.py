from BaseClasses import Region

from ..base_classes import D3DLevel


class E4L6(D3DLevel):
    name = "Going Postal"
    levelnum = 5
    volumenum = 3
    keys = ["Red"]
    location_defs = [
        {"id": 25, "mp": True, "name": "MP 25 Protective Boots", "type": "sprite"},
        {"id": 26, "mp": True, "name": "MP 26 Devastator", "type": "sprite"},
        {"id": 81, "mp": True, "name": "MP 81 Pipebombs", "type": "sprite"},
        {"id": 84, "mp": True, "name": "MP 84 Shrinker", "type": "sprite"},
        {"id": 145, "name": "145 Red Key Card", "type": "sprite"},
        {"id": 206, "mp": True, "name": "MP 206 Chaingun", "type": "sprite"},
        {"id": 209, "mp": True, "name": "MP 209 Armor", "type": "sprite"},
        {"id": 210, "mp": True, "name": "MP 210 Medkit", "type": "sprite"},
        {"id": 217, "mp": True, "name": "MP 217 Pipebombs", "type": "sprite"},
        {"id": 266, "mp": True, "name": "MP 266 Tripbomb", "type": "sprite"},
        {"id": 267, "mp": True, "name": "MP 267 Tripbomb", "type": "sprite"},
        {"id": 277, "mp": True, "name": "MP 277 Holo Duke", "type": "sprite"},
        {"id": 279, "mp": True, "name": "MP 279 Atomic Health", "type": "sprite"},
        {"id": 281, "mp": True, "name": "MP 281 Freezethrower", "type": "sprite"},
        {"id": 284, "mp": True, "name": "MP 284 Steroids", "type": "sprite"},
        {"id": 286, "mp": True, "name": "MP 286 Armor", "type": "sprite"},
        {"id": 287, "mp": True, "name": "MP 287 Shotgun", "type": "sprite"},
        {"id": 288, "mp": True, "name": "MP 288 Pipebombs", "type": "sprite"},
        {"id": 290, "mp": True, "name": "MP 290 Devastator", "type": "sprite"},
        {
            "id": 291,
            "mp": True,
            "name": "MP 291 Night Vision Goggles",
            "type": "sprite",
        },
        {"id": 293, "mp": True, "name": "MP 293 Steroids", "type": "sprite"},
        {"id": 294, "mp": True, "name": "MP 294 Armor", "type": "sprite"},
        {"id": 295, "name": "295 Jetpack", "type": "sprite"},
        {"id": 296, "mp": True, "name": "MP 296 Medkit", "type": "sprite"},
        {"id": 305, "mp": True, "name": "MP 305 Chaingun", "type": "sprite"},
        {"id": 306, "mp": True, "name": "MP 306 RPG", "type": "sprite"},
        {"id": 353, "mp": True, "name": "MP 353 Atomic Health", "type": "sprite"},
        {"id": 464, "mp": True, "name": "MP 464 Atomic Health", "type": "sprite"},
        {"id": 530, "mp": True, "name": "MP 530 Atomic Health", "type": "sprite"},
        {"id": 534, "mp": True, "name": "MP 534 Blue Key Card", "type": "sprite"},
        {"id": 590, "mp": True, "name": "MP 590 Devastator", "type": "sprite"},
        {"id": 635, "mp": True, "name": "MP 635 Shotgun", "type": "sprite"},
        {"id": 665, "mp": True, "name": "MP 665 Atomic Health", "type": "sprite"},
        {"id": 672, "mp": True, "name": "MP 672 Medkit", "type": "sprite"},
        {"id": 724, "name": "724 Yellow Key Card", "type": "sprite"},
        {"id": 750, "mp": True, "name": "MP 750 Pipebombs", "type": "sprite"},
        {"id": 185, "name": "Secret 1", "type": "sector"},
        {"id": 250, "name": "Secret 2", "type": "sector"},
        {"id": 302, "name": "Secret 3", "type": "sector"},
        {"id": 317, "name": "Secret 4", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
