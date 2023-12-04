from BaseClasses import Region

from ..base_classes import D3DLevel


class E4L11(D3DLevel):
    name = "Area 51"
    levelnum = 10
    volumenum = 3
    keys = ["Red", "Blue", "Yellow"]
    location_defs = [
        {"id": 50, "name": "UFO Atomic Health", "type": "sprite"},
        {"id": 90, "name": "Vent Entrance Pipebombs", "type": "sprite"},
        {"id": 94, "mp": True, "name": "MP Outside Pipebombs", "type": "sprite"},
        {"id": 109, "mp": True, "name": "MP Blue Chaingun", "type": "sprite"},
        {"id": 112, "mp": True, "name": "MP Red Steroids", "type": "sprite"},
        {"id": 198, "name": "Elevator Drop Devastator", "type": "sprite"},
        {"id": 234, "name": "Cave Night Vision Goggles", "type": "sprite"},
        {"id": 252, "name": "Blue Night Vision Goggles", "type": "sprite"},
        {"id": 254, "name": "Outside Pipebombs", "type": "sprite"},
        {"id": 258, "name": "Crate Holo Duke", "type": "sprite"},
        {"id": 275, "name": "Lake Pipebombs", "type": "sprite"},
        {"id": 294, "name": "Blue Tripmine 1", "type": "sprite"},
        {"id": 295, "name": "Blue Tripmine 2", "type": "sprite"},
        {"id": 297, "name": "Blue Holo Duke", "type": "sprite"},
        {"id": 298, "name": "Symbol Atomic Health", "type": "sprite"},
        {"id": 299, "name": "Corner Steroids", "type": "sprite"},
        {"id": 300, "name": "Blue Tripmine 3", "type": "sprite"},
        {"id": 301, "name": "Blue Medkit", "type": "sprite"},
        {"id": 302, "mp": True, "name": "MP Freezer Atomic Health", "type": "sprite"},
        {"id": 304, "name": "Crate Armor", "type": "sprite"},
        {"id": 306, "name": "Tele Cave Shotgun", "type": "sprite"},
        {"id": 308, "name": "Vent Secret Atomic Health", "type": "sprite"},
        {"id": 311, "name": "Blue Key Card", "type": "sprite"},
        {"id": 335, "name": "Bunker Chaingun", "type": "sprite"},
        {"id": 469, "name": "Red Key Card", "type": "sprite"},
        {"id": 513, "name": "Vent Entrance Armor", "type": "sprite"},
        {"id": 558, "name": "Conveyer Jetpack", "type": "sprite"},
        {"id": 560, "name": "Conveyer Shrinker", "type": "sprite"},
        {"id": 561, "mp": True, "name": "MP Cave Jetpack", "type": "sprite"},
        {"id": 568, "name": "Bridge RPG", "type": "sprite"},
        {"id": 584, "name": "Red Shotgun", "type": "sprite"},
        {"id": 610, "name": "Elevator Drop Medkit", "type": "sprite"},
        {"id": 637, "name": "Crate Scuba Gear", "type": "sprite"},
        {"id": 656, "name": "Table Freezethrower", "type": "sprite"},
        {"id": 690, "name": "Yellow Key Card", "type": "sprite"},
        {"id": 50, "name": "Secret Symbol", "type": "sector"},
        {"id": 54, "name": "Secret Corner", "type": "sector"},
        {"id": 82, "name": "Secret Crate", "type": "sector"},
        {"id": 293, "name": "Secret Vent", "type": "sector"},
        {"id": 337, "name": "Secret Bridge", "type": "sector"},
        {"id": 440, "name": "Secret Lake", "type": "sector"},
        {"id": 574, "name": "Secret UFO", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]

    def main_region(self) -> Region:
        r = self.rules
        ret = self.region(
            self.name,
            [
                "MP Outside Pipebombs",
                "Outside Pipebombs",
            ],
        )

        second_area = self.region(
            "Second Area",
            [
                "Bunker Chaingun",
            ],
        )
        self.connect(ret, second_area, r.jetpack(50) | r.explosives)

        bridge_secret = self.region(
            "Secret Bridge",
            [
                "Secret Bridge",
                "Bridge RPG",
            ],
        )
        # Can also get here from lake secret
        self.connect(second_area, bridge_secret, r.jetpack(50))

        cave = self.region(
            "Cave",
            [
                "MP Cave Jetpack",
                "Cave Night Vision Goggles",
            ],
        )
        self.connect(second_area, cave, r.jump)

        vent_entrance = self.region(
            "Vent Entrance",
            [
                "Vent Entrance Pipebombs",
                "Blue Key Card",
                "Tele Cave Shotgun",
                "Vent Entrance Armor",
            ],
        )
        self.connect(second_area, vent_entrance, r.jump)

        vent_secret = self.region(
            "Secret Vent",
            [
                "Secret Vent",
                "Vent Secret Atomic Health",
            ],
        )
        # 50ish for the vent and 25 for the no jump entrance to here
        self.connect(vent_entrance, vent_secret, r.jetpack(75))

        blue_key_area = self.region(
            "Blue Key Area",
            [
                "Blue Tripmine 1",
                "Blue Tripmine 2",
                "Blue Tripmine 3",
                "Blue Night Vision Goggles",
                "MP Blue Chaingun",
            ],
        )
        self.connect(second_area, blue_key_area, self.blue_key)

        blue_upper = self.region(
            "Blue Upper Area",
            [
                "Blue Holo Duke",
            ],
        )
        self.connect(blue_key_area, blue_upper, r.jump)

        secret_symbol = self.region(
            "Secret Symbol",
            [
                "Secret Symbol",
                "Symbol Atomic Health",
                "Secret Corner",
                "Corner Steroids",
            ],
        )
        # jetpack can't get onto the ledge for the trigger
        self.connect(blue_key_area, secret_symbol, r.can_jump)

        hidden_wall = self.region(
            "Blue Hidden Wall",
            [
                "Blue Medkit",
            ],
        )
        # Maybe walk + roids is also possible?
        self.connect(blue_key_area, hidden_wall, (r.can_sprint | r.jump))

        elevator_drop = self.region(
            "Elevator Drop",
            [
                "Elevator Drop Medkit",
                "Elevator Drop Devastator",
            ],
        )
        # Can fall right onto the medkit
        # Jetpack can be avoided but leaves the player at 25 health
        self.connect(
            blue_key_area,
            elevator_drop,
            r.difficulty("hard")
            | r.jetpack(50)
            | r.difficulty("medium") & (r.jump | r.jetpack),
        )

        past_elevator = self.region(
            "Past Elevator",
            [
                "Secret Crate",
                "Crate Armor",
                "Crate Scuba Gear",
            ],
        )
        # Can fall from elevator into opening
        self.connect(elevator_drop, past_elevator, r.jump | r.difficulty("hard"))

        lake_secret = self.region(
            "Lake Secret Area",
            [
                "Secret Lake",
                "Lake Pipebombs",
            ],
        )
        self.connect(past_elevator, lake_secret, r.explosives)
        self.connect(lake_secret, bridge_secret)

        alien_table = self.region(
            "Alien Table",
            [
                "Table Freezethrower",
            ],
        )
        # Can sr50 on this without jump by using the pillar
        self.connect(past_elevator, alien_table, r.difficulty("hard") | r.jump)

        alien_freezer = self.region(
            "Alien Freezer",
            [
                "MP Freezer Atomic Health",
                "Red Key Card",
            ],
        )
        self.connect(past_elevator, alien_freezer, r.can_crouch)

        crates_upper = self.region(
            "Upper Crate Area",
            [
                "Crate Holo Duke",
            ],
        )
        self.connect(past_elevator, crates_upper, r.jump)

        conveyer_upper = self.region(
            "Conveyer Upper Area",
            [
                "Conveyer Jetpack",
                "Conveyer Shrinker",
            ],
        )
        self.connect(past_elevator, conveyer_upper, r.jump)

        ufo_secret = self.region(
            "Secret UFO",
            [
                "UFO Atomic Health",
                "Secret UFO",
            ],
        )

        self.connect(past_elevator, ufo_secret)

        red_key_area = self.region(
            "Red Key Area",
            [
                "Yellow Key Card",
                "Red Shotgun",
            ],
        )
        self.connect(
            past_elevator, red_key_area, self.red_key | r.crouch_jump & r.steroids
        )

        red_table = self.region(
            "Red Table",
            [
                "MP Red Steroids",
            ],
        )
        # Can sr50 on table
        self.connect(red_key_area, red_table, r.difficulty("hard") | r.jump)

        yellow_key_area = self.region(
            "Yellow Key Area",
            [
                "Exit",
            ],
        )
        self.connect(past_elevator, yellow_key_area, self.yellow_key)
        return ret
