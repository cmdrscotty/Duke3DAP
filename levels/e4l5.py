from BaseClasses import Region

from ..base_classes import D3DLevel


class E4L5(D3DLevel):
    name = "Pigsty"
    levelnum = 4
    volumenum = 3
    keys = ["Red"]
    location_defs = [
        {"id": 61, "mp": True, "name": "MP 61 Pipebombs", "type": "sprite"},
        {"id": 76, "mp": True, "name": "MP 76 Atomic Health", "type": "sprite"},
        {"id": 79, "mp": True, "name": "MP 79 Steroids", "type": "sprite"},
        {"id": 80, "mp": True, "name": "MP 80 Steroids", "type": "sprite"},
        {"id": 90, "mp": True, "name": "MP 90 Freezethrower", "type": "sprite"},
        {"id": 91, "mp": True, "name": "MP 91 Devastator", "type": "sprite"},
        {"id": 92, "mp": True, "name": "MP 92 RPG", "type": "sprite"},
        {"id": 123, "mp": True, "name": "MP 123 Atomic Health", "type": "sprite"},
        {"id": 142, "name": "142 Shotgun", "type": "sprite"},
        {"id": 196, "mp": True, "name": "MP 196 Tripbomb", "type": "sprite"},
        {"id": 197, "mp": True, "name": "MP 197 Tripbomb", "type": "sprite"},
        {"id": 198, "mp": True, "name": "MP 198 Freezethrower", "type": "sprite"},
        {"id": 211, "mp": True, "name": "MP 211 Jetpack", "type": "sprite"},
        {"id": 260, "mp": True, "name": "MP 260 RPG", "type": "sprite"},
        {"id": 264, "mp": True, "name": "MP 264 Medkit", "type": "sprite"},
        {"id": 266, "mp": True, "name": "MP 266 Atomic Health", "type": "sprite"},
        {"id": 267, "mp": True, "name": "MP 267 Steroids", "type": "sprite"},
        {"id": 268, "mp": True, "name": "MP 268 Medkit", "type": "sprite"},
        {"id": 363, "mp": True, "name": "MP 363 Blue Key Card", "type": "sprite"},
        {"id": 441, "mp": True, "name": "MP 441 Atomic Health", "type": "sprite"},
        {"id": 528, "mp": True, "name": "MP 528 Chaingun", "type": "sprite"},
        {"id": 529, "mp": True, "name": "MP 529 Chaingun", "type": "sprite"},
        {"id": 530, "mp": True, "name": "MP 530 Chaingun", "type": "sprite"},
        {"id": 613, "mp": True, "name": "MP 613 Shotgun", "type": "sprite"},
        {"id": 618, "mp": True, "name": "MP 618 Chaingun", "type": "sprite"},
        {"id": 717, "mp": True, "name": "MP 717 Pipebombs", "type": "sprite"},
        {"id": 751, "name": "751 Yellow Key Card", "type": "sprite"},
        {"id": 767, "name": "767 Jetpack", "type": "sprite"},
        {"id": 768, "mp": True, "name": "MP 768 Shrinker", "type": "sprite"},
        {"id": 771, "mp": True, "name": "MP 771 Armor", "type": "sprite"},
        {
            "id": 773,
            "mp": True,
            "name": "MP 773 Night Vision Goggles",
            "type": "sprite",
        },
        {"id": 811, "mp": True, "name": "MP 811 Pipebombs", "type": "sprite"},
        {"id": 812, "name": "812 Armor", "type": "sprite"},
        {"id": 813, "name": "813 Shotgun", "type": "sprite"},
        {"id": 841, "mp": True, "name": "MP 841 Holo Duke", "type": "sprite"},
        {"id": 854, "name": "854 Red Key Card", "type": "sprite"},
        {"id": 5, "name": "Secret 1", "type": "sector"},
        {"id": 56, "name": "Secret 2", "type": "sector"},
        {"id": 123, "name": "Secret 3", "type": "sector"},
        {"id": 465, "name": "Secret 4", "type": "sector"},
        {"id": 469, "name": "Secret 5", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
