from BaseClasses import Region

from ..base_classes import D3DLevel


class E4L7(D3DLevel):
    name = "XXX-Stacy"
    levelnum = 6
    volumenum = 3
    keys = ["Red", "Blue"]
    location_defs = [
        {"id": 8, "name": "Crusher Scuba Gear", "type": "sprite"},
        {"id": 29, "name": "Blue Holo Duke", "type": "sprite"},
        {"id": 34, "name": "Crate Freezethrower", "type": "sprite"},
        {"id": 35, "mp": True, "name": "MP Front Jetpack", "type": "sprite"},
        {"id": 37, "name": "Blue Apt. Pipebombs", "type": "sprite"},
        {
            "name": "Printer Trashcan Pipebombs",
            "id": 39,
            "type": "sprite",
            "sprite_type": "trashcan",
        },
        {"id": 83, "name": "Front Upper Armor", "type": "sprite"},
        {"id": 84, "name": "Front Upper Atomic Health", "type": "sprite"},
        {"id": 110, "name": "Crusher RPG", "type": "sprite"},
        {"id": 112, "name": "Crusher Medkit", "type": "sprite"},
        {"id": 165, "name": "Blue Key Card", "type": "sprite"},
        {"id": 166, "name": "Cola Tripmine 1", "type": "sprite"},
        {"id": 167, "name": "Cola Tripmine 2", "type": "sprite"},
        {"id": 170, "name": "Blue Devastator", "type": "sprite"},
        {"id": 176, "name": "Outside Pipebombs", "type": "sprite"},
        {"id": 177, "name": "Front Chaingun", "type": "sprite"},
        {"id": 186, "name": "Front Protective Boots", "type": "sprite"},
        {"id": 195, "name": "Blue Secret Shrinker", "type": "sprite"},
        {"id": 207, "mp": True, "name": "MP Outside Shotgun", "type": "sprite"},
        {"id": 216, "name": "Blue Atomic Health", "type": "sprite"},
        {"id": 245, "name": "Blue Night Vision Goggles", "type": "sprite"},
        {"id": 322, "name": "Blue Medkit", "type": "sprite"},
        {"id": 331, "name": "Front Steroids", "type": "sprite"},
        {"id": 365, "mp": True, "name": "MP Blue Jetpack", "type": "sprite"},
        {"id": 372, "name": "Red Key Card", "type": "sprite"},
        {"id": 420, "name": "Blue Shotgun", "type": "sprite"},
        {
            "name": "Blue Apt. Trashcan Devastator",
            "id": 528,
            "type": "sprite",
            "sprite_type": "trashcan",
        },
        {"id": 591, "name": "Blue Apt. RPG", "type": "sprite"},
        {"id": 65, "name": "Secret Blue Area", "type": "sector"},
        {"id": 232, "name": "Secret Crate", "type": "sector"},
        {"id": 265, "name": "Secret Blue Appartment", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
    must_dive = True

    def main_region(self) -> Region:
        r = self.rules
        ret = self.region(
            self.name,
            [
                "MP Outside Shotgun",
                "Outside Pipebombs",
                "Front Protective Boots",
                "Front Chaingun",
                "Front Steroids",
                "MP Front Jetpack",
                "Printer Trashcan Pipebombs",
            ],
        )

        front_upper = self.region(
            "Front Upper",
            [
                "Front Upper Armor",
                "Front Upper Atomic Health",
                "Blue Key Card",
            ],
        )
        self.connect(ret, front_upper, r.jump)

        crate_secret = self.region(
            "Crate Secret",
            [
                "Secret Crate",
                "Crate Freezethrower",
            ],
        )
        # can't fit with just jetpack
        self.connect(ret, crate_secret, r.can_jump)

        blue_key_area = self.region(
            "Blue Key Area",
            [
                "Blue Medkit",
                "Blue Shotgun",
                "MP Blue Jetpack",
                "Red Key Card",
                "Blue Holo Duke",
                "Blue Devastator",
                "Blue Atomic Health",
            ],
        )
        # One way, cant go back without crouching
        self.connect(
            ret, blue_key_area, (self.blue_key & r.jump) | (r.crouch_jump & r.steroids)
        )

        blue_apt = self.region(
            "Blue Apt.",
            [
                "Secret Blue Appartment",
                "Blue Apt. RPG",
                "Blue Apt. Pipebombs",
                "Blue Apt. Trashcan Devastator",
            ],
        )
        # SR50 jump possible for reaching the apartment
        self.connect(blue_key_area, blue_apt, (r.difficulty("Hard") & r.can_jump) | r.jump)

        blue_dive = self.region(
            "Blue Dive Area",
            [
                "Blue Night Vision Goggles",
            ],
        )
        # Crouchjump through window skips dive and jetpack requirement
        self.connect(blue_key_area, blue_dive, r.can_dive | r.crouch_jump)

        cola_machine = self.region(
            "Blue Dive Area",
            [
                "Cola Tripmine 1",
                "Cola Tripmine 2",
            ],
        )
        self.connect(blue_dive, cola_machine, r.jump)

        blue_secret = self.region(
            "Secret Blue Area",
            [
                "Blue Secret Shrinker",
                "Secret Blue Area",
            ],
        )
        # Clip on top of trashcan and strafe around to secret
        self.connect(blue_dive, blue_secret, r.jump | (r.difficulty("Hard")))

        dive_crusher = self.region(
            "Dive Crusher",
            [
                "Crusher Scuba Gear",
                "Crusher RPG",
                "Crusher Medkit",
            ],
        )
        self.connect(blue_dive, dive_crusher, r.can_dive)

        red_key_area = self.region(
            "Red Key Area",
            [
                "Exit",
            ],
        )
        self.connect(blue_dive, red_key_area, self.red_key)
        return ret
