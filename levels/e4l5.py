from BaseClasses import Region

from ..base_classes import D3DLevel


class E4L5(D3DLevel):
    name = "Pigsty"
    levelnum = 4
    volumenum = 3
    keys = ["Red"]
    location_defs = [
        {"id": 61, "name": "61 Pipebombs", "type": "sprite"},
        {"id": 76, "name": "76 Atomic Health", "type": "sprite"},
        {"id": 79, "name": "79 Steroids", "type": "sprite"},
        {"id": 80, "name": "80 Steroids", "type": "sprite"},
        {"id": 90, "name": "90 Freezethrower", "type": "sprite"},
        {"id": 91, "name": "91 Devastator", "type": "sprite"},
        {"id": 92, "name": "92 RPG", "type": "sprite"},
        {"id": 123, "name": "123 Atomic Health", "type": "sprite"},
        {"id": 142, "mp": True, "name": "MP 142 Shotgun", "type": "sprite"},
        {"id": 196, "name": "196 Tripmine", "type": "sprite"},
        {"id": 197, "name": "197 Tripmine", "type": "sprite"},
        {"id": 198, "name": "198 Freezethrower", "type": "sprite"},
        {"id": 211, "name": "211 Jetpack", "type": "sprite"},
        {"id": 260, "name": "260 RPG", "type": "sprite"},
        {"id": 264, "name": "264 Medkit", "type": "sprite"},
        {"id": 266, "name": "266 Atomic Health", "type": "sprite"},
        {"id": 267, "name": "267 Steroids", "type": "sprite"},
        {"id": 268, "name": "268 Medkit", "type": "sprite"},
        {"id": 363, "name": "363 Blue Key Card", "type": "sprite"},
        {"id": 441, "name": "441 Atomic Health", "type": "sprite"},
        {"id": 528, "name": "528 Chaingun", "type": "sprite"},
        {"id": 529, "name": "529 Chaingun", "type": "sprite"},
        {"id": 530, "name": "530 Chaingun", "type": "sprite"},
        {"id": 613, "name": "613 Shotgun", "type": "sprite"},
        {"id": 618, "name": "618 Chaingun", "type": "sprite"},
        {"id": 717, "name": "717 Pipebombs", "type": "sprite"},
        {"id": 751, "name": "751 Yellow Key Card", "type": "sprite"},
        {"id": 767, "mp": True, "name": "MP 767 Jetpack", "type": "sprite"},
        {"id": 768, "name": "768 Shrinker", "type": "sprite"},
        {"id": 771, "name": "771 Armor", "type": "sprite"},
        {"id": 773, "name": "773 Night Vision Goggles", "type": "sprite"},
        {"id": 811, "name": "811 Pipebombs", "type": "sprite"},
        {"id": 812, "mp": True, "name": "MP 812 Armor", "type": "sprite"},
        {"id": 813, "mp": True, "name": "MP 813 Shotgun", "type": "sprite"},
        {"id": 841, "name": "841 Holo Duke", "type": "sprite"},
        {"id": 854, "name": "854 Red Key Card", "type": "sprite"},
        {"id": 5, "name": "Secret 1", "type": "sector"},
        {"id": 56, "name": "Secret 2", "type": "sector"},
        {"id": 123, "name": "Secret 3", "type": "sector"},
        {"id": 465, "name": "Secret 4", "type": "sector"},
        {"id": 469, "name": "Secret 5", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
        {"id": 10, "name": "Secret Exit", "type": "exit"},
    ]
