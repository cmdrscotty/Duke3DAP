from BaseClasses import Region

from ..base_classes import D3DLevel


class E3L8(D3DLevel):
    name = "Hotel Hell"
    levelnum = 7
    volumenum = 2
    keys = ["Blue", "Yellow"]
    location_defs = [
        {"id": 85, "name": "Shark Tank Atomic Health", "type": "sprite"},
        {"id": 86, "name": "Shark Tank Scuba Gear 2", "type": "sprite"},
        {"id": 99, "name": "Hallway Night Vision Goggles", "type": "sprite"},
        {"id": 152, "name": "Hotel Room Vent Shrinker", "type": "sprite"},
        {"id": 172, "name": "Yellow Key Card", "type": "sprite"},
        {"id": 175, "name": "Toilet RPG", "type": "sprite"},
        {"id": 182, "name": "Dive Board Pipebombs", "type": "sprite"},
        {"id": 285, "name": "Toilet Atomic Health", "type": "sprite"},
        {"id": 355, "name": "Outside Vent Steroids", "type": "sprite"},
        {"id": 358, "name": "Apartment Devastator", "type": "sprite"},
        {"id": 372, "name": "Blue Key Card", "type": "sprite"},
        {
            "id": 386,
            "name": "Trashcan Pipebombs",
            "type": "sprite",
            "sprite_type": "trashcan",
        },
        {"id": 392, "name": "Dumpster Medkit", "type": "sprite"},
        {"id": 395, "name": "Dumpster Chaingun", "type": "sprite"},
        {"id": 397, "name": "Ledge Shotgun", "type": "sprite"},
        {"id": 423, "name": "Streets Atomic Health 1", "type": "sprite"},
        {"id": 460, "name": "Hotel Room Armor", "type": "sprite"},
        {"id": 478, "name": "Corner Tripmine 1", "type": "sprite"},
        {"id": 479, "name": "Corner Tripmine 2", "type": "sprite"},
        {"id": 564, "name": "Streets Atomic Health 2", "type": "sprite"},
        {"id": 575, "name": "Shark Tank Pipebombs", "type": "sprite"},
        {"id": 576, "name": "Shark Tank Medkit", "type": "sprite"},
        {"id": 577, "name": "Viewpoint Holo Duke", "type": "sprite"},
        {"id": 592, "name": "Shark Tank Scuba Gear 1", "type": "sprite"},
        {"id": 596, "name": "Wine Rack Holo Duke", "type": "sprite"},
        {"id": 657, "name": "Lobby Night Vision Goggles", "type": "sprite"},
        {"id": 663, "name": "Lobby Armor", "type": "sprite"},
        {"id": 667, "name": "Lobby Medkit", "type": "sprite"},
        {"id": 684, "mp": True, "name": "MP Lobby Jetpack", "type": "sprite"},
        {"id": 685, "mp": True, "name": "MP Staircase Armor", "type": "sprite"},
        {"id": 688, "mp": True, "name": "MP Streets Chaingun", "type": "sprite"},
        {"id": 690, "mp": True, "name": "MP Hallway Freezethrower", "type": "sprite"},
        {"id": 725, "name": "Shark Tank Freezethrower", "type": "sprite"},
        {"id": 769, "name": "Indiana Jones Atomic Health", "type": "sprite"},
        {"id": 823, "name": "Exit Pipebombs", "type": "sprite"},
        {"id": 827, "name": "Jungle Freezethrower", "type": "sprite"},
        {"id": 138, "name": "Secret Shark Tank", "type": "sector"},
        {"id": 155, "name": "Secret Wine Rack", "type": "sector"},
        {"id": 284, "name": "Secret Indiana Jones", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
        {"id": 11, "name": "Secret Exit", "type": "exit"},
    ]
    events = ["Windows Opened"]
    must_dive = True

    def main_region(self) -> Region:
        r = self.rules
        ret = self.region(self.name, ["Trashcan Pipebombs"])

        stadium_elevator = self.region("Stadium Elevator", ["Exit", "Exit Pipebombs"])
        # sure we can clip up somehow as well
        self.connect(ret, stadium_elevator, r.jump & r.pipebomb)

        entrance_ledges = self.region(
            "Entrance Ledges",
            [
                "Dumpster Chaingun",
                "Dumpster Medkit",
                "Ledge Shotgun",
                "Blue Key Card",
                "Outside Vent Steroids",
            ],
        )
        self.connect(ret, entrance_ledges, r.jump)
        self.connect(
            entrance_ledges,
            stadium_elevator,
            r.crouch_jump | (r.can_jump & self.event("Windows Opened")),
        )

        hotel_lobby = self.region(
            "Lobby",
            [
                "Toilet RPG",
                "Lobby Medkit",
                "MP Lobby Jetpack",
                "Lobby Night Vision Goggles",
                "MP Streets Chaingun",
                "Lobby Armor",
            ],
        )
        self.restrict("Lobby Armor", r.jump)
        self.connect(ret, hotel_lobby, self.blue_key)

        streets_ledge = self.region(
            "Streets Ledge", ["Streets Atomic Health 1", "Streets Atomic Health 2"]
        )
        # can probably jump on enemies
        self.connect(hotel_lobby, streets_ledge, r.jetpack(50))

        apartment = self.region(
            "Apartment Building", ["Yellow Key Card", "Apartment Devastator"]
        )
        self.connect(hotel_lobby, apartment, r.jump)

        upstairs = self.region(
            "Hotel Upstairs",
            [
                "MP Staircase Armor",
                "Secret Wine Rack",
                "Wine Rack Holo Duke",
                "Secret Shark Tank",
                "Shark Tank Scuba Gear 1",
                "Shark Tank Pipebombs",
                "Shark Tank Medkit",
                "Hotel Room Armor",
                "Hallway Night Vision Goggles",
                "MP Hallway Freezethrower",
                "Jungle Freezethrower",
                "Secret Exit",
                "Secret Indiana Jones",
                "Corner Tripmine 1",
                "Corner Tripmine 2",
            ],
        )
        # can clip up from the broken reception tv
        self.connect(hotel_lobby, upstairs, self.yellow_key | r.crouch_jump)
        # can walk out through exploding wall
        self.connect(upstairs, streets_ledge, r.true)

        upstairs_ledges = self.region(
            "Upstairs Ledges",
            [
                "Hotel Room Vent Shrinker",
                "Indiana Jones Atomic Health",
                "Dive Board Pipebombs",
                "Viewpoint Holo Duke",
                "Windows Opened",
            ],
        )
        self.connect(upstairs, upstairs_ledges, r.jump)

        shark_tank = self.region(
            "Shark Tank",
            [
                "Shark Tank Atomic Health",
                "Shark Tank Scuba Gear 2",
                "Shark Tank Freezethrower",
            ],
        )
        self.connect(upstairs, shark_tank, r.can_dive & r.jump)

        pool = self.region("Inside Pool", ["Toilet Atomic Health"])
        # There might be a different way to get here, maybe?
        self.connect(upstairs, pool, r.can_dive & r.explosives)
        return ret
