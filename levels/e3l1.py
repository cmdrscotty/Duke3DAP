from BaseClasses import Region

from ..base_classes import D3DLevel


class E3L1(D3DLevel):
    name = "Raw Meat"
    levelnum = 0
    volumenum = 2
    keys = ["Blue", "Red"]
    location_defs = [
        {"id": 78, "name": "Booth Jetpack", "type": "sprite"},
        {"id": 115, "name": "Start Ledge Chaingun", "type": "sprite"},
        {"id": 116, "name": "Start Ledge Atomic Health", "type": "sprite"},
        {"id": 161, "name": "Sushi Belt Atomic Health", "type": "sprite"},
        {"id": 305, "name": "Sushi Belt Freezethrower", "type": "sprite"},
        {"id": 308, "name": "Start Pit Atomic Health", "type": "sprite"},
        {"id": 309, "name": "Start Pit Pipebombs", "type": "sprite"},
        {"id": 389, "name": "Sushi Belt Steroids", "type": "sprite"},
        {"id": 452, "name": "Blue Key Card", "type": "sprite"},
        {"id": 457, "name": "Red Key Card", "type": "sprite"},
        {"id": 492, "name": "Booth Shotgun", "type": "sprite"},
        {"id": 497, "name": "Hallway Poster Shrinker", "type": "sprite"},
        {"id": 499, "name": "Booth Backroom Steroids", "type": "sprite"},
        {"id": 500, "name": "Booth Medkit", "type": "sprite"},
        {"id": 524, "name": "Karaoke RPG", "type": "sprite"},
        {"id": 536, "name": "Stove Jetpack", "type": "sprite"},
        {"id": 543, "name": "Start Pool Pipebombs", "type": "sprite"},
        {"id": 561, "name": "Sink Atomic Health", "type": "sprite"},
        {"id": 564, "name": "Kitchen Armor", "type": "sprite"},
        {"id": 569, "name": "Kitchen Vent Tripmine", "type": "sprite"},
        {"id": 570, "name": "Sushi Belt Night Vision Goggles", "type": "sprite"},
        {"id": 574, "density": 5, "name": "MP Garage Door Shotgun", "type": "sprite"},
        {"id": 575, "density": 5, "name": "MP Booth Chaingun", "type": "sprite"},
        {"id": 577, "density": 5, "name": "MP Garage Pool Medkit", "type": "sprite"},
        {"id": 608, "name": "Start Devastator", "type": "sprite"},
        {"id": 609, "name": "Start Pool Holo Duke", "type": "sprite"},
        {"id": 624, "name": "Sushi Belt Cupboard Pipebombs", "type": "sprite"},
        {"id": 632, "name": "Garage Door Scuba Gear", "type": "sprite"},
        {"id": 636, "name": "Hallway Armor", "type": "sprite"},
        {"id": 656, "name": "Night Vision Goggles behind Urn", "type": "sprite"},
        {"id": 135, "name": "Secret Geisha Wall", "type": "sector"},
        {"id": 137, "name": "Secret Hallway Sign", "type": "sector"},
        {"id": 161, "name": "Secret Sushi Belt Wall", "type": "sector"},
        {"id": 287, "name": "Secret Wine Cabinet", "type": "sector"},
        {"id": 332, "name": "Secret Sushi Belt Cupboard", "type": "sector"},
        {"id": 338, "name": "Secret Hallway Wall", "type": "sector"},
        {"id": 344, "name": "Secret Hallway Poster", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
    events = ["Backrooms Switch"]
    must_dive = True

    def main_region(self) -> Region:
        r = self.rules
        ret = self.region(
            self.name,
            [
                "Start Devastator",
                "Booth Jetpack",
                "Booth Shotgun",
                "Booth Medkit",
                "MP Booth Chaingun",
                "Night Vision Goggles behind Urn",
                "Secret Hallway Sign",
                "Hallway Armor",
                "Secret Hallway Wall",
                "Secret Geisha Wall",
            ],
        )
        self.restrict("Secret Hallway Sign", r.jump)
        self.restrict("Hallway Armor", r.jump)
        self.restrict("Secret Hallway Wall", r.explosives)
        self.restrict(
            "Secret Geisha Wall", r.jump | r.can_crouch
        )  # Can crouch into the wall from the sign

        start_ledge = self.region(
            "Start Ledge", ["Start Ledge Chaingun", "Start Ledge Atomic Health"]
        )
        self.connect(ret, start_ledge, r.can_sprint | r.jump)

        start_pool = self.region(
            "Start Pool", ["Start Pool Holo Duke", "Start Pool Pipebombs"]
        )
        self.connect(ret, start_pool, r.can_dive)

        starting_ledges = self.region(
            "Start Pit",
            [
                "Start Pit Atomic Health",
                "Start Pit Pipebombs",
                "Secret Hallway Poster",
                "Hallway Poster Shrinker",
            ],
        )
        # Can get on these by stepping up over enemies
        self.connect(ret, starting_ledges, r.jump | r.difficulty("hard"))

        booth_backroom = self.region(
            "Booth Backroom", ["Backrooms Switch", "Booth Backroom Steroids"]
        )
        self.connect(
            ret,
            booth_backroom,
            r.can_crouch & r.jump | (r.difficulty("medium") & r.can_jump),
        )  # can get in with just jetpack but we're stuck then, possible to clip in and out with jump

        hatch_room = self.region(
            "Hatching Room",
            ["Blue Key Card", "MP Garage Door Shotgun", "Garage Door Scuba Gear"],
        )
        self.connect(ret, hatch_room, self.event("Backrooms Switch"))

        garage_pool = self.region(
            "Garage Pool", ["MP Garage Pool Medkit", "Red Key Card"]
        )
        self.connect(hatch_room, garage_pool, r.can_dive)
        # clipping from here to the kitchen sink was a EDuke32 only bug, I think

        club_room = self.region(
            "Club Room",
            [
                "Karaoke RPG",
                "Secret Sushi Belt Wall",
                "Sushi Belt Freezethrower",
                "Sushi Belt Night Vision Goggles",
                "Kitchen Armor",
                "Secret Wine Cabinet",
            ],
        )
        self.connect(
            ret,
            club_room,
            self.blue_key
            | (
                r.difficulty("medium")
                & (
                    (r.glitched & r.steroids & r.can_crouch & r.can_sprint)
                    | r.crouch_jump
                )
            ),
        )

        sushi_belt_cupboard = self.region(
            "Sushi Belt Cupboard",
            ["Secret Sushi Belt Cupboard", "Sushi Belt Cupboard Pipebombs"],
        )
        self.connect(club_room, sushi_belt_cupboard, r.can_crouch)

        kitchen_ledges = self.region(
            "Kitchen Ledges",
            [
                "Sushi Belt Atomic Health",
                "Sushi Belt Steroids",
                "Stove Jetpack",
                "Sink Atomic Health",
                "Kitchen Vent Tripmine",
            ],
        )
        self.connect(
            club_room, kitchen_ledges, r.jump
        )  # there might be a way to clip up the ledges

        garage = self.region("Garage", ["Exit"])
        # Tripclip never disappoints
        self.connect(
            club_room,
            garage,
            self.red_key
            | (
                r.difficulty("extreme")
                & r.glitched
                & (r.steroids | r.can_sprint)
                & r.tripmine
                & r.can_jump
            ),
        )
        self.restrict("Exit", r.jump)
        return ret
