from BaseClasses import Region

from ..base_classes import D3DLevel


class E4L1(D3DLevel):
    name = "It's Impossible"
    levelnum = 0
    volumenum = 3
    keys = ["Blue", "Red"]
    location_defs = [
        {"id": 4, "name": "Basement Container Tripmine 1", "type": "sprite"},
        {"id": 47, "name": "Kitchen Freezer Freezethrower", "type": "sprite"},
        {"id": 53, "name": "Cave Night Vision Goggles", "type": "sprite"},
        {"id": 54, "name": "Upper Canyon Ledge Holo Duke", "type": "sprite"},
        {"id": 56, "name": "Red Basement Pipebombs", "type": "sprite"},
        {"id": 135, "name": "Red Key Card", "type": "sprite"},
        {"id": 136, "name": "Blue Key Card", "type": "sprite"},
        {"id": 149, "name": "Basement Container Tripmine 2", "type": "sprite"},
        {"id": 150, "name": "Basement Container Tripmine 3", "type": "sprite"},
        {"id": 151, "name": "Upper Canyon Ledge Pipebombs", "type": "sprite"},
        {
            "id": 152,
            "mp": True,
            "name": "MP Upper Canyon Ledge Steroids",
            "type": "sprite",
        },
        {"id": 170, "name": "Cave Atomic Health", "type": "sprite"},
        {"id": 192, "name": "Final Doors Atomic Health", "type": "sprite"},
        {"id": 373, "name": "Upstairs Computer RPG", "type": "sprite"},
        {"id": 407, "name": "Bathroom Secret Medkit", "type": "sprite"},
        {"id": 419, "name": "Briefing Room Armor", "type": "sprite"},
        {"id": 539, "name": "Briefing Room Shotgun", "type": "sprite"},
        {"id": 540, "name": "Bathroom Chaingun", "type": "sprite"},
        {
            "id": 544,
            "mp": True,
            "name": "MP Outside Area Ledge Shotgun",
            "type": "sprite",
        },
        {
            "id": 545,
            "mp": True,
            "name": "MP Outside Area Ledge Chaingun",
            "type": "sprite",
        },
        {"id": 562, "name": "Briefing Room Pipebombs", "type": "sprite"},
        {"id": 563, "name": "Kitchen Conveyer Atomic Health", "type": "sprite"},
        {"id": 633, "name": "Kitchen Secret Shrinker", "type": "sprite"},
        {"id": 634, "name": "Kitchen Secret Armor", "type": "sprite"},
        {"id": 655, "name": "Final Doors Devastator", "type": "sprite"},
        {"id": 674, "name": "Exit Pipebombs", "type": "sprite"},
        {"id": 839, "name": "Barracks Bed Steroids", "type": "sprite"},
        {"id": 840, "name": "Barracks Bed Jetpack", "type": "sprite"},
        {"id": 116, "name": "Secret Upstairs Computer", "type": "sector"},
        {"id": 221, "name": "Secret Final Doors", "type": "sector"},
        {"id": 232, "name": "Secret Kitchen Freezer", "type": "sector"},
        {"id": 270, "name": "Secret Cave", "type": "sector"},
        {"id": 274, "name": "Secret Bathroom", "type": "sector"},
        {"id": 388, "name": "Secret Barracks Bed", "type": "sector"},
        {"id": 414, "name": "Secret Upper Canyon Ledge", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]

    def main_region(self) -> Region:
        r = self.rules
        ret = self.region(
            self.name,
            [
                "Secret Barracks Bed",
                "Barracks Bed Steroids",
                "Barracks Bed Jetpack",
                "Blue Key Card",
                "Bathroom Chaingun",
                "Secret Kitchen Freezer",
                "Kitchen Freezer Freezethrower",
                "Secret Cave",
                "Cave Night Vision Goggles",
                "Cave Atomic Health",
                "Briefing Room Pipebombs",
                "Briefing Room Armor",
            ],
        )

        behind_desk = self.region(
            "Behind Briefing Room Desk",
            [
                "Briefing Room Shotgun",
            ],
        )
        # Can walk over the desk with precise diagonal movement
        self.connect(ret, behind_desk, r.jump | r.difficulty("medium"))

        upper_canyon = self.region(
            "Upper Canyon Ledge",
            [
                "MP Upper Canyon Ledge Steroids",
                "MP Outside Area Ledge Shotgun",
                "MP Outside Area Ledge Chaingun",
                "Upper Canyon Ledge Holo Duke",
                "Upper Canyon Ledge Pipebombs",
                "Secret Upper Canyon Ledge",
            ],
        )
        self.connect(ret, upper_canyon, r.jump)

        bathroom_secret = self.region(
            "Bathroom Secret Region",
            [
                "Secret Bathroom",
                "Bathroom Secret Medkit",
            ],
        )
        self.connect(ret, bathroom_secret, r.jump)

        upper_kitchen_secret = self.region(
            "Upper Kitchen Secret",
            [
                "Kitchen Secret Shrinker",
                "Kitchen Secret Armor",
            ],
        )
        self.connect(ret, upper_kitchen_secret, r.jump)

        basement_container = self.region(
            "Basement Container",
            [
                "Basement Container Tripmine 1",
                "Basement Container Tripmine 2",
                "Basement Container Tripmine 3",
            ],
        )
        # Door clipping on top of the container and SR50
        self.connect(ret, basement_container, r.jump | r.difficulty("hard"))

        kitchen_conveyer = self.region(
            "Behind Kitchen Conveyer",
            [
                "Kitchen Conveyer Atomic Health",
            ],
        )
        self.connect(ret, kitchen_conveyer, r.jump | r.can_dive)

        blue_key_area = self.region(
            "Blue Key Room",
            [
                "Red Key Card",
                "Secret Upstairs Computer",
                "Upstairs Computer RPG",
            ],
        )
        self.connect(ret, blue_key_area, self.blue_key)

        janitor_closet = self.region(
            "Janitor Closet",
            [
                "Red Basement Pipebombs",
            ],
        )
        self.connect(ret, janitor_closet, self.red_key)

        mission_impossible = self.region(
            "Mission Impossible Room",
            [
                "Secret Final Doors",
                "Final Doors Atomic Health",
                "Final Doors Devastator",
            ],
        )
        # Triggering the tripmines requires 100 health and precise movement
        # Without saving this would need to be extreme logic
        self.connect(
            janitor_closet,
            mission_impossible,
            r.can_jump & (r.explosives | (r.can_sprint & r.difficulty("hard"))),
        )

        exit_region = self.region(
            "Exit Region",
            [
                "Exit Pipebombs",
                "Exit",
            ],
        )
        self.connect(mission_impossible, exit_region, r.explosives)
        return ret
