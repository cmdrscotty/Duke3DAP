from BaseClasses import Region

from ..base_classes import D3DLevel


class E1L2(D3DLevel):
    name = "Red Light District"
    levelnum = 1
    volumenum = 0
    keys = {"Blue", "Red", "Yellow"}
    location_defs = [
        {"name": "Blue Key Card", "id": 27, "type": "sprite"},
        {"name": "Sewers Jetpack", "id": 51, "type": "sprite"},
        {"name": "Sewers Night Vision Goggles", "id": 52, "type": "sprite"},
        {"name": "Sewers Steroids", "id": 53, "type": "sprite"},
        {"name": "Sewers Holo Duke", "id": 54, "type": "sprite"},
        {"name": "Vent Pipebombs", "id": 63, "type": "sprite"},
        {
            "name": "MP Steroids outside Strip Floor",
            "id": 120,
            "type": "sprite",
            "mp": True,
        },
        {"name": "Night Vision Goggles behind Curtains", "id": 170, "type": "sprite"},
        {"name": "Strippers Chaingun", "id": 174, "type": "sprite"},
        {"name": "Yellow Key Card", "id": 179, "type": "sprite"},
        {"name": "Dark Area Atomic Health", "id": 183, "type": "sprite"},
        {"name": "Toilets Night Vision Goggles", "id": 186, "type": "sprite"},
        {"name": "Pornography Store Shelves Pipebombs", "id": 188, "type": "sprite"},
        {"name": "Pornography Store Shelves Armor", "id": 189, "type": "sprite"},
        {"name": "Video Booth RPG", "id": 192, "type": "sprite"},
        {"name": "Pornography Store Corner Holo Duke", "id": 208, "type": "sprite"},
        {"name": "Red Key Card", "id": 249, "type": "sprite"},
        {"name": "Sewers Atomic Health", "id": 260, "type": "sprite"},
        {"name": "Sewers Pipebombs", "id": 265, "type": "sprite"},
        {"name": "Attic Medkit", "id": 278, "type": "sprite"},
        {"name": "MP Outside Ledge Jetpack", "id": 366, "type": "sprite", "mp": True},
        {"name": "Outside Ledge Armor", "id": 367, "type": "sprite"},
        {"name": "Strip Club Entrance Shotgun", "id": 391, "type": "sprite"},
        {
            "name": "Video Booth Steroids",
            "id": 407,
            "type": "sprite",
            "sprite_type": "trashcan",
        },
        {"name": "Chaingun near Blue Key Card", "id": 442, "type": "sprite"},
        {"name": "Vent Atomic Health", "id": 497, "type": "sprite"},
        {"name": "Pornography Store Shotgun", "id": 515, "type": "sprite"},
        {"name": "MP Bar RPG", "id": 751, "type": "sprite", "mp": True},
        {"name": "Pornography Store Atomic Health", "id": 822, "type": "sprite"},
        {"name": "Construction Site Medkit", "id": 823, "type": "sprite"},
        {
            "name": "MP Outside Ledge Spawn Pipebombs",
            "id": 824,
            "type": "sprite",
            "mp": True,
        },
        {"name": "Strip Club Vents", "id": 91, "type": "sector"},
        {"name": "Hidden Ledge behind Curtains", "id": 107, "type": "sector"},
        {"name": "Pornography Store Corner", "id": 158, "type": "sector"},
        {"name": "Pornography Store Shelves", "id": 161, "type": "sector"},
        {"name": "Pornography Store Dark Area", "id": 172, "type": "sector"},
        {"name": "Behind Strippers", "id": 177, "type": "sector"},
        {"name": "Attic Hidden Compartment", "id": 187, "type": "sector"},
        {"name": "Sewers", "id": 218, "type": "sector"},
        {"name": "Exit", "id": 0, "type": "exit"},
    ]
