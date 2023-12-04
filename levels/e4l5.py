from BaseClasses import Region

from ..base_classes import D3DLevel


class E4L5(D3DLevel):
    name = "Pigsty"
    levelnum = 4
    volumenum = 3
    keys = ["Blue", "Red", "Yellow"]
    location_defs = [
        {"id": 61, "name": "Basement Pipebombs", "type": "sprite"},
        {"id": 76, "name": "Basement Atomic Health", "type": "sprite"},
        {"id": 79, "name": "Security Steroids", "type": "sprite"},
        {"id": 80, "name": "Graffiti Steroids", "type": "sprite"},
        {"id": 90, "name": "Graffiti Freezethrower", "type": "sprite"},
        {"id": 91, "name": "Graffiti Devastator", "type": "sprite"},
        {"id": 92, "name": "Graffiti RPG", "type": "sprite"},
        {"id": 123, "name": "Yellow Atomic Health", "type": "sprite"},
        {"id": 142, "mp": True, "name": "MP Yellow Shotgun", "type": "sprite"},
        {"id": 196, "name": "Basement Tripmine 1", "type": "sprite"},
        {"id": 197, "name": "Basement Tripmine 2", "type": "sprite"},
        {"id": 198, "name": "Basement Freezethrower", "type": "sprite"},
        {"id": 211, "name": "Basement Jetpack", "type": "sprite"},
        {"id": 260, "name": "Upstairs RPG", "type": "sprite"},
        {"id": 264, "name": "Upstairs Medkit", "type": "sprite"},
        {"id": 266, "name": "Bookshelf Atomic Health", "type": "sprite"},
        {"id": 267, "name": "Red Area Steroids", "type": "sprite"},
        {"id": 268, "name": "Poster Medkit", "type": "sprite"},
        {"id": 363, "name": "Blue Key Card", "type": "sprite"},
        {"id": 441, "name": "Telephone Atomic Health", "type": "sprite"},
        {"id": 528, "name": "Bookshelf Chaingun 1", "type": "sprite"},
        {"id": 529, "name": "Bookshelf Chaingun 2", "type": "sprite"},
        {"id": 530, "name": "Bookshelf Chaingun 3", "type": "sprite"},
        {"id": 613, "name": "Start Shotgun", "type": "sprite"},
        {"id": 618, "name": "Start Chaingun", "type": "sprite"},
        {"id": 717, "name": "Basement Blue Pipebombs", "type": "sprite"},
        {"id": 751, "name": "Yellow Key Card", "type": "sprite"},
        {"id": 767, "mp": True, "name": "MP Hangout Jetpack", "type": "sprite"},
        {"id": 768, "name": "Yellow Shrinker", "type": "sprite"},
        {"id": 771, "name": "Start Armor", "type": "sprite"},
        {"id": 773, "name": "Upstairs Night Vision Goggles", "type": "sprite"},
        {"id": 811, "name": "Start Pipebombs", "type": "sprite"},
        {"id": 812, "mp": True, "name": "MP Security Armor", "type": "sprite"},
        {"id": 813, "mp": True, "name": "MP Security Shotgun", "type": "sprite"},
        {"id": 841, "name": "Unreachable Holo Duke", "type": "sprite"},
        {"id": 854, "name": "Red Key Card", "type": "sprite"},
        {"id": 5, "name": "Secret Telephone", "type": "sector"},
        {"id": 56, "name": "Secret Poster", "type": "sector"},
        {"id": 123, "name": "Secret Bookshelf", "type": "sector"},
        {"id": 465, "name": "Secret Graffiti", "type": "sector"},
        {"id": 469, "name": "Secret Basement", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
        {"id": 11, "name": "Secret Exit", "type": "exit"},
    ]

    def main_region(self) -> Region:
        r = self.rules
        ret = self.region(
            self.name,
            [
                "Start Shotgun",
                "Start Chaingun",
                "Start Armor",
                "Start Pipebombs",
            ],
        )
        tele_secret = self.region(
            "Secret Telephone",
            [
                "Secret Telephone",
                "Telephone Atomic Health",
            ],
        )
        # one way, cant go back without crouching
        self.connect(ret, tele_secret, r.jump)

        graffiti_secret = self.region(
            "Secret Graffiti",
            [
                "Secret Graffiti",
                "Graffiti Steroids",
                "Graffiti Freezethrower",
                "Graffiti Devastator",
                "Graffiti RPG",
            ],
        )
        self.connect(ret, graffiti_secret, r.jetpack(100))

        past_car = self.region(
            "Lobby past car",
            [
                "Basement Pipebombs",
                "Basement Jetpack",
                "Basement Tripmine 1",
                "Basement Tripmine 2",
                "Basement Freezethrower",
                "Basement Atomic Health",
                "Secret Basement",
                "Upstairs RPG",
                "Upstairs Medkit",
                "Upstairs Night Vision Goggles",
                "Blue Key Card",
            ],
        )
        # Can walk off the stairs on top of the, a bit tricky without sprint
        # Other entry leads through manhole cover
        self.connect(
            ret, past_car, r.can_sprint | r.difficulty("medium") | r.explosives
        )

        security_mons_upper = self.region(
            "Security Monitors Upper",
            [
                "Security Steroids",
                "MP Security Armor",
                "MP Security Shotgun",
            ],
        )
        # Can diagonal walk into security monitors and use crouch to clip up
        # Requires difficult sr50 without sprint
        self.connect(
            past_car,
            security_mons_upper,
            r.can_sprint & r.difficulty("medium") | r.difficulty("hard") | r.jump,
        )

        blue_key_area = self.region(
            "Blue Key Area",
            [
                "Secret Bookshelf",
                "Bookshelf Atomic Health",
                "Bookshelf Chaingun 1",
                "Bookshelf Chaingun 2",
                "Bookshelf Chaingun 3",
            ],
        )
        self.connect(past_car, blue_key_area, self.blue_key)
        # Can clip through basement blue key door with roid crouch jump
        basement_blue_area = self.region(
            "Basement Blue Area",
            [
                "Basement Blue Pipebombs",
                "Red Key Card",
            ],
        )
        self.connect(
            past_car, basement_blue_area, self.blue_key | r.crouch_jump & r.steroids
        )

        red_key_area = self.region(
            "Red Key Area",
            [
                "Red Area Steroids",
                "Yellow Key Card",
            ],
        )
        self.connect(past_car, red_key_area, self.red_key)

        poster_secret = self.region(
            "Poster Secret Area",
            [
                "Secret Poster",
                "Poster Medkit",
            ],
        )
        # Strafe up the terminal on the right to get into the poster secret
        self.connect(red_key_area, poster_secret, r.jump | r.difficulty("medium"))

        yellow_key_area = self.region(
            "Yellow Key Area",
            [
                "Yellow Shrinker",
                "MP Yellow Shotgun",
                "Yellow Atomic Health",
            ],
        )
        self.connect(ret, yellow_key_area, self.yellow_key)

        secret_exit_area = self.region(
            "Secret Exit Area",
            [
                "Secret Exit",
            ],
        )
        self.connect(yellow_key_area, secret_exit_area, r.jump)

        hangout_room = self.region(
            "Hangout Room",
            [
                "MP Hangout Jetpack",
                "Exit",
            ],
        )
        self.connect(yellow_key_area, hangout_room, r.jump)

        # This location is unreachable behind a wall that's supposed to blow up:
        # {"id": 841, "name": "Unreachable Holo Duke", "type": "sprite"},
        return ret
