from BaseClasses import Region

from ..base_classes import D3DLevel


class E4L2(D3DLevel):
    name = "Duke-Burger"
    levelnum = 1
    volumenum = 3
    keys = ["Blue", "Red"]
    location_defs = [
        {"id": 59, "name": "Slaughterhouse Tripmine", "type": "sprite"},
        {"id": 75, "name": "Conveyer Upper RPG", "type": "sprite"},
        {"id": 98, "name": "Kitchen Vent Pipebombs", "type": "sprite"},
        {"id": 101, "name": "Kitchen Vent Steroids", "type": "sprite"},
        {"id": 102, "name": "Kitchen Vent Medkit", "type": "sprite"},
        {"id": 125, "name": "Inside DB Freezethrower", "type": "sprite"},
        {"id": 140, "name": "Dog Kennel Pipebombs", "type": "sprite"},
        {"id": 150, "name": "Manager Room Tripmine 1", "type": "sprite"},
        {"id": 151, "name": "Manager Room Tripmine 2", "type": "sprite"},
        {"id": 198, "name": "Red Key Card", "type": "sprite"},
        {"id": 217, "name": "Manager Room Armor", "type": "sprite"},
        {"id": 354, "name": "Kitchen Fryer Armor", "type": "sprite"},
        {"id": 355, "name": "Slaughterhouse Vent Medkit", "type": "sprite"},
        {"id": 413, "name": "Outside Atomic Health", "type": "sprite"},
        {"id": 414, "name": "Outside Pipebombs", "type": "sprite"},
        {"id": 416, "mp": True, "name": "MP Inside DB RPG", "type": "sprite"},
        {"id": 417, "name": "Kitchen Shotgun", "type": "sprite"},
        {"id": 418, "name": "Kitchen Corner Chaingun", "type": "sprite"},
        {"id": 423, "name": "Outside Steroids", "type": "sprite"},
        {"id": 563, "mp": True, "name": "MP Outside Sign Holo Duke", "type": "sprite"},
        {"id": 595, "name": "Slaughterhouse Devastator", "type": "sprite"},
        {"id": 663, "name": "Outside Sign Shrinker", "type": "sprite"},
        {"id": 664, "name": "Blue Key Card", "type": "sprite"},
        {"id": 679, "name": "Kitchen Back Night Vision Goggles", "type": "sprite"},
        {"id": 748, "name": "Kitchen Back Freezethrower", "type": "sprite"},
        {"id": 102, "name": "Secret Dog Kennel", "type": "sector"},
        {"id": 311, "name": "Secret Kitchen Vent", "type": "sector"},
        {"id": 313, "name": "Secret Conveyer Upper", "type": "sector"},
        {"id": 321, "name": "Secret Kitchen Back", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]

    def main_region(self) -> Region:
        r = self.rules
        ret = self.region(
            self.name,
            [
                "Outside Atomic Health",
                "Outside Pipebombs",
                "Outside Steroids",
            ],
        )

        outside_sign = self.region(
            "Outside Sign",
            [
                "Outside Sign Shrinker",
                "MP Outside Sign Holo Duke",
                "Blue Key Card",
            ],
        )
        self.connect(ret, outside_sign, r.jump)

        kitchen_secret = self.region(
            "Kitchen Vent",
            [
                "Kitchen Vent Pipebombs",
                "Kitchen Vent Steroids",
                "Kitchen Vent Medkit",
                "Secret Kitchen Vent",
            ],
        )
        # Can enter without crouch but cant exit, maybe hard difficulty?
        self.connect(
            ret, kitchen_secret, (r.can_jump & r.difficulty("medium")) | r.jetpack(50)
        )

        inside_db_front = self.region(
            "Inside DB Front",
            [
                "MP Inside DB RPG",
                "Inside DB Freezethrower",
            ],
        )
        inside_db_kitchen = self.region(
            "Inside DB Kitchen",
            [
                "Red Key Card",
                "Kitchen Shotgun",
            ],
        )

        # Can go in through kitchen secret or go in the normal way
        self.connect(ret, inside_db_front, self.blue_key)
        self.connect(kitchen_secret, inside_db_kitchen, r.can_crouch)
        # Outside path requires shrinker to get to kitchen area,
        # Glitched logic allows jumpclip through shrinker path
        self.connect(inside_db_front, inside_db_kitchen, r.crouch_jump | r.can_shrink)

        kitchen_corner = self.region(
            "Kitchen Corner",
            [
                "Kitchen Corner Chaingun",
            ],
        )
        # This one can be gotten by diagonal walking onto the counter instead of having jump
        # Hard difficulty because if certain entities are destroyed it wont work anymore
        self.connect(inside_db_kitchen, kitchen_corner, r.difficulty("hard") | r.jump)

        kitchen_fryer = self.region(
            "Kitchen Fryer",
            [
                "Kitchen Fryer Armor",
            ],
        )
        # TODO: Can maybe be grabbed by diagonal walking into the corner?
        self.connect(
            inside_db_kitchen,
            kitchen_fryer,
            r.jump | (r.difficulty("hard") & r.can_sprint),
        )

        kitchen_back_secret = self.region(
            "Secret Kitchen Back",
            [
                "Kitchen Back Freezethrower",
                "Secret Kitchen Back",
            ],
        )
        # Can jump/jetpack instead of duck to activate switch at desk
        # TODO: Extreme logic: Use enforcer to clip on topmost box for secret
        # r.jetpack(100) & r.difficulty("extreme") 100 jetpack just to be nice and allow more attempts
        self.connect(
            inside_db_kitchen,
            kitchen_back_secret,
            (r.can_jump & r.difficulty("medium")) | r.can_jump & r.can_crouch,
        )

        kitchen_back_crate = self.region(
            "Kitchen Back Crate",
            [
                "Kitchen Back Night Vision Goggles",
            ],
        )
        self.connect(inside_db_kitchen, kitchen_back_crate, r.jump)

        slaughterhouse = self.region(
            "Slaughterhouse",
            [
                "Slaughterhouse Devastator",
            ],
        )
        self.connect(inside_db_kitchen, slaughterhouse, self.red_key)

        slaughterhouse_vent = self.region(
            "Slaughterhouse Vent",
            [
                "Slaughterhouse Vent Medkit",
            ],
        )
        self.connect(slaughterhouse, slaughterhouse_vent, r.jump)

        # Can just walk/run past the tripmines, a bit obscure so medium

        conveyers = self.region(
            "Slaughterhouse Conveyers",
            [
                "Slaughterhouse Tripmine",
            ],
        )
        self.connect(slaughterhouse, conveyers, r.difficulty("medium") | r.explosives)

        conveyers_upper = self.region(
            "Slaughterhouse Conveyers Upper",
            [
                "Secret Conveyer Upper",
                "Conveyer Upper RPG",
            ],
        )
        self.connect(conveyers, conveyers_upper, r.jump)

        dog_kennel = self.region(
            "Secret Dog Kennel",
            [
                "Secret Dog Kennel",
                "Dog Kennel Pipebombs",
            ],
        )
        self.connect(conveyers_upper, dog_kennel, r.jump & r.explosives)

        manager_room = self.region(
            "Manager Room",
            [
                "Manager Room Tripmine 1",
                "Manager Room Tripmine 2",
                "Exit",
            ],
        )
        self.connect(conveyers_upper, manager_room)

        # Alternate path by blowing up office wall from the outside
        # Medium difficulty because its obscure
        self.connect(
            ret,
            manager_room,
            r.difficulty("medium") & r.pipebomb & r.can_crouch & r.glitched,
        )

        manager_room_cabinet = self.region(
            "Manager Room Cabinet",
            [
                "Manager Room Armor",
            ],
        )
        self.connect(manager_room, manager_room_cabinet, r.jump)
        return ret
