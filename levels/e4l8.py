from BaseClasses import Region

from ..base_classes import D3DLevel


class E4L8(D3DLevel):
    name = "Critical Mass"
    levelnum = 7
    volumenum = 3
    keys = ["Red", "Blue", "Yellow"]
    location_defs = [
        {"id": 313, "name": "Warehouse Vent Night Vision Goggles", "type": "sprite"},
        {"id": 323, "mp": True, "name": "MP Bookshelf Jetpack", "type": "sprite"},
        {"id": 344, "name": "Control Freezethrower", "type": "sprite"},
        {"id": 351, "name": "Control Armor", "type": "sprite"},
        {"id": 352, "name": "Control Shotgun", "type": "sprite"},
        {"id": 386, "name": "Blue Key Card", "type": "sprite"},
        {"id": 456, "name": "Homer Atomic Health", "type": "sprite"},
        {"id": 479, "name": "Explosion Lower Medkit", "type": "sprite"},
        {"id": 532, "name": "Explosion Lower Devastator", "type": "sprite"},
        {"id": 533, "name": "Explosion Lower Atomic Health", "type": "sprite"},
        {"id": 538, "name": "Explosion Lower Pipebombs", "type": "sprite"},
        {"id": 613, "name": "Front Upper Armor", "type": "sprite"},
        {"id": 614, "name": "Warehouse Atomic Health", "type": "sprite"},
        {"id": 648, "name": "Explosion Chaingun", "type": "sprite"},
        {"id": 713, "name": "Outside Pipebombs", "type": "sprite"},
        {"id": 714, "name": "Warehouse Shotgun", "type": "sprite"},
        {"id": 724, "name": "Explosion Lower Holo Duke", "type": "sprite"},
        {"id": 733, "name": "Storage Medkit", "type": "sprite"},
        {"id": 734, "name": "Storage Steroids", "type": "sprite"},
        {"id": 735, "name": "Explosion Lower Protective Boots", "type": "sprite"},
        {"id": 761, "name": "Blue Dive Atomic Health", "type": "sprite"},
        {"id": 762, "name": "Yellow Key Card", "type": "sprite"},
        {"id": 827, "name": "Blue Upper Shrinker", "type": "sprite"},
        {"id": 830, "name": "Blue Chaingun", "type": "sprite"},
        {"id": 834, "name": "Blue Secret RPG", "type": "sprite"},
        {"id": 835, "name": "Storage Tripmine 1", "type": "sprite"},
        {"id": 836, "name": "Storage Tripmine 2", "type": "sprite"},
        {"id": 854, "name": "Red Key Card", "type": "sprite"},
        {"id": 863, "name": "Explosion Lower Scuba Gear", "type": "sprite"},
        {"id": 864, "mp": True, "name": "MP Explosion RPG", "type": "sprite"},
        {"id": 868, "mp": True, "name": "MP Outside Freezethrower", "type": "sprite"},
        {"id": 105, "name": "Secret Explosion Lower", "type": "sector"},
        {"id": 116, "name": "Secret Homer", "type": "sector"},
        {"id": 234, "name": "Secret Blue Area", "type": "sector"},
        {"id": 240, "name": "Secret Blue Upper", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
    must_dive = True
    events = ["Meltdown"]

    def main_region(self) -> Region:
        r = self.rules
        ret = self.region(
            self.name,
            [
                "Outside Pipebombs",
                "MP Outside Freezethrower",
            ],
        )

        front_upper = self.region(
            "Front Upper",
            [
                "Front Upper Armor",
                "Warehouse Atomic Health",
                "Warehouse Shotgun",
                "Warehouse Vent Night Vision Goggles",
                "Explosion Chaingun",
                "Secret Homer",
                "Homer Atomic Health",
                "MP Explosion RPG",
            ],
        )
        self.connect(ret, front_upper, r.jump)

        expl_lower = self.region(
            "Explosion Lower",
            [
                "Explosion Lower Atomic Health",
                "Explosion Lower Pipebombs",
                "Explosion Lower Scuba Gear",
                "Secret Explosion Lower",
                "Explosion Lower Medkit",
                "Explosion Lower Devastator",
                "Explosion Lower Holo Duke",
                "Explosion Lower Protective Boots",
            ],
        )
        self.connect(front_upper, expl_lower, r.can_crouch & r.can_dive)

        upper_storage = self.region(
            "Storage Upper Area",
            [
                "Storage Steroids",
                "Storage Tripmine 1",
                "Storage Tripmine 2",
            ],
        )
        self.connect(expl_lower, upper_storage, r.jump)

        control_room = self.region(
            "Control Room",
            [
                "Storage Medkit",
                "Control Freezethrower",
                "Control Armor",
                "Control Shotgun",
                "Blue Key Card",
            ],
        )
        self.connect(expl_lower, control_room)

        blue_key_area = self.region(
            "Blue Key Area",
            [
                "Secret Blue Area",
                "Blue Secret RPG",
                "Blue Chaingun",
            ],
        )
        self.connect(control_room, blue_key_area, self.blue_key)

        blue_upper = self.region(
            "Blue Key Upper Area",
            [
                "Secret Blue Upper",
                "Blue Upper Shrinker",
            ],
        )
        # 75 is generous, 60 could be enough
        self.connect(blue_key_area, blue_upper, r.jetpack(75))

        blue_dive = self.region(
            "Blue Dive Area",
            [
                "Blue Dive Atomic Health", 
                "Yellow Key Card", 
                "Meltdown"
            ],
        )
        self.connect(blue_key_area, blue_dive, r.can_dive)

        yellow_key_area = self.region(
            "Yellow Key Area",
            [],
        )
        self.connect(control_room, yellow_key_area, self.yellow_key)

        yellow_bookshelf = self.region(
            "Office Bookshelf",
            [
                "MP Bookshelf Jetpack",
                "Red Key Card",
            ],
        )
        # Can clip up the bookshelf by using the door
        self.connect(yellow_key_area, yellow_bookshelf, r.jump | r.difficulty("Hard"))

        red_key_area = self.region(
            "Red Key Area",
            [
                "Exit",
            ],
        )
        self.connect(
            yellow_key_area,
            red_key_area,
            self.red_key & r.can_crouch & r.jump & self.event("Meltdown"),
        )
        return ret
