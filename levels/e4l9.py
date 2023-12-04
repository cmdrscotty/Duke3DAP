from BaseClasses import Region

from ..base_classes import D3DLevel


class E4L9(D3DLevel):
    name = "Derelict"
    levelnum = 8
    volumenum = 3
    keys = ["Red", "Blue", "Yellow"]
    location_defs = [
        {"id": 10, "name": "Kitchen Medkit", "type": "sprite"},
        {"id": 65, "name": "Yellow Upper Atomic Health", "type": "sprite"},
        {"id": 185, "name": "Crusher Atomic Health", "type": "sprite"},
        {"id": 211, "name": "Captains Shrinker", "type": "sprite"},
        {"id": 214, "name": "Captains Atomic Health 1", "type": "sprite"},
        {"id": 215, "name": "Captains Atomic Health 2", "type": "sprite"},
        {"id": 216, "name": "Captains Night Vision Goggles", "type": "sprite"},
        {"id": 217, "name": "Captains Armor", "type": "sprite"},
        {"id": 223, "name": "Barracks Steroids", "type": "sprite"},
        {"id": 229, "name": "TV Chaingun", "type": "sprite"},
        {"id": 261, "name": "Yellow Pipebombs", "type": "sprite"},
        {"id": 504, "name": "Blue Key Card", "type": "sprite"},
        {"id": 626, "name": "Yellow Upper Pipebombs", "type": "sprite"},
        {"id": 834, "name": "Crate Protective Boots", "type": "sprite"},
        {"id": 960, "name": "Upper Deck Steroids", "type": "sprite"},
        {"id": 961, "name": "Upper Deck Medkit", "type": "sprite"},
        {"id": 962, "name": "Scan Room RPG", "type": "sprite"},
        {"id": 964, "name": "Outside Dive RPG", "type": "sprite"},
        {"id": 967, "name": "Upper Deck Atomic Health 1", "type": "sprite"},
        {"id": 968, "name": "Upper Deck Atomic Health 2", "type": "sprite"},
        {"id": 969, "name": "Ship Deck Scuba Gear", "type": "sprite"},
        {"id": 970, "mp": True, "name": "MP Outside Dive Jetpack 1", "type": "sprite"},
        {"id": 971, "mp": True, "name": "MP Outside Dive Jetpack 2", "type": "sprite"},
        {"id": 972, "mp": True, "name": "MP Yellow Final Jetpack", "type": "sprite"},
        {"id": 973, "name": "Ship Deck Armor", "type": "sprite"},
        {"id": 976, "name": "Upper Deck Shotgun", "type": "sprite"},
        {"id": 977, "name": "Low Deck Chaingun", "type": "sprite"},
        {"id": 980, "name": "Upper Deck Shrinker", "type": "sprite"},
        {"id": 983, "name": "Upper Deck Tripmine 1", "type": "sprite"},
        {"id": 984, "name": "Upper Deck Tripmine 2", "type": "sprite"},
        {"id": 988, "name": "Crate Freezethrower", "type": "sprite"},
        {"id": 989, "name": "Crate Devastator", "type": "sprite"},
        {"id": 992, "name": "Scan Room  Night Vision Goggles", "type": "sprite"},
        {"id": 994, "name": "Crate RPG", "type": "sprite"},
        {"id": 995, "mp": True, "name": "MP Crate Jetpack", "type": "sprite"},
        {"id": 996, "name": "Low Deck Atomic Health", "type": "sprite"},
        {"id": 997, "name": "Low Deck Holo Duke", "type": "sprite"},
        {"id": 1007, "name": "Big Crate Pipebombs 1", "type": "sprite"},
        {"id": 1008, "name": "Big Crate Pipebombs 2", "type": "sprite"},
        {"id": 1009, "name": "Big Crate Armor", "type": "sprite"},
        {"id": 1010, "name": "Fire Atomic Health", "type": "sprite"},
        {"id": 1011, "name": "Next to Crusher Chaingun", "type": "sprite"},
        {"id": 1012, "name": "Next to Crusher Shotgun", "type": "sprite"},
        {"id": 1021, "name": "Red Key Card", "type": "sprite"},
        {"id": 1022, "name": "Yellow Key Card", "type": "sprite"},
        {"id": 1058, "name": "Yellow Atomic Health", "type": "sprite"},
        {"id": 1081, "name": "Yellow Protective Boots", "type": "sprite"},
        {"id": 1082, "name": "Yellow Steroids", "type": "sprite"},
        {"id": 1111, "name": "1111 Atomic Health", "type": "sprite"},
        {"id": 1118, "name": "Yellow Underwater Atomic Health", "type": "sprite"},
        {"id": 1173, "mp": True, "name": "MP Yellow Jetpack", "type": "sprite"},
        {"id": 1181, "name": "Dive Secret Chaingun", "type": "sprite"},
        {"id": 1182, "name": "Dive Secret Steroids", "type": "sprite"},
        {"id": 1183, "name": "Dive Secret Night Vision Goggles", "type": "sprite"},
        {"id": 1184, "name": "Dive Secret Armor", "type": "sprite"},
        {"id": 1185, "name": "1185 Shotgun", "type": "sprite"},
        {"id": 347, "name": "Secret Crate", "type": "sector"},
        {"id": 718, "name": "Secret TV", "type": "sector"},
        {"id": 761, "name": "Secret Captains Cabin", "type": "sector"},
        {"id": 795, "name": "Secret Dive", "type": "sector"},
        {"id": 800, "name": "Secret Kitchen", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]

    def main_region(self) -> Region:
        r = self.rules
        ret = self.region(
            self.name,
            [],
        )

        outside_dive = self.region(
            "Outside Dive",
            [
                "Outside Dive RPG",
                "MP Outside Dive Jetpack 1",
                "MP Outside Dive Jetpack 2",
                "Secret Dive",
                "Dive Secret Chaingun",
                "Dive Secret Steroids",
                "Dive Secret Night Vision Goggles",
                "Dive Secret Armor",
            ],
        )
        self.connect(ret, outside_dive, r.can_dive)

        ship_deck = self.region(
            "Ship Deck",
            [
                "Ship Deck Armor",
                "Ship Deck Scuba Gear",
            ],
        )
        self.connect(ret, ship_deck)

        upper_deck = self.region(
            "Upper Deck",
            [
                "Upper Deck Steroids",
                "Upper Deck Medkit",
                "Upper Deck Atomic Health 1",
                "Upper Deck Atomic Health 2",
                "Upper Deck Shotgun",
                "Upper Deck Shrinker",
                "Upper Deck Tripmine 1",
                "Upper Deck Tripmine 2",
                "Blue Key Card",
                "Scan Room RPG",
                "Scan Room  Night Vision Goggles",
                "Crate Freezethrower",
                "Crate Devastator",
                "Low Deck Atomic Health",
                "Low Deck Chaingun",
                "Low Deck Holo Duke",
            ],
        )
        self.connect(ship_deck, upper_deck, r.jump)

        blue_key_area = self.region(
            "Blue Key Area",
            [
                "Barracks Steroids",
            ],
        )
        self.connect(upper_deck, blue_key_area, self.blue_key)

        blue_key_lower = self.region(
            "Blue Key Lower Area",
            [
                "Secret Kitchen",
                "Kitchen Medkit",
                "Captains Armor",
            ],
        )
        self.connect(blue_key_area, blue_key_lower, r.can_crouch)

        blue_key_upper = self.region(
            "Blue Key Upper Area",
            [
                "Captains Night Vision Goggles",
                "Red Key Card",
                "Secret Captains Cabin",
                "Captains Shrinker",
                "Captains Atomic Health 1",
                "Captains Atomic Health 2",
            ],
        )
        self.connect(blue_key_area, blue_key_upper, r.jump)

        red_key_area = self.region(
            "Red Key Area",
            [
                "Fire Atomic Health",
            ],
        )
        self.connect(blue_key_area, red_key_area, self.red_key | r.crouch_jump)

        red_upper = self.region(
            "Red Upper Area",
            [
                "Crusher Atomic Health",
                "Big Crate Pipebombs 1",
                "Big Crate Pipebombs 2",
                "Big Crate Armor",
                "Fire Atomic Health",
                "Next to Crusher Chaingun",
                "Next to Crusher Shotgun",
                "Yellow Key Card",
            ],
        )
        self.connect(red_key_area, red_upper, r.jump)

        yellow_key_area = self.region(
            "Yellow Key Area",
            [
                "MP Yellow Jetpack",
                "Yellow Atomic Health",
                "Yellow Pipebombs",
                "Yellow Steroids",
                "Yellow Protective Boots",
            ],
        )
        self.connect(blue_key_area, yellow_key_area, self.yellow_key)

        crate_secret = self.region(
            "Secret Crate",
            [
                "Secret Crate",
                "Crate RPG",
                "MP Crate Jetpack",
                "Crate Protective Boots",
            ],
        )
        self.connect(yellow_key_area, crate_secret, r.jump)

        yellow_underwater = self.region(
            "Yellow Underwater",
            [
                "Yellow Underwater Atomic Health",
            ],
        )
        self.connect(yellow_key_area, yellow_underwater, r.can_dive)

        yellow_upper = self.region(
            "Yellow Upper Area",
            [
                "Yellow Upper Atomic Health",
                "Yellow Upper Pipebombs",
            ],
        )
        self.connect(yellow_key_area, yellow_upper, r.can_dive | r.jetpack(50))

        yellow_final = self.region(
            "Yellow Final Area",
            [
                "MP Yellow Final Jetpack",
                "Exit",
            ],
        )
        self.connect(yellow_upper, yellow_final, r.can_dive)
        return ret
