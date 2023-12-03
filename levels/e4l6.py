from BaseClasses import Region

from ..base_classes import D3DLevel


class E4L6(D3DLevel):
    name = "Going Postal"
    levelnum = 5
    volumenum = 3
    keys = ["Red", "Blue", "Yellow"]
    location_defs = [
        {"id": 25, "name": "Firetruck Protective Boots", "type": "sprite"},
        {"id": 26, "name": "Firetruck Devastator", "type": "sprite"},
        {"id": 81, "name": "Container Pipebombs", "type": "sprite"},
        {"id": 84, "name": "Blue Vent Shrinker", "type": "sprite"},
        {"id": 145, "name": "Conveyer Upper Red Key Card", "type": "sprite"},
        {"id": 206, "name": "Red Chaingun", "type": "sprite"},
        {"id": 209, "name": "Red Armor", "type": "sprite"},
        {"id": 210, "name": "Red Medkit", "type": "sprite"},
        {"id": 217, "name": "Red Pipebombs", "type": "sprite"},
        {"id": 266, "name": "Red Tripbomb 1", "type": "sprite"},
        {"id": 267, "name": "Red Tripbomb 2", "type": "sprite"},
        {"id": 277, "name": "Front Holo Duke", "type": "sprite"},
        {"id": 279, "name": "Red Atomic Health", "type": "sprite"},
        {"id": 281, "name": "Blue Freezethrower", "type": "sprite"},
        {"id": 284, "name": "Locker Steroids", "type": "sprite"},
        {"id": 286, "name": "Locker Armor", "type": "sprite"},
        {"id": 287, "name": "Behind Counter Shotgun", "type": "sprite"},
        {"id": 288, "name": "Blue Desk Pipebombs", "type": "sprite"},
        {"id": 290, "name": "Blue Crates Devastator", "type": "sprite"},
        {"id": 291, "name": "Conveyer Upper Night Vision Goggles", "type": "sprite"},
        {"id": 293, "name": "Blue Steroids", "type": "sprite"},
        {"id": 294, "name": "Blue Armor", "type": "sprite"},
        {"id": 295, "mp": True, "name": "MP Conveyer Upper Jetpack", "type": "sprite"},
        {"id": 296, "name": "Conveyer Upper Medkit", "type": "sprite"},
        {"id": 305, "name": "Locker Crate Chaingun", "type": "sprite"},
        {"id": 306, "name": "Basement RPG", "type": "sprite"},
        {"id": 353, "name": "Locker Secret Atomic Health", "type": "sprite"},
        {"id": 464, "name": "Blue Atomic Health", "type": "sprite"},
        {"id": 530, "name": "Firetruck Atomic Health", "type": "sprite"},
        {"id": 534, "name": "Locker Blue Key Card", "type": "sprite"},
        {"id": 590, "name": "Red Devastator", "type": "sprite"},
        {"id": 635, "name": "Paw Shotgun", "type": "sprite"},
        {"id": 665, "name": "Blue Conveyer Atomic Health", "type": "sprite"},
        {"id": 672, "name": "Locker Secret Medkit", "type": "sprite"},
        {"id": 724, "name": "Red Area Yellow Key Card", "type": "sprite"},
        {"id": 750, "name": "Front Vent Pipebombs", "type": "sprite"},
        {"id": 185, "name": "Locker Secret", "type": "sector"},
        {"id": 250, "name": "Blue Vent Secret", "type": "sector"},
        {"id": 302, "name": "Firetruck Secret", "type": "sector"},
        {"id": 317, "name": "Front Vent Secret", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
    def main_region(self) -> Region:
        r = self.rules
        ret = self.region(
            self.name,
            [
                "Front Holo Duke",
            ],
        )

        start_upper = self.region(
            "Start Upper",
            [
                "Container Pipebombs",
                "Firetruck Atomic Health",
                "Firetruck Secret",
                "Firetruck Protective Boots",
                "Firetruck Devastator",
                "Container Pipebombs",
            ],
        )
        self.connect(ret, start_upper, r.jump)

        paw_secret = self.region(
            "Paw Secret",
            [
                "Paw Shotgun",
            ],
        )
        # Can grab the item by jumping and sr40ing towards the item
        self.connect(ret, paw_secret, r.can_crouch |
                     r.difficulty("hard") & r.jump)
        
        behind_counter = self.region(
            "Behind Counter",
            [
                "Behind Counter Shotgun",
                "Basement RPG",
                "Locker Steroids",
                "Locker Armor",
                "Locker Blue Key Card",
                "Locker Secret",
                "Locker Secret Atomic Health",
            ],
        )
        self.connect(ret, behind_counter, r.jump)

        front_vent = self.region(
            "Front Vent",
            [
                "Front Vent Pipebombs",
            ],
        )
        # Can grab the item by jumping towards the item
        self.connect(ret, front_vent, r.can_crouch |
                     r.difficulty("hard") & r.jump)
        
        front_vent_secret = self.region(
            "Front Vent Secret",
            [
                "Front Vent Secret",
            ],
        )
        self.connect(ret, front_vent_secret, r.can_crouch & r.jump)

        locker_secret_upper = self.region(
            "Locker Secret Upper",
            [
                "Locker Crate Chaingun",
            ],
        )
        self.connect(behind_counter, locker_secret_upper, r.jump)

        locker_secret_grate = self.region(
            "Locker Secret Grate",
            [
                "Locker Secret Medkit",
            ],
        )
        # Can grab the item by jumping towards the hole, easier than others
        self.connect(behind_counter, locker_secret_grate, r.explosives &
                    (r.can_crouch | 
                    (r.difficulty("medium") & r.jump)
                    ))
        
        blue_key_area = self.region(
            "Blue Key Area",
            [
                "Blue Steroids",
                "Blue Armor",
                "Blue Freezethrower",
                "Blue Atomic Health",
            ],
        )
        self.connect(behind_counter, blue_key_area, self.blue_key)

        blue_vent_secret = self.region(
            "Blue Vent Secret",
            [
                "Blue Vent Secret",
                "Blue Vent Shrinker",
            ],
        )

        self.connect(blue_key_area, blue_vent_secret, r.can_crouch)

        blue_crates = self.region(
            "Blue Crates",
            [
                "Blue Crates Devastator",
            ],
        )
        self.connect(blue_key_area, blue_crates, r.jump)

        conveyer_ducking = self.region(
            "Blue Conveyer Ducking",
            [
                "Blue Conveyer Atomic Health",
            ],
        )
        self.connect(blue_key_area, conveyer_ducking, r.can_crouch)

        blue_desk = self.region(
            "Blue Desk",
            [
                "Blue Desk Pipebombs",
            ],
        )
        # Can get up by clipping on the post bag and sr50ing over to conveyer
        self.connect(blue_key_area, blue_desk, r.jump |
                     r.difficulty("medium"))
        
        conveyer_upper = self.region(
            "Blue Conveyer Upper",
            [
                "Conveyer Upper Night Vision Goggles",
                "MP Conveyer Upper Jetpack",
                "Conveyer Upper Medkit",
                "Conveyer Upper Red Key Card",
            ],
        )
        self.connect(blue_desk, conveyer_upper, 
                     (r.jump & r.difficulty("medium")|
                     (r.difficulty("hard") & r.can_crouch) |
                     (r.jump & r.can_crouch)
                     ))
        
        red_key_area = self.region(
            "Red Key Area",
            [
                "Red Tripbomb 1",
                "Red Tripbomb 2",
                "Red Chaingun",
                "Red Armor",
                "Red Medkit",
                "Red Pipebombs",
                "Red Devastator",
                "Red Area Yellow Key Card",
                "Red Atomic Health", 
            ],
        )
        self.connect(blue_key_area, red_key_area, self.red_key & r.jump & r.can_crouch)

        yellow_key_area = self.region(
            "Yellow Key Area",
            [
                "Exit",
            ],
        )
        self.connect(red_key_area, yellow_key_area, self.yellow_key)