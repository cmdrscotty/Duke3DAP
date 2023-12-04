from BaseClasses import Region

from ..base_classes import D3DLevel


class E2L4(D3DLevel):
    name = "Fusion Station"
    levelnum = 3
    volumenum = 1
    keys = []
    location_defs = [
        {"id": 3, "name": "Timed Room Freezethrower", "type": "sprite"},
        {"id": 13, "name": "Column Armor", "type": "sprite"},
        {"id": 18, "name": "Start Night Vision Goggles", "type": "sprite"},
        {"id": 19, "name": "First Level Night Vision Goggles", "type": "sprite"},
        {"id": 20, "name": "Reactor Night Vision Goggles", "type": "sprite"},
        {"id": 46, "name": "Top Floor Chaingun", "type": "sprite"},
        {"id": 54, "mp": True, "name": "MP Reactor Holo Duke", "type": "sprite"},
        {"id": 111, "name": "Start Atomic Health", "type": "sprite"},
        {"id": 135, "name": "Pistons Tripmine 1", "type": "sprite"},
        {"id": 136, "name": "Pistons Tripmine 2", "type": "sprite"},
        {"id": 139, "name": "Pistons Protective Boots", "type": "sprite"},
        {"id": 142, "name": "Top Ledge Atomic Health 1", "type": "sprite"},
        {"id": 143, "name": "Top Ledge Atomic Health 2", "type": "sprite"},
        {"id": 158, "name": "Red Room Devastator", "type": "sprite"},
        {"id": 159, "name": "Top Floor Atomic Health", "type": "sprite"},
        {"id": 167, "name": "Top Floor Medkit", "type": "sprite"},
        {"id": 210, "name": "Start Armor", "type": "sprite"},
        {"id": 253, "name": "Top Ledge Jetpack", "type": "sprite"},
        {"id": 696, "name": "Vents Atomic Health", "type": "sprite"},
        {"id": 715, "name": "Shotgun behind Babe", "type": "sprite"},
        {"id": 718, "name": "Pistons Medkit", "type": "sprite"},
        {"id": 720, "name": "Pistons Tripmine 3", "type": "sprite"},
        {"id": 721, "name": "Pistons Night Vision Goggles", "type": "sprite"},
        {"id": 722, "name": "Pistons Chaingun", "type": "sprite"},
        {"id": 739, "name": "First Level Shrinker", "type": "sprite"},
        {"id": 750, "name": "Underwater Pipebombs 1", "type": "sprite"},
        {"id": 751, "name": "Underwater Pipebombs 2", "type": "sprite"},
        {"id": 756, "name": "Start RPG", "type": "sprite"},
        {"id": 759, "mp": True, "name": "MP Floor Jetpack 1", "type": "sprite"},
        {"id": 760, "mp": True, "name": "MP Floor Jetpack 2", "type": "sprite"},
        {"id": 761, "mp": True, "name": "MP Floor Jetpack 3", "type": "sprite"},
        {"id": 762, "mp": True, "name": "MP Floor Jetpack 4", "type": "sprite"},
        {"id": 790, "name": "Pistons Atomic Health 1", "type": "sprite"},
        {"id": 791, "name": "Pistons Atomic Health 2", "type": "sprite"},
        {"id": 792, "name": "Pistons Tunnel Pipebombs 1", "type": "sprite"},
        {"id": 793, "name": "Pistons Tunnel Pipebombs 2", "type": "sprite"},
        {"id": 835, "name": "Top Floor Shotgun", "type": "sprite"},
        {"id": 836, "mp": True, "name": "MP Floor RPG", "type": "sprite"},
        {"id": 837, "mp": True, "name": "MP Floor Devastator", "type": "sprite"},
        {"id": 838, "name": "Slime Hallway Tripmine 1", "type": "sprite"},
        {"id": 839, "name": "Slime Hallway Tripmine 2", "type": "sprite"},
        {"id": 867, "mp": True, "name": "MP Reactor Pipebombs", "type": "sprite"},
        {
            "id": 870,
            "mp": True,
            "name": "MP Floor Protective Boots 1",
            "type": "sprite",
        },
        {
            "id": 871,
            "mp": True,
            "name": "MP Floor Protective Boots 2",
            "type": "sprite",
        },
        {
            "id": 872,
            "mp": True,
            "name": "MP Floor Protective Boots 3",
            "type": "sprite",
        },
        {
            "id": 873,
            "mp": True,
            "name": "MP Floor Protective Boots 4",
            "type": "sprite",
        },
        {"id": 874, "name": "Red Room Steroids", "type": "sprite"},
        {"id": 875, "name": "Pistons Ledge Steroids", "type": "sprite"},
        {"id": 317, "name": "Secret Top of Vents", "type": "sector"},
        {"id": 374, "name": "Secret Pistons Tunnel", "type": "sector"},
        {"id": 378, "name": "Secret Pistons Tunnel Ledge", "type": "sector"},
        {"id": 384, "name": "Secret Pistons Chamber", "type": "sector"},
        {"id": 405, "name": "Secret Column", "type": "sector"},
        {"id": 409, "name": "Secret Timed Blade Room", "type": "sector"},
        {"id": 416, "name": "Secret Vents Wall", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
    must_dive = True

    def main_region(self) -> Region:
        r = self.rules
        ret = self.region(
            self.name,
            [
                "Start Night Vision Goggles",
                "Shotgun behind Babe",
                "Start Armor",
                "Start RPG",
                "Start Atomic Health",
                "Pistons Protective Boots",
                "MP Floor Jetpack 1",
                "MP Floor Jetpack 2",
                "MP Floor Jetpack 3",
                "MP Floor Jetpack 4",
                "MP Floor Protective Boots 1",
                "MP Floor Protective Boots 2",
                "MP Floor Protective Boots 3",
                "MP Floor Protective Boots 4",
                "MP Floor RPG",
                "MP Floor Devastator",
            ],
        )

        # can just use a piston to clip into the center, no crouch required
        pistons = self.region(
            "Pistons",
            [
                "Pistons Ledge Steroids",
                "Pistons Medkit",
                "Pistons Night Vision Goggles",
                "Pistons Chaingun",
                "Pistons Atomic Health 1",
                "Pistons Atomic Health 2",
                "Pistons Tripmine 1",
                "Pistons Tripmine 2",
                "Pistons Tripmine 3",
                "Secret Pistons Chamber",
                "Secret Pistons Tunnel",
                "Secret Pistons Tunnel Ledge",
                "Pistons Tunnel Pipebombs 1",
                "Pistons Tunnel Pipebombs 2",
            ],
        )
        # all of this stuff is on ledges
        self.connect(ret, pistons, r.jump)

        blade_pool = self.region(
            "Spinning Blade Pool",
            [
                "Underwater Pipebombs 1",
                "Underwater Pipebombs 2",
                "Secret Timed Blade Room",
                "Timed Room Freezethrower",
            ],
        )
        # Need to get to the elevator switch, which requires climbing on one of the ledges at least
        self.connect(pistons, blade_pool, r.can_dive)

        first_level = self.region(
            "First Level Platform",
            [
                "First Level Night Vision Goggles",
                "First Level Shrinker",
                "Column Armor",
                "Secret Column",
                "Secret Top of Vents",
                "Vents Atomic Health",
                "Secret Vents Wall",
                "Slime Hallway Tripmine 1",
                "Slime Hallway Tripmine 2",
                "Red Room Steroids",
                "Red Room Devastator",
                "Reactor Night Vision Goggles",
                "MP Reactor Pipebombs",
                "MP Reactor Holo Duke",
                "Top Floor Medkit",
                "Top Floor Shotgun",
            ],
        )
        self.connect(blade_pool, first_level, r.true)
        self.connect(ret, first_level, r.jetpack(100))
        self.restrict("Secret Vents Wall", r.explosives)
        # So the logic is correct if we find a way through the piston room without jump
        self.restrict("Secret Top of Vents", r.jump)
        self.restrict("Vents Atomic Health", r.jump)

        top_floor_ledge = self.region(
            "Top Floor Ledge",
            [
                "Top Ledge Atomic Health 1",
                "Top Ledge Atomic Health 2",
                "Top Ledge Jetpack",
            ],
        )
        self.connect(first_level, top_floor_ledge, r.can_sprint | r.jump)

        top_floor = self.region(
            "Top Floor", ["Top Floor Chaingun", "Top Floor Atomic Health", "Exit"]
        )
        # the full route only requires 50 jetpack fuel, the bypass to first floor uses about 90
        self.connect(
            first_level, top_floor, (r.can_dive & r.jetpack(50)) | r.jetpack(100)
        )

        return ret
