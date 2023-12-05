from BaseClasses import Region

from ..base_classes import D3DLevel


class E4L4(D3DLevel):
    name = "Babe Land"
    levelnum = 3
    volumenum = 3
    keys = ["Red", "Blue"]
    location_defs = [
        {"id": 6, "name": "Red Boat RPG", "type": "sprite"},
        {"id": 9, "name": "Red Boat Chaingun", "type": "sprite"},
        {"id": 19, "name": "Red Upper Protective Boots", "type": "sprite"},
        {"id": 56, "name": "Red Key Card", "type": "sprite"},
        {"id": 101, "name": "Red Upper 2 Pipebombs", "type": "sprite"},
        {
            "id": 184,
            "mp": True,
            "name": "MP Boat Top Protective Boots",
            "type": "sprite",
        },
        {"id": 190, "name": "Castle Pipebombs", "type": "sprite"},
        {"id": 191, "name": "Castle Jetpack", "type": "sprite"},
        {"id": 200, "name": "Castle Holo Duke", "type": "sprite"},
        {"id": 204, "name": "Red Auction Night Vision Goggles", "type": "sprite"},
        {"id": 205, "name": "Red Upper 2 Holo Duke", "type": "sprite"},
        {"id": 210, "name": "Upper Main Pipebombs", "type": "sprite"},
        {"id": 213, "mp": True, "name": "MP Red Key Medkit", "type": "sprite"},
        {"id": 214, "name": "Blue Area Hidden Night Vision Goggles", "type": "sprite"},
        {"id": 215, "name": "Blue Area Hidden Armor", "type": "sprite"},
        {"id": 218, "name": "Pool Steroids", "type": "sprite"},
        {"id": 220, "name": "Pool Medkit", "type": "sprite"},
        {"id": 229, "name": "Inside Boat Shrinker", "type": "sprite"},
        {"id": 230, "name": "Boat Top Freezethrower", "type": "sprite"},
        {"id": 231, "name": "Castle Atomic Health", "type": "sprite"},
        {"id": 232, "name": "Castle RPG", "type": "sprite"},
        {"id": 233, "name": "Castle Devastator", "type": "sprite"},
        {"id": 234, "name": "Castle Chaingun", "type": "sprite"},
        {"id": 235, "name": "Castle Shotgun", "type": "sprite"},
        {"id": 236, "name": "Upper Pool Chaingun", "type": "sprite"},
        {"id": 238, "name": "Blue Area Back RPG", "type": "sprite"},
        {"id": 245, "name": "Upper Main Atomic Health", "type": "sprite"},
        {"id": 246, "name": "Ticket Booth Shotgun", "type": "sprite"},
        {"id": 445, "name": "Blue Key Card", "type": "sprite"},
        {"id": 634, "name": "Red Upper Armor", "type": "sprite"},
        {"id": 656, "name": "Castle Dive Tripmine 1", "type": "sprite"},
        {"id": 657, "name": "Castle Dive Tripmine 2", "type": "sprite"},
        {"id": 668, "name": "Castle Dive Scuba Gear", "type": "sprite"},
        {"id": 694, "name": "Sky Secret Atomic Health", "type": "sprite"},
        {"id": 755, "name": "Red Boat Shrinker", "type": "sprite"},
        {"id": 90, "name": "Secret Blue Area Hidden Room", "type": "sector"},
        {"id": 193, "name": "Secret Blue Explosion", "type": "sector"},
        {"id": 200, "name": "Secret Sky", "type": "sector"},
        {"id": 336, "name": "Secret Prison", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
    must_dive = True

    def main_region(self) -> Region:
        r = self.rules
        ret = self.region(
            self.name,
            [],
        )

        ticket_booth = self.region(
            "Ticket Booth",
            [
                "Ticket Booth Shotgun",
                "Pool Steroids",
            ],
        )
        # Can use the rotating door to clip over into the ticket booth
        # Also possible to strafe into corner and grab, TODO maybe lower difficulty
        self.connect(ret, ticket_booth, r.difficulty("hard") | r.jump)

        main_upper = self.region(
            "Upper Main Area",
            [
                "Upper Main Pipebombs",
                "Upper Main Atomic Health",
            ],
        )
        self.connect(ret, main_upper, r.jump)

        pool = self.region(
            "Pool",
            [
                "Pool Medkit",
            ],
        )
        self.connect(ret, pool, r.can_dive)

        upper_pool = self.region(
            "Upper Pool",
            [
                "Upper Pool Chaingun",
            ],
        )
        self.connect(ret, upper_pool, r.jump)

        pool_price = self.region(
            "Pool Price Area",
            [
                "Blue Key Card",
            ],
        )
        # Can sr50 from the rotating boats onto the price pillar
        self.connect(ret, pool_price, r.difficulty("hard") | r.jump)

        blue_area = self.region(
            "Blue Key Area",
            [],
        )
        self.connect(ret, blue_area, self.blue_key)

        blue_secret = self.region(
            "Blue Secret",
            [
                "Secret Red Explosion",
            ],
        )
        self.connect(blue_area, blue_secret, r.explosives)

        blue_area_back = self.region(
            "Blue Area Behind Targets",
            [
                "Blue Area Back RPG",
            ],
        )
        self.connect(blue_area, blue_area_back, r.jump)

        blue_area_hidden = self.region(
            "Blue Area Hidden Room",
            [
                "Secret Blue Area Hidden Room",
                "Blue Area Hidden Night Vision Goggles",
                "Blue Area Hidden Armor",
                "Blue Key Card",
            ],
        )
        self.connect(blue_area, blue_area_hidden, r.jump & r.can_crouch)

        red_area = self.region(
            "Red Key Area",
            [
                "MP Red Key Medkit",
                "Red Boat RPG",
                "Red Boat Chaingun",
                "Red Boat Shrinker",
                "Red Auction Night Vision Goggles",
            ],
        )
        self.connect(main_upper, red_area, self.red_key)

        red_upper_start = self.region(
            "Red Upper Area Start",
            [
                "Red Upper Armor",
                "Red Upper Protective Boots",
            ],
        )
        # Can sr50 jump up using the sign
        self.connect(
            red_area, red_upper_start, r.jump & (r.difficulty("hard") | r.can_sprint)
        )

        red_upper = self.region(
            "Red Upper Area",
            [
                "Red Upper 2 Pipebombs",
                "Red Upper 2 Holo Duke",
            ],
        )
        self.connect(red_area, red_upper, r.jump)

        prison_secret = self.region(
            "Prison Secret Area",
            [
                "Secret Prison",
            ],
        )
        self.connect(red_area, prison_secret, r.explosives & r.jump)

        castle_dive = self.region(
            "Castle Dive Area",
            [
                "Castle Dive Tripmine 1",
                "Castle Dive Tripmine 2",
                "Castle Dive Scuba Gear",
                "Inside Boat Shrinker",
            ],
        )
        self.connect(red_area, castle_dive, r.can_dive)

        boat_top = self.region(
            "Boat Top",
            [
                "MP Boat Top Protective Boots",
                "Boat Top Freezethrower",
            ],
        )
        self.connect(red_area, boat_top, r.jump)

        castle = self.region(
            "Castle",
            [
                "Castle Pipebombs",
                "Castle Jetpack",
                "Castle Holo Duke",
                "Castle Atomic Health",
                "Castle RPG",
                "Castle Devastator",
                "Castle Chaingun",
                "Castle Shotgun",
                "Exit",
            ],
        )
        self.connect(red_area, castle, r.jump)

        sky_secret = self.region(
            "Sky Secret Area",
            [
                "Secret Sky",
                "Sky Secret Atomic Health",
            ],
        )

        # Only requires around 30 jetpack i believe
        self.connect(red_area, sky_secret, r.jetpack(50))
        return ret
