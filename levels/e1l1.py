from BaseClasses import Region

from ..base_classes import D3DLevel


class E1L1(D3DLevel):
    name = "Hollywood Holocaust"
    levelnum = 0
    volumenum = 0
    keys = ["Red"]
    location_defs = [
        {"name": "Exit Ledge Night Vision Goggles", "id": 25, "type": "sprite"},
        {"name": "Bachelor RPG", "id": 26, "type": "sprite"},
        {"name": "Bachelor Pipebombs", "id": 27, "type": "sprite"},
        {"name": "Elevator Night Vision", "id": 40, "type": "sprite"},
        {"name": "Bachelor Shotgun", "id": 44, "type": "sprite"},
        {"name": "Bachelor Chaingun", "id": 45, "type": "sprite"},
        {"name": "MP Start Shotgun", "id": 81, "type": "sprite", "mp": True},
        {"name": "Billboard RPG", "id": 82, "type": "sprite"},
        {"name": "MP Chaingun behind Screen", "id": 111, "type": "sprite", "mp": True},
        {"name": "Outside Ledge Atomic Health", "id": 170, "type": "sprite"},
        {"name": "Cash Register Atomic Health", "id": 209, "type": "sprite"},
        {"name": "Arcade Holo Duke", "id": 297, "type": "sprite"},
        {"name": "Cash Register Shotgun", "id": 337, "type": "sprite"},
        {"name": "Toilet Medkit", "id": 376, "type": "sprite"},
        {"name": "Projector Atomic Health", "id": 400, "type": "sprite"},
        {"name": "Vent Holo Duke", "id": 411, "type": "sprite"},
        {"name": "MP Exit Shotgun", "id": 421, "type": "sprite", "mp": True},
        {"name": "Projector Secret RPG", "id": 431, "type": "sprite"},
        {"name": "Jetpack behind Screen", "id": 447, "type": "sprite"},
        {"name": "Red Key Card", "id": 451, "type": "sprite"},
        {"name": "Poster Steroids", "id": 527, "type": "sprite"},
        {"name": "MP Entrance Chaingun", "id": 530, "type": "sprite", "mp": True},
        {"name": "Cinema Armor", "id": 532, "type": "sprite"},
        {"name": "MP Red Door Pipebombs", "id": 535, "type": "sprite", "mp": True},
        {"name": "Cash Register Alcove Armor", "id": 546, "type": "sprite"},
        {"name": "Projector Steroids", "id": 595, "type": "sprite"},
        {"name": "Elevator Pipebombs", "id": 632, "type": "sprite"},
        {"name": "Jetpack above Exit", "id": 633, "type": "sprite"},
        {"name": "Secret: Behind the Screen", "id": 149, "type": "sector"},
        {"name": "Secret: Projector Hidden Room", "id": 154, "type": "sector"},
        {"name": "Secret: Hidden Apartment", "id": 197, "type": "sector"},
        {"name": "Secret: Projector Security Room", "id": 211, "type": "sector"},
        {"name": "Secret: Behind Poster", "id": 238, "type": "sector"},
        {"name": "Secret: Cash Register Alcove", "id": 241, "type": "sector"},
        {"name": "Secret: Bachelor Apartment", "id": 249, "type": "sector"},
        {"name": "Secret: Below Billboard", "id": 290, "type": "sector"},
        {"name": "Exit", "id": 0, "type": "exit"},
    ]

    def main_region(self) -> Region:
        r = self.rules
        ret = self.region(
            self.name,
            [
                "MP Start Shotgun",
                "Cinema Armor",
                "Cash Register Alcove Armor",
                "Cash Register Shotgun",
                "Cash Register Atomic Health",
                "Red Key Card",
                "Projector Steroids",
                "Toilet Medkit",
                "Secret: Cash Register Alcove",
                "Secret: Projector Security Room",
                "Arcade Holo Duke",
                "MP Entrance Chaingun",
                "Vent Holo Duke",
            ],
        )
        self.restrict("Vent Holo Duke", r.jump & r.explosives)

        apartment = self.region(
            "Apartments",
            [
                "Billboard RPG",
                "Outside Ledge Atomic Health",
                "Poster Steroids",
                "Secret: Hidden Apartment",
                "Secret: Behind Poster",
                "Secret: Below Billboard",
            ],
        )
        self.connect(ret, apartment, r.jump)

        cinema_ledges = self.region(
            "Cinema Ledges",
            [
                "Elevator Night Vision",
                "Elevator Pipebombs",
                "Projector Atomic Health",
                "Projector Secret RPG",
                "Secret: Projector Hidden Room",
            ],
        )
        self.connect(ret, cinema_ledges, r.jump)

        exit_ledge = self.region(
            "Exit Ledge",
            [
                "Exit Ledge Night Vision Goggles",
                "Exit",
                "MP Exit Shotgun",
                "MP Red Door Pipebombs",
            ],
        )
        self.connect(
            ret,
            exit_ledge,
            (r.difficulty("medium") & r.jump) | r.jetpack(50) | self.red_key,
        )

        bachelor_secret = self.region(
            "Bachelor Apartment",
            [
                "Bachelor RPG",
                "Bachelor Pipebombs",
                "Bachelor Shotgun",
                "Bachelor Chaingun",
                "Secret: Bachelor Apartment",
            ],
        )
        self.connect(exit_ledge, bachelor_secret, r.jump)

        behind_screen = self.region(
            "Behind the Screen",
            [
                "Secret: Behind the Screen",
                "Jetpack behind Screen",
                "MP Chaingun behind Screen",
            ],
        )
        self.connect(
            exit_ledge, behind_screen, r.difficulty("medium")
        )  # Can just walk off the ledge
        self.connect(ret, behind_screen, (r.can_jump & r.explosives) | r.jetpack(50))

        top_of_building = self.region(f"Top of Building")
        self.add_locations(["Jetpack above Exit"], top_of_building)
        self.connect(ret, top_of_building, r.jetpack(200))
        self.connect(exit_ledge, top_of_building, r.crouch_jump)  # glitched logic
        return ret
