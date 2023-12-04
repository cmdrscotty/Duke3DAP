from BaseClasses import Region

from ..base_classes import D3DLevel


class E3L7(D3DLevel):
    name = "Fahrenheit"
    levelnum = 6
    volumenum = 2
    keys = ["Blue", "Red", "Yellow"]
    location_defs = [
        {"id": 39, "name": "Pool Shotgun", "type": "sprite"},
        {"id": 60, "name": "Building Night Vision Goggles", "type": "sprite"},
        {"id": 77, "mp": True, "name": "MP Broadcast Jetpack", "type": "sprite"},
        {"id": 80, "name": "Building Freezethrower", "type": "sprite"},
        {"id": 88, "name": "Fire Station Medkit", "type": "sprite"},
        {"id": 89, "name": "Fire Truck Holo Duke", "type": "sprite"},
        {"id": 134, "name": "Blue Key Card", "type": "sprite"},
        {"id": 192, "name": "Window Medkit", "type": "sprite"},
        {"id": 202, "name": "Passage Armor", "type": "sprite"},
        {"id": 203, "mp": True, "name": "MP Crates Jetpack", "type": "sprite"},
        {"id": 259, "name": "Crates Atomic Health", "type": "sprite"},
        {"id": 268, "name": "Pool Ledge Pipebombs", "type": "sprite"},
        {"id": 294, "name": "Broadcast Devastator", "type": "sprite"},
        {"id": 295, "name": "Red Key Card", "type": "sprite"},
        {"id": 299, "name": "Set Chaingun", "type": "sprite"},
        {"id": 334, "name": "Wine Rack Medkit", "type": "sprite"},
        {"id": 335, "name": "Building Steroids", "type": "sprite"},
        {"id": 344, "name": "Pool Shrinker", "type": "sprite"},
        {"id": 347, "name": "Broadcast Tripmine", "type": "sprite"},
        {"id": 348, "name": "Building Tripmine", "type": "sprite"},
        {"id": 368, "name": "Exit RPG", "type": "sprite"},
        {"id": 422, "name": "Pool Medkit", "type": "sprite"},
        {"id": 426, "name": "Fire Station RPG", "type": "sprite"},
        {"id": 429, "name": "Fire Station Atomic Health", "type": "sprite"},
        {"id": 430, "name": "Curtain Atomic Health", "type": "sprite"},
        {"id": 431, "name": "Broadcast Shotgun", "type": "sprite"},
        {"id": 432, "name": "Yellow Key Card", "type": "sprite"},
        {"id": 111, "name": "Secret Broadcast", "type": "sector"},
        {"id": 133, "name": "Secret Wine Rack", "type": "sector"},
        {"id": 176, "name": "Secret Painting", "type": "sector"},
        {"id": 179, "name": "Secret Curtain", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
    must_dive = True

    def main_region(self) -> Region:
        r = self.rules
        # can't go anywhere at the start, sad
        ret = self.region(self.name, [])

        start_ledges = self.region("Start Ledges", ["Pool Ledge Pipebombs"])
        self.connect(ret, start_ledges, r.jump)

        pool = self.region(
            "Pool", ["Pool Shotgun", "Pool Shrinker", "Pool Medkit", "Blue Key Card"]
        )
        self.connect(start_ledges, pool, r.can_dive)

        exit_area = self.region("Exit Area", ["Exit RPG", "Exit"])
        self.connect(pool, exit_area, self.red_key)
        self.restrict("Exit", r.jump & r.explosives)

        plaza = self.region("Plaza", ["Passage Armor", "Fire Station Medkit"])
        # pretty tricky jump off a flying lizard trooper
        self.connect(
            ret,
            plaza,
            self.blue_key | r.jetpack(50) | (r.difficulty("hard") & r.can_jump),
        )

        plaza_ledges = self.region(
            "Plaza ledges",
            [
                "Fire Truck Holo Duke",
                "MP Crates Jetpack",
                "Crates Atomic Health",
                "Window Medkit",
                "Building Tripmine",
                "Building Freezethrower",
                "Building Night Vision Goggles",
                "Building Steroids",
                "Wine Rack Medkit",
                "Secret Wine Rack",
                "Secret Painting",
            ],
        )
        self.connect(plaza, plaza_ledges, r.jump)

        fire_station = self.region(
            "Fire Station",
            ["Fire Station RPG", "Fire Station Atomic Health", "Yellow Key Card"],
        )
        # This one doesn't even require sprinting speed to clip into
        self.connect(
            plaza, fire_station, r.explosives | r.glitched & r.can_jump & r.can_crouch
        )

        broadcast = self.region(
            "Broadcast Building",
            [
                "Secret Broadcast",
                "MP Broadcast Jetpack",
                "Red Key Card",
                "Broadcast Tripmine",
                "Broadcast Devastator",
                "Set Chaingun",
                "Curtain Atomic Health",
                "Secret Curtain",
            ],
        )
        self.connect(plaza, broadcast, self.yellow_key)

        broadcast_top = self.region("Top of Broadcast Building", ["Broadcast Shotgun"])
        self.connect(
            plaza, broadcast_top, r.jetpack(50) | (r.difficulty("medium") & r.can_jump)
        )
        self.connect(broadcast, broadcast_top, r.true)
        return ret
