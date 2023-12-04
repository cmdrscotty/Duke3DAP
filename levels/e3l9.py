from BaseClasses import Region

from ..base_classes import D3DLevel


class E3L9(D3DLevel):
    name = "Stadium"
    levelnum = 8
    volumenum = 2
    keys = []
    location_defs = [
        {"id": 1, "mp": True, "name": "MP Floor Armor", "type": "sprite"},
        {"id": 12, "mp": True, "name": "MP Ledge Shotgun", "type": "sprite"},
        {"id": 13, "name": "Floor Pipebombs 1", "type": "sprite"},
        {"id": 14, "name": "Floor Pipebombs 2", "type": "sprite"},
        {"id": 15, "name": "Floor Pipebombs 3", "type": "sprite"},
        {"id": 16, "name": "Floor Pipebombs 4", "type": "sprite"},
        {"id": 17, "name": "Ledge Shrinker 1", "type": "sprite"},
        {"id": 18, "mp": True, "name": "MP Floor Chaingun", "type": "sprite"},
        {"id": 19, "mp": True, "name": "MP Floor Freezethrower", "type": "sprite"},
        {"id": 20, "mp": True, "name": "MP Floor RPG", "type": "sprite"},
        {"id": 21, "mp": True, "name": "MP Floor Devastator", "type": "sprite"},
        {"id": 23, "name": "Ledge Shrinker 2", "type": "sprite"},
        {"id": 24, "name": "Ledge Night Vision Goggles 1", "type": "sprite"},
        {"id": 25, "name": "Ledge Holo Duke", "type": "sprite"},
        {"id": 45, "name": "Ledge Chaingun", "type": "sprite"},
        {"id": 46, "name": "Ledge Jetpack", "type": "sprite"},
        {"id": 47, "name": "Ledge RPG", "type": "sprite"},
        {"id": 48, "name": "Ledge Freezethrower", "type": "sprite"},
        {"id": 49, "name": "Ledge Shotgun", "type": "sprite"},
        {"id": 50, "name": "Ledge Devastator", "type": "sprite"},
        {"id": 51, "name": "Floor Steroids 1", "type": "sprite"},
        {"id": 52, "name": "Floor Steroids 2", "type": "sprite"},
        {"id": 85, "mp": True, "name": "MP Ledge Jetpack 1", "type": "sprite"},
        {"id": 86, "mp": True, "name": "MP Ledge Jetpack 2", "type": "sprite"},
        {"id": 87, "name": "Floor Night Vision Goggles", "type": "sprite"},
        {"id": 88, "mp": True, "name": "MP Ledge Chaingun", "type": "sprite"},
        {"id": 89, "mp": True, "name": "MP Ledge Pipebombs", "type": "sprite"},
        {"id": 90, "mp": True, "name": "MP Ledge Devastator", "type": "sprite"},
        {"id": 91, "mp": True, "name": "MP Ledge RPG", "type": "sprite"},
        {"id": 92, "mp": True, "name": "MP Ledge Shrinker", "type": "sprite"},
        {"id": 93, "mp": True, "name": "MP Ledge Freezethrower", "type": "sprite"},
        {"id": 94, "name": "Floor Medkit", "type": "sprite"},
        {"id": 95, "name": "Ledge Night Vision Goggles 2", "type": "sprite"},
        {"id": 104, "name": "Floor Atomic Health 1", "type": "sprite"},
        {"id": 105, "name": "Floor Atomic Health 2", "type": "sprite"},
        {"id": 106, "name": "Floor Atomic Health 3", "type": "sprite"},
        {"id": 107, "name": "Floor Atomic Health 4", "type": "sprite"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
    has_boss = True

    def main_region(self) -> Region:
        r = self.rules
        ret = self.region(
            self.name,
            [
                "MP Floor Armor",
                "Floor Pipebombs 1",
                "Floor Pipebombs 2",
                "Floor Pipebombs 3",
                "Floor Pipebombs 4",
                "MP Floor Chaingun",
                "MP Floor Freezethrower",
                "MP Floor RPG",
                "MP Floor Devastator",
                "Floor Steroids 1",
                "Floor Steroids 2",
                "Floor Night Vision Goggles",
                "Floor Medkit",
                "Floor Atomic Health 1",
                "Floor Atomic Health 2",
                "Floor Atomic Health 3",
                "Floor Atomic Health 4",
                "Exit",
            ],
        )
        self.restrict("Exit", r.can_kill_boss_3)

        ledge = self.region(
            "Stadium Ledge",
            [
                "MP Ledge Shotgun",
                "Ledge Shrinker 1",
                "Ledge Shrinker 2",
                "Ledge Night Vision Goggles 1",
                "Ledge Holo Duke",
                "Ledge Chaingun",
                "Ledge Jetpack",
                "Ledge RPG",
                "Ledge Freezethrower",
                "Ledge Shotgun",
                "Ledge Devastator",
                "MP Ledge Jetpack 1",
                "MP Ledge Jetpack 2",
                "MP Ledge Chaingun",
                "MP Ledge Pipebombs",
                "MP Ledge Devastator",
                "MP Ledge RPG",
                "MP Ledge Shrinker",
                "MP Ledge Freezethrower",
                "Ledge Night Vision Goggles 2",
            ],
        )
        self.connect(ret, ledge, r.can_jump)
        return ret
