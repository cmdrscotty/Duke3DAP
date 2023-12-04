from BaseClasses import Region

from ..base_classes import D3DLevel


class E2L11(D3DLevel):
    name = "Lunatic Fringe"
    levelnum = 10
    volumenum = 1
    keys = []
    location_defs = [
        {"id": 28, "name": "Center Ring Shrinker", "type": "sprite"},
        {"id": 58, "name": "Top Ledge Devastator", "type": "sprite"},
        {
            "id": 63,
            "mp": True,
            "name": "MP Center Ring Night Vision Goggles",
            "type": "sprite",
        },
        {"id": 92, "name": "Bottom Ring Holo Duke", "type": "sprite"},
        {"id": 93, "name": "Center Ring RPG", "type": "sprite"},
        {"id": 96, "name": "Bottom Ring Armor", "type": "sprite"},
        {"id": 99, "mp": True, "name": "MP Center Ring Jetpack", "type": "sprite"},
        {"id": 102, "name": "Center Ring Atomic Health", "type": "sprite"},
        {"id": 104, "name": "Top Ledge Pipebombs", "type": "sprite"},
        {"id": 109, "name": "Center Ring Steroids", "type": "sprite"},
        {"id": 111, "name": "Bottom Ring Tripmine", "type": "sprite"},
        {"id": 112, "name": "Top Ledge Medkit", "type": "sprite"},
        {"id": 113, "mp": True, "name": "MP Top Ledge Shrinker", "type": "sprite"},
        {"id": 115, "name": "Center Ring Chaingun", "type": "sprite"},
        {"id": 123, "name": "Bottom Ring Shotgun", "type": "sprite"},
        {"id": 124, "name": "Bottom Ring Freezethrower", "type": "sprite"},
        {"id": 125, "name": "Bottom Ring Shotgun", "type": "sprite"},
        {"id": 127, "name": "Center Ring Pipebombs", "type": "sprite"},
        {"id": 180, "name": "Center Top Atomic Health 1", "type": "sprite"},
        {"id": 181, "name": "Center Top Atomic Health 2", "type": "sprite"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]

    def main_region(self) -> Region:
        r = self.rules
        ret = self.region(
            self.name,
            [
                "Top Ledge Devastator",
                "Top Ledge Pipebombs",
                "MP Top Ledge Shrinker",
                "Top Ledge Medkit",
                "Bottom Ring Holo Duke",
                "Bottom Ring Armor",
                "Bottom Ring Tripmine",
                "Bottom Ring Shotgun",
                "Bottom Ring Freezethrower",
                "Bottom Ring Shotgun",
            ],
        )

        center_ring = self.region(
            "Center Top Ring",
            [
                "Center Ring RPG",
                "MP Center Ring Night Vision Goggles",
                "Center Ring Chaingun",
                "Center Ring Steroids",
                "Center Ring Pipebombs",
                "Center Ring Atomic Health",
                "MP Center Ring Jetpack",
                "Center Ring Shrinker",
                "Exit",
            ],
        )
        # can walk across a lizard trooper from the start
        self.connect(ret, center_ring, r.jump | r.difficulty("medium"))
        self.restrict("Exit", r.can_shrink | r.crouch_jump)

        center_top = self.region(
            "Center Top Platform",
            ["Center Top Atomic Health 1", "Center Top Atomic Health 2"],
        )
        self.connect(center_ring, center_top, r.jump)
        return ret
