from BaseClasses import Region

from ..base_classes import D3DLevel


class E2L1(D3DLevel):
    name = "Spaceport"
    levelnum = 0
    volumenum = 1
    keys = ["Blue", "Red"]
    location_defs = [
        {
            "name": "Underwater Night Vision Goggles",
            "id": 31,
            "type": "sprite",
        },
        {"name": "Vent Pipebombs", "id": 40, "type": "sprite"},
        {"name": "Elevator Armor", "id": 54, "type": "sprite"},
        {"name": "Elevator Shrinker", "id": 58, "type": "sprite"},
        {
            "name": "MP Elevator Corner Freezethrower",
            "id": 60,
            "type": "sprite",
            "density": 5,
        },
        {"name": "Middle Floor Jetpack", "id": 69, "type": "sprite"},
        {"name": "Attic Night Vision Goggles", "id": 81, "type": "sprite"},
        {"name": "Underwater Jetpack", "id": 110, "type": "sprite"},
        {"name": "Bottom Floor Medkit", "id": 155, "type": "sprite"},
        {"name": "Start Shotgun", "id": 156, "type": "sprite"},
        {"name": "Bottom Floor Scuba Gear", "id": 165, "type": "sprite"},
        {"name": "Blue Key Card", "id": 180, "type": "sprite"},
        {"name": "Middle Floor Pipebombs", "id": 235, "type": "sprite"},
        {"name": "Underwater Atomic Health 1", "id": 276, "type": "sprite"},
        {"name": "Underwater Atomic Health 2", "id": 277, "type": "sprite"},
        {"name": "Bottom Floor Armor", "id": 280, "type": "sprite"},
        {"name": "Top Floor Atomic Health", "id": 289, "type": "sprite"},
        {"name": "Red Key Card", "id": 318, "type": "sprite"},
        {"name": "Bottom Floor Holo Duke", "id": 367, "type": "sprite"},
        {"name": "Space Shuttle RPG", "id": 373, "type": "sprite"},
        {"name": "Underwater Chaingun", "id": 374, "type": "sprite"},
        {"name": "MP Attic Tripmine 1", "id": 385, "type": "sprite", "density": 5},
        {"name": "MP Attic Tripmine 2", "id": 386, "type": "sprite", "density": 5},
        {"name": "MP Attic Tripmine 3", "id": 387, "type": "sprite", "density": 5},
        {"name": "MP Start Armor", "id": 396, "type": "sprite", "density": 5},
        {"name": "Top Floor Devastator", "id": 399, "type": "sprite"},
        {"name": "Middle Room Atomic Health", "id": 420, "type": "sprite"},
        {"name": "Space Shuttle Steroids", "id": 422, "type": "sprite"},
        {"name": "Monitor Wall Atomic Health", "id": 448, "type": "sprite"},
        {"name": "Secret Top Floor", "id": 4, "type": "sector"},
        {"name": "Secret Timed Alcove", "id": 275, "type": "sector"},
        {"name": "Secret Elevator Corner", "id": 304, "type": "sector"},
        {"name": "Secret Ventilation Shaft", "id": 321, "type": "sector"},
        {"name": "Secret Shrinker Room", "id": 334, "type": "sector"},
        {"name": "Secret Monitor Wall", "id": 354, "type": "sector"},
        {"name": "Exit", "id": 0, "type": "exit"},
    ]
    must_dive = True

    def main_region(self) -> Region:
        r = self.rules
        ret = self.region(
            self.name,
            [
                "Space Shuttle RPG",
                "Space Shuttle Steroids",
                "Start Shotgun",
                "Secret Monitor Wall",
                "Monitor Wall Atomic Health",
                "Bottom Floor Holo Duke",
                "Bottom Floor Armor",
                "Bottom Floor Medkit",
                "Bottom Floor Scuba Gear",
                "Blue Key Card",
            ],
        )

        start_ledges = self.region(
            "Early Ledges",
            [
                "MP Start Armor",
                "Secret Timed Alcove",
                "Secret Ventilation Shaft",
                "Vent Pipebombs",
            ],
        )
        self.connect(ret, start_ledges, r.jump)

        hidden_water_passage = self.region(
            "Hidden Water Passage",
            ["Underwater Chaingun", "Underwater Night Vision Goggles"],
        )
        self.connect(ret, hidden_water_passage, r.can_dive)

        middle_floor = self.region(
            "Middle Floor",
            [
                "Middle Floor Pipebombs",
                "Secret Shrinker Room",
                "Elevator Shrinker",
                "Elevator Armor",
                "Exit",
                "Middle Floor Jetpack",
            ],
        )
        self.connect(ret, middle_floor, self.blue_key)
        self.restrict("Exit", self.red_key)
        self.restrict("Middle Floor Jetpack", r.jump)

        middle_floor_ledge = self.region(
            "Middle Floor Jetpack Ledge",
            [
                "Middle Room Atomic Health",
                "Secret Elevator Corner",
                "MP Elevator Corner Freezethrower",
            ],
        )
        self.connect(middle_floor, middle_floor_ledge, r.jetpack(50))

        pool = self.region(
            "Underwater Section",
            [
                "Red Key Card",
                "Underwater Jetpack",
                "Underwater Atomic Health 1",
                "Underwater Atomic Health 2",
            ],
        )
        # Need to get to the second floor to disable force field
        self.connect(middle_floor, pool, r.jump & r.can_dive)

        upper_floor = self.region(
            "Top Floor",
            ["Secret Top Floor", "Top Floor Atomic Health", "Top Floor Devastator"],
        )
        self.connect(middle_floor, upper_floor, r.jetpack(75))

        attic = self.region(
            "Attic",
            [
                "MP Attic Tripmine 1",
                "MP Attic Tripmine 2",
                "MP Attic Tripmine 3",
                "Attic Night Vision Goggles",
            ],
        )
        self.connect(middle_floor, attic, r.jetpack(100))

        return ret
