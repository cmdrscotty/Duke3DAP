from BaseClasses import Region

from ..base_classes import D3DLevel


class E2L1(D3DLevel):
    name = "Spaceport"
    levelnum = 0
    volumenum = 1
    keys = {"Blue", "Red"}
    location_defs = [
        {
            "name": "Night Vision Goggles behind Red Key Card",
            "id": 31,
            "type": "sprite",
        },
        {"name": "Vent Pipebombs", "id": 40, "type": "sprite"},
        {"name": "Armor near Shrinker", "id": 54, "type": "sprite"},
        {"name": "Secret Shrinker", "id": 58, "type": "sprite"},
        {
            "name": "MP Underwater Passage Freezethrower",
            "id": 60,
            "type": "sprite",
            "mp": True,
        },
        {"name": "Middle Floor Jetpack", "id": 69, "type": "sprite"},
        {"name": "Attic Night Vision Goggles", "id": 81, "type": "sprite"},
        {"name": "Underwater Jetpack", "id": 110, "type": "sprite"},
        {"name": "Bottom Floor Medkit", "id": 155, "type": "sprite"},
        {"name": "Start Shotgun", "id": 156, "type": "sprite"},
        {"name": "Bottom Floor Scuba Gear", "id": 165, "type": "sprite"},
        {"name": "Blue Key Card", "id": 180, "type": "sprite"},
        {"name": "Middle Floor Pipebombs", "id": 235, "type": "sprite"},
        {"name": "Underwater Atomic Health 1", "id": 276, "type": "sprite"},
        {"name": "Underwater Atomic Health 2", "id": 277, "type": "sprite"},
        {"name": "Bottom Floor Armor", "id": 280, "type": "sprite"},
        {"name": "Top Floor Atomic Health", "id": 289, "type": "sprite"},
        {"name": "Red Key Card", "id": 318, "type": "sprite"},
        {"name": "Bottom Floor Holo Duke", "id": 367, "type": "sprite"},
        {"name": "Space Shuttle RPG", "id": 373, "type": "sprite"},
        {"name": "Chaingun behind Red Key Card", "id": 374, "type": "sprite"},
        {"name": "MP Attic Tripbomb 1", "id": 385, "type": "sprite", "mp": True},
        {"name": "MP Attic Tripbomb 2", "id": 386, "type": "sprite", "mp": True},
        {"name": "MP Attic Tripbomb 3", "id": 387, "type": "sprite", "mp": True},
        {"name": "MP Start Armor", "id": 396, "type": "sprite", "mp": True},
        {"name": "Top Floor Devastator", "id": 399, "type": "sprite"},
        {"name": "Middle Room Atomic Health", "id": 420, "type": "sprite"},
        {"name": "Space Shuttle Steroids", "id": 422, "type": "sprite"},
        {"name": "Start Hidden Wall Atomic Health", "id": 448, "type": "sprite"},
        {"name": "Top Floor", "id": 4, "type": "sector"},
        {"name": "Hidden Alcove near Start", "id": 275, "type": "sector"},
        {"name": "Underwater Passage", "id": 304, "type": "sector"},
        {"name": "Ventilation Shaft", "id": 321, "type": "sector"},
        {"name": "Shrinker Room", "id": 334, "type": "sector"},
        {"name": "Hidden Wall near Start", "id": 354, "type": "sector"},
        {"name": "Exit", "id": 0, "type": "exit"},
    ]
