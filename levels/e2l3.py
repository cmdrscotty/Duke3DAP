from BaseClasses import Region

from ..base_classes import D3DLevel


class E2L3(D3DLevel):
    name = "Warp Factor"
    levelnum = 2
    volumenum = 1
    keys = ["Blue", "Yellow"]
    location_defs = [
        {"name": "Engine Room Atomic Health", "id": 9, "type": "sprite"},
        {"name": "Engine Room Shotgun", "id": 10, "type": "sprite"},
        {"name": "MP Drone Room Holo Duke", "id": 13, "type": "sprite", "mp": True},
        {"name": "Blue Key Card", "id": 14, "type": "sprite"},
        {"name": "Main Room Shrinker", "id": 47, "type": "sprite"},
        {"name": "Engine Room Armor", "id": 61, "type": "sprite"},
        {"name": "MP Control Room Jetpack", "id": 91, "type": "sprite", "mp": True},
        {"name": "Ready Room Medkit", "id": 96, "type": "sprite"},
        {"name": "Control Room Devastator", "id": 135, "type": "sprite"},
        {"name": "Engine Room Tripbomb", "id": 162, "type": "sprite"},
        {"name": "Start Chaingun", "id": 177, "type": "sprite"},
        {"name": "Wall Panel Freezethrower", "id": 182, "type": "sprite"},
        {"name": "Wall Panel Pipebombs", "id": 226, "type": "sprite"},
        {"name": "Reactor Atomic Health 1", "id": 274, "type": "sprite"},
        {"name": "Reactor Atomic Health 2", "id": 275, "type": "sprite"},
        {"name": "Control Room Medkit", "id": 284, "type": "sprite"},
        {"name": "Yellow Key Card", "id": 316, "type": "sprite"},
        {"name": "Control Room Holo Duke", "id": 496, "type": "sprite"},
        {"name": "Conveyor Night Vision Goggles", "id": 694, "type": "sprite"},
        {"name": "Control Room Steroids", "id": 695, "type": "sprite"},
        {"name": "Engine Room Burrowed Atomic Health 1", "id": 699, "type": "sprite"},
        {"name": "Drone Room Medkit", "id": 725, "type": "sprite"},
        {"name": "Engine Room Burrowed Atomic Health 2", "id": 766, "type": "sprite"},
        {"name": "Engine Room Burrowed Atomic Health 3", "id": 767, "type": "sprite"},
        {"name": "Main Room Shotgun", "id": 768, "type": "sprite"},
        {"name": "Control Room RPG", "id": 772, "type": "sprite"},
        {"name": "Left Wing RPG", "id": 782, "type": "sprite"},
        {"name": "MP Control Room Armor", "id": 799, "type": "sprite", "mp": True},
        {"name": "MP Main Room Chaingun", "id": 801, "type": "sprite", "mp": True},
        {"name": "Really Ready Room Devastator", "id": 817, "type": "sprite"},
        {"name": "Really Ready Room Freezethrower", "id": 818, "type": "sprite"},
        {"name": "Bridge Chaingun", "id": 819, "type": "sprite"},
        {"name": "Bridge Pipebombs", "id": 820, "type": "sprite"},
        {"name": "Bridge RPG", "id": 821, "type": "sprite"},
        {"name": "Bridge Atomic Health", "id": 822, "type": "sprite"},
        {"name": "Bridge", "id": 42, "type": "sector"},
        {"name": "Ready Room", "id": 297, "type": "sector"},
        {"name": "Exit", "id": 0, "type": "exit"},
    ]
