from BaseClasses import Region

from ..base_classes import D3DLevel


class E1L7(D3DLevel):
    name = "Faces of Death"
    levelnum = 6
    volumenum = 0
    keys = {"Blue"}
    location_defs = [
        {"name": "MP Side Room Devastator", "id": 0, "type": "sprite", "mp": True},
        {"name": "MP Side Room RPG", "id": 1, "type": "sprite", "mp": True},
        {"name": "Waterfall 2 Atomic Health", "id": 21, "type": "sprite"},
        {"name": "Waterfall 2 Armor", "id": 22, "type": "sprite"},
        {"name": "Waterfall 1 Armor", "id": 23, "type": "sprite"},
        {"name": "Waterfall 1 Atomic Health", "id": 24, "type": "sprite"},
        {"name": "Side Room Atomic Health 1", "id": 97, "type": "sprite"},
        {"name": "Side Room Atomic Health 2", "id": 98, "type": "sprite"},
        {"name": "Side Room Armor", "id": 107, "type": "sprite"},
        {"name": "Side Room Holo Duke", "id": 108, "type": "sprite"},
        {"name": "Center Atomic Health", "id": 109, "type": "sprite"},
        {"name": "Center Armor", "id": 110, "type": "sprite"},
        {"name": "Center Protective Boots", "id": 111, "type": "sprite"},
        {"name": "Center Night Vision Goggles", "id": 112, "type": "sprite"},
        {"name": "Center Steroids", "id": 113, "type": "sprite"},
        {"name": "Side Room Tripmine 2", "id": 121, "type": "sprite"},
        {"name": "Side Room Tripmine 2", "id": 122, "type": "sprite"},
        {"name": "Side Room Pipebombs", "id": 127, "type": "sprite"},
        {"name": "Main Room Shotgun", "id": 179, "type": "sprite"},
        {"name": "Main Room Devastator", "id": 231, "type": "sprite"},
        {"name": "Main Room Freezethrower", "id": 232, "type": "sprite"},
        {"name": "Main Room Chaingun", "id": 233, "type": "sprite"},
        {"name": "Main Room RPG", "id": 234, "type": "sprite"},
        {"name": "Main Room Jetpack", "id": 235, "type": "sprite"},
        {"name": "Main Room Tripmine 1", "id": 236, "type": "sprite"},
        {"name": "Main Room Tripmine 2", "id": 237, "type": "sprite"},
        {"name": "Main Room Shrinker", "id": 238, "type": "sprite"},
        {"name": "Main Room Pipebombs", "id": 248, "type": "sprite"},
        {"name": "Blue Key Card", "id": 302, "type": "sprite"},
        {"name": "Behind Waterfall 1", "id": 110, "type": "sector"},
        {"name": "Behind Waterfall 2", "id": 111, "type": "sector"},
    ]
