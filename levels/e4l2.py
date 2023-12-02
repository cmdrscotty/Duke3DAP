from BaseClasses import Region

from ..base_classes import D3DLevel


class E4L2(D3DLevel):
    name = "Duke-Burger"
    levelnum = 1
    volumenum = 3
    keys = ["Blue","Red"]
    location_defs = [
        {"id": 59, "name": "Slaughterhouse Tripbomb", "type": "sprite"},
        {"id": 75, "name": "Conveyer Upper RPG", "type": "sprite"},
        {"id": 98, "name": "Kitchen Vent Pipebombs", "type": "sprite"},
        {"id": 101, "name": "Kitchen Vent Steroids", "type": "sprite"},
        {"id": 102, "name": "Kitchen Vent Medkit", "type": "sprite"},
        {"id": 125, "name": "Inside DB  Freezethrower", "type": "sprite"},
        {"id": 140, "name": "Dog Kennel Pipebombs", "type": "sprite"},
        {"id": 150, "name": "Manager Room Tripbomb 1", "type": "sprite"},
        {"id": 151, "name": "Manager Room Tripbomb 2", "type": "sprite"},
        {"id": 198, "name": "Kitchen Red Key Card", "type": "sprite"},
        {"id": 217, "name": "Manager Room Armor", "type": "sprite"},
        {"id": 354, "name": "Kitchen Fryer Armor", "type": "sprite"},
        {"id": 355, "name": "Slaughterhouse Vent Medkit", "type": "sprite"},
        {"id": 413, "name": "Outside Atomic Health", "type": "sprite"},
        {"id": 414, "name": "Outside Pipebombs", "type": "sprite"},
        {"id": 416, "mp": True, "name": "MP Inside DB RPG", "type": "sprite"},
        {"id": 417, "name": "Kitchen Shotgun", "type": "sprite"},
        {"id": 418, "name": "Kitchen Corner Chaingun", "type": "sprite"},
        {"id": 423, "name": "Outside Steroids", "type": "sprite"},
        {"id": 563, "mp": True, "name": "Outside Sign Holo Duke", "type": "sprite"},
        {"id": 595, "name": "Slaughterhouse Devastator", "type": "sprite"},
        {"id": 663, "name": "Outside Sign Shrinker", "type": "sprite"},
        {"id": 664, "name": "Outside Sign Blue Key Card", "type": "sprite"},
        {"id": 679, "name": "Kitchen Back Night Vision Goggles", "type": "sprite"},
        {"id": 748, "name": "Kitchen Back Freezethrower", "type": "sprite"},
        {"id": 102, "name": "Dog Kennel Secret", "type": "sector"},
        {"id": 311, "name": "Kitchen Vent Secret", "type": "sector"},
        {"id": 313, "name": "Conveyer Upper Secret", "type": "sector"},
        {"id": 321, "name": "Kitchen Back Secret", "type": "sector"},
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
                "Outside Sign Holo Duke",
                "Outside Sign Blue Key Card",
            ],
        )

        kitchen_secret  = self.region(
            "Kitchen Vent",
            [
                "Kitchen Vent Pipebombs",
                "Kitchen Vent Steroids",
                "Kitchen Vent Medkit",
                "Kitchen Vent Secret",
            ],
        )
        # Can enter without crouch but cant exit, maybe hard difficulty?
        self.connect(ret, kitchen_secret, (r.jump & r.difficulty("medium")) | 
                     (self.blue_key & r.jump))
        
        inside_db_front = self.region(
            "Inside DB Front",
            [
                "MP Inside DB RPG",
                "Inside DB  Freezethrower",
            ],
        )
        inside_db_kitchen = self.region(
            "Inside DB Kitchen",
            [
                "Kitchen Red Key Card",
                "Kitchen Shotgun",
            ],
        )
        
        # Can jump in through kitchen secret or go in from outside
        self.connect(ret, inside_db_front, self.blue_key)
        self.connect(kitchen_secret, inside_db_kitchen, r.can_crouch)
        # Outside path requires shrinker to get to kitchen area, 
        # glitched logic allows jumpclip, only relevant if somebody plays easy+glitched
        self.connect(inside_db_front, inside_db_kitchen, r.crouch_jump | r.can_shrink)

        kitchen_corner = self.region(
            "Kitchen Corner",
            [
                "Kitchen Corner Chaingun",
            ],
        )
        # This one can be gotten by diagonal walking + crouch tap instead of having jump
        self.connect(inside_db_kitchen, kitchen_corner, r.can_crouch | r.jump)
        
        kitchen_fryer = self.region(
            "Kitchen Fryer",
            [
                "Kitchen Fryer Armor",
            ],
        )
        self.connect(inside_db_kitchen, kitchen_fryer, r.jump)

        kitchen_back_secret = self.region(
            "Kitchen Back Secret",
            [
                "Kitchen Back Freezethrower",
                "Kitchen Back Secret",
            ],
        )
        # Can jump instead of duck to activate switch at desk
        self.connect(inside_db_kitchen, kitchen_back_secret, (r.jump & r.difficulty("medium")) | r.jump & r.can_crouch)

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
                "Slaughterhouse Tripbomb",
            ],
        )
        self.connect(slaughterhouse, conveyers, r.difficulty("medium") | r.explosives)

        conveyers_upper = self.region(
            "Slaughterhouse Conveyers Upper",
            [
                "Conveyer Upper Secret",
                "Conveyer Upper RPG",
            ],
        )
        self.connect(conveyers, conveyers_upper, r.jump)

        dog_kennel = self.region(
            "Dog Kennel Secret",
            [
                "Dog Kennel Secret",
                "Dog Kennel Pipebombs",
            ],
        )
        self.connect(conveyers_upper, dog_kennel, r.jump & r.explosives)

        manager_room = self.region(
            "Manager Room",
            [
                "Manager Room Tripbomb 1",
                "Manager Room Tripbomb 2",
                "Exit", 
            ],
        )
        self.connect(conveyers_upper, manager_room)

        manager_room_cabinet = self.region(
            "Manager Room Cabinet",
            [
                "Manager Room Armor",
            ],
        )
        self.connect(manager_room, manager_room_cabinet, r.jump)