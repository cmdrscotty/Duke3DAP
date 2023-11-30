from BaseClasses import Region

from ..base_classes import D3DLevel


class E1L4(D3DLevel):
    name = "Toxic Dump"
    levelnum = 3
    volumenum = 0
    keys = ["Blue", "Red"]
    location_defs = [
        {"name": "Gear Room Secret Scuba Gear", "id": 59, "type": "sprite"},
        {"name": "Gear Room Secret Armor", "id": 60, "type": "sprite"},
        {"name": "Canyon Steroids", "id": 67, "type": "sprite"},
        {
            "name": "Secret Alcove Holo Duke outside Submarine",
            "id": 86,
            "type": "sprite",
        },
        {"name": "Red Key Card", "id": 210, "type": "sprite"},
        {"name": "Blue Key Card", "id": 247, "type": "sprite"},
        {"name": "Guard Tower Chaingun", "id": 274, "type": "sprite"},
        {"name": "MP Sewage Chaingun", "id": 293, "type": "sprite", "mp": True},
        {"name": "Toxic Waste Belt Scuba Gear", "id": 294, "type": "sprite"},
        {"name": "Sewage Atomic Health", "id": 301, "type": "sprite"},
        {"name": "Gear Room Medkit", "id": 625, "type": "sprite"},
        {"name": "Underwater Canyon Night Vision Goggles", "id": 626, "type": "sprite"},
        {"name": "Submarine Return Cave Atomic Health", "id": 741, "type": "sprite"},
        {"name": "Sewage Protective Boots", "id": 899, "type": "sprite"},
        {"name": "MP Waterfall Shotgun", "id": 905, "type": "sprite", "mp": True},
        {"name": "Underwater Canyon Chaingun", "id": 913, "type": "sprite"},
        {"name": "Underwater Gate RPG", "id": 929, "type": "sprite"},
        {"name": "Underwater Scuba Gear", "id": 957, "type": "sprite"},
        {"name": "RPG near Blue Key Card", "id": 962, "type": "sprite"},
        {"name": "Underwater Secret Pipebombs 1", "id": 969, "type": "sprite"},
        {"name": "Underwater Secret Pipebombs 2", "id": 970, "type": "sprite"},
        {"name": "Underwater Secret Atomic Health", "id": 971, "type": "sprite"},
        {"name": "Right Cylinder Atomic Health", "id": 987, "type": "sprite"},
        {"name": "Underwater Medkit", "id": 988, "type": "sprite"},
        {"name": "Cylinders Armor", "id": 991, "type": "sprite"},
        {"name": "Underwater Hallway Holo Duke", "id": 1013, "type": "sprite"},
        {"name": "Underwater Canyon Pipebombs", "id": 1014, "type": "sprite"},
        {"name": "Canyon Secret Scuba Gear", "id": 1050, "type": "sprite"},
        {"name": "Submarine Medkit", "id": 1060, "type": "sprite"},
        {"name": "Submarine Atomic Health", "id": 1061, "type": "sprite"},
        {"name": "Submarine Armor", "id": 1062, "type": "sprite"},
        {"name": "Shotgun near Red Key Card", "id": 1069, "type": "sprite"},
        {"name": "Left Cylinder Atomic Health 2", "id": 1070, "type": "sprite"},
        {"name": "Left Cylinder Atomic Health 1", "id": 1071, "type": "sprite"},
        {"name": "Canyon Dark Cave Shotgun", "id": 1074, "type": "sprite"},
        {"name": "Canyon Dark Cave Medkit", "id": 1075, "type": "sprite"},
        {"name": "Sewage Secret Alcove Atomic Health 1", "id": 1079, "type": "sprite"},
        {"name": "Sewage Secret Alcove Atomic Health 2", "id": 1080, "type": "sprite"},
        {"name": "Canyon RPG", "id": 1085, "type": "sprite"},
        {"name": "Submarine Return Cave 1", "id": 88, "type": "sector"},
        {"name": "Submarine Return Cave 2", "id": 89, "type": "sector"},
        {"name": "Submarine Return Cave 3", "id": 90, "type": "sector"},
        {"name": "Waterfall Secret Teleporter", "id": 184, "type": "sector"},
        {"name": "Underwater Secret Cave", "id": 267, "type": "sector"},
        {"name": "Guard Tower", "id": 274, "type": "sector"},
        {"name": "Secret Alcove near Blue Key Card", "id": 330, "type": "sector"},
        {"name": "Sewage Secret Alcove", "id": 331, "type": "sector"},
        {"name": "Toxic Waste Belt Hidden Alcove", "id": 418, "type": "sector"},
        {"name": "Canyon Secret Wall", "id": 421, "type": "sector"},
        {"name": "Top of Submarine", "id": 430, "type": "sector"},
        {"name": "Left Cylinder", "id": 435, "type": "sector"},
        {"name": "Canyon Dark Cave", "id": 453, "type": "sector"},
        {"name": "Secret Exit Area", "id": 465, "type": "sector"},
        {"name": "Exit", "id": 0, "type": "exit"},
        {"name": "Secret Exit", "id": 6, "type": "exit"},
    ]
    events = ["Underwater Gate"]

    def main_region(self) -> Region:
        r = self.rules
        ret = self.region(self.name)

        submarine = self.region(
            "Submarine",
            [
                "Underwater Scuba Gear",
                "Underwater Medkit",
                "RPG near Blue Key Card",
                "Blue Key Card",
                "Secret Alcove Holo Duke outside Submarine",
                "Secret Alcove near Blue Key Card",
            ],
        )
        # Can get out of the submarine in just 150 units. Relevant to note for later dive logic
        self.connect(ret, submarine, r.can_dive)
        self.restrict(
            self.get_location("Secret Alcove Holo Duke outside Submarine"), r.jump
        )
        self.restrict(self.get_location("Secret Alcove near Blue Key Card"), r.jump)

        submarine_secret = self.region(
            "Submarine Secret",
            [
                "Top of Submarine",
                "Submarine Medkit",
                "Submarine Atomic Health)",
                "Submarine Armor",
            ],
        )
        # Can run off the Blue Key Card ledge
        self.connect(submarine, submarine_secret, r.can_sprint or r.jump)

        underwater_cave = self.region(
            "Submarine Secret",
            [
                "Underwater Secret Atomic Health",
                "Underwater Secret Pipebombs 2",
                "Underwater Secret Pipebombs 1",
                "Underwater Secret Cave",
            ],
        )
        self.connect(submarine, underwater_cave, r.explosives)

        facility = self.region(
            "Waste Facility",
            [
                "Guard Tower",
                "Guard Tower Chaingun",
                "Toxic Waste Belt Scuba Gear",
                "Shotgun near Red Key Card",
                "Red Key Card",
                "Toxic Waste Belt Hidden Alcove",
                "Cylinders Armor",
                "Right Cylinder Atomic Health",
            ],
        )
        self.connect(submarine, facility, self.blue_key)

        cylinders = self.region(
            "Waste Storage Cylinders",
            [
                "Left Cylinder",
                "Left Cylinder Atomic Health 2",
                "Left Cylinder Atomic Health 1",
            ],
        )
        self.connect(facility, cylinders, r.jump)

        flooded_area = self.region(
            "Flooded Area",
            [
                "Underwater Canyon Night Vision Goggles",
                "Canyon Steroids",
                # Can shoot mine to unlock
                "Underwater Canyon Chaingun",
            ],
        )
        self.connect(
            facility,
            flooded_area,
            (
                (r.can_shrink & self.red_key)
                | (r.glitched & r.crouch_jump)
                # dive capacity logic, need 150 to exit sub at start
                & (
                    r.dive(500)
                    | (r.difficulty("medium") & r.dive(250))
                    | (r.difficulty("hard") & r.dive(150))
                )
            ),
        )

        # Cost of rising the water level and getting to the top of the canyon with scuba gear remaining, from start
        second_dive = (
            r.dive(1000)
            | (r.difficulty("medium") & r.dive(750))
            | (r.difficulty("hard") & (r.dive(350) | (r.can_sprint & r.dive(300))))
        )

        canyon_far = self.region(
            "Canyon Far Side",
            [
                "Underwater Gate",
                "Canyon RPG",
                "Canyon Secret Wall",
                "Canyon Secret Scuba Gear",
            ],
        )
        self.connect(flooded_area, canyon_far, r.can_sprint or r.jump)
        self.restrict(self.get_location("Canyon Secret Scuba Gear"), r.can_crouch)
        self.restrict(self.get_location("Canyon Secret Wall"), r.can_crouch)

        canyon_return1 = self.region(
            "Canyon Return Path 1", ["Submarine Return Cave 1"]
        )
        self.connect(canyon_far, canyon_return1, r.explosives)
        canyon_return2 = self.region(
            "Canyon Return Path 2",
            ["Submarine Return Cave 2", "Submarine Return Cave Atomic Health"],
        )
        self.connect(canyon_return1, canyon_return2, r.explosives_count(2))
        canyon_return3 = self.region(
            "Canyon Return Path 1", ["Submarine Return Cave 3"]
        )
        self.connect(canyon_return2, canyon_return3, r.explosives_count(3))

        canyon_dark_area = self.region(
            "Canyon Dark Area",
            ["Canyon Dark Cave", "Canyon Dark Cave Medkit", "Canyon Dark Cave Shotgun"],
        )
        self.connect(flooded_area, canyon_dark_area, r.jump)

        deep_water = self.region(
            "Deep Water Area",
            [
                "Underwater Hallway Holo Duke",
                "Gear Room Medkit",
                "Gear Room Secret Scuba Gear",
                "Gear Room Secret Armor",
                "MP Waterfall Shotgun",
                "Underwater Gate RPG",
                "Underwater Canyon Pipebombs",
            ],
        )

        self.connect(
            flooded_area, deep_water, self.event("Underwater Gate") & second_dive
        )

        # Cost of rising the water level and getting through the moving gears
        third_dive = (
            r.dive(1900)
            | (r.difficulty("medium") & r.dive(1250))
            | (r.difficulty("hard") & (r.dive(950) | (r.can_sprint & r.dive(800))))
        )

        top_of_waterfall = self.region(
            "Top of Waterfall", ["Waterfall Secret Teleporter"]
        )
        self.connect(deep_water, top_of_waterfall, third_dive)
        self.restrict(self.get_location("Waterfall Secret Teleporter"), r.explosives)

        moving_platforms = self.region("Moving Platforms", ["Underwater Gate RPG"])
        self.connect(top_of_waterfall, moving_platforms)

        top_of_sewer = self.region(
            "Sewers Top",
            [
                "MP Sewage Chaingun",
                "Sewage Atomic Health",
                "Sewage Secret Alcove",
                "Sewage Secret Alcove Atomic Health 1",
                "Sewage Secret Alcove Atomic Health 2",
                "Sewage Protective Boots",
            ],
        )
        self.connect(
            moving_platforms, top_of_sewer, r.jump
        )  # There might be a way to get off the water fall without jump

        secret_exit = self.region(
            "Secret Exit Area", ["Secret Exit Area", "Secret Exit"]
        )
        self.connect(top_of_sewer, secret_exit, r.explosives)

        exit_area = self.region("Exit Area", ["Exit"])
        # Secret teleporter in canyon wall
        self.connect(flooded_area, exit_area, r.jump)
        self.connect(
            secret_exit,
            exit_area,
            r.explosives & (r.can_sprint | r.can_jump | r.jetpack(250)),
        )
        # sprint might work with protective boots
        self.connect(
            exit_area, top_of_sewer, r.can_crouch & (r.can_jump | r.jetpack(500))
        )
        # respect scuba use up to here on this return path from teleporter
        self.connect(top_of_sewer, moving_platforms, second_dive)
        self.connect(moving_platforms, top_of_waterfall, r.jetpack(100))
        return ret
