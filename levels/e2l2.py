from BaseClasses import Region

from ..base_classes import D3DLevel


class E2L2(D3DLevel):
    name = "Incubator"
    levelnum = 1
    volumenum = 1
    keys = ["Yellow"]
    location_defs = [
        {"name": "MP Underwater Jetpack", "id": 34, "type": "sprite", "mp": True},
        {"name": "Overgrown Passage Jetpack", "id": 67, "type": "sprite"},
        {"name": "Wall Panel Freezethrower", "id": 69, "type": "sprite"},
        {"name": "Underwater Devastator", "id": 82, "type": "sprite"},
        {"name": "Drone Alcove Atomic Health", "id": 99, "type": "sprite"},
        {"name": "Hidden Screen Room Armor", "id": 103, "type": "sprite"},
        {
            "name": "MP Freezethrower behind Yellow Door",
            "id": 130,
            "type": "sprite",
            "mp": True,
        },
        {"name": "EDF Logo Medkit", "id": 132, "type": "sprite"},
        {"name": "Pool Steroids", "id": 133, "type": "sprite"},
        {"name": "Pool Medkit", "id": 134, "type": "sprite"},
        {"name": "Hidden Screen Room Pipebombs", "id": 171, "type": "sprite"},
        {"name": "Armory RPG", "id": 179, "type": "sprite"},
        {"name": "Pipebombs behind Turret", "id": 225, "type": "sprite"},
        {"name": "Scuba Gear", "id": 264, "type": "sprite"},
        {"name": "Force Field Control Atomic Health 1", "id": 266, "type": "sprite"},
        {"name": "Force Filed Control Atomic Health 2", "id": 267, "type": "sprite"},
        {"name": "Force Field Control Chaingun", "id": 268, "type": "sprite"},
        {"name": "Medkit", "id": 285, "type": "sprite"},
        {"name": "Steroids", "id": 325, "type": "sprite"},
        {"name": "Armory Tripbomb 1", "id": 390, "type": "sprite"},
        {"name": "Armory Tripbomb 2", "id": 391, "type": "sprite"},
        {"name": "Armory Tripbomb 3", "id": 392, "type": "sprite"},
        {"name": "Wall Panel Holo Duke", "id": 410, "type": "sprite"},
        {"name": "Cupboard Night Vision Goggles", "id": 432, "type": "sprite"},
        {"name": "Yellow Key Card", "id": 524, "type": "sprite"},
        {"name": "Start Shotgun", "id": 525, "type": "sprite"},
        {"name": "Pipebombs behind Yellow Door", "id": 549, "type": "sprite"},
        {"name": "Overgrown Passage Shrinker", "id": 579, "type": "sprite"},
        {"name": "EDF Logo", "id": 142, "type": "sector"},
        {"name": "Force Field Control Wall", "id": 153, "type": "sector"},
        {"name": "Hidden Screen Room 1", "id": 155, "type": "sector"},
        {"name": "Hidden Screen Room 2", "id": 156, "type": "sector"},
        {"name": "Wall Panel", "id": 248, "type": "sector"},
        {"name": "Exit", "id": 0, "type": "exit"},
    ]
