from BaseClasses import Region

from ..base_classes import D3DLevel


class E1L2(D3DLevel):
    name = "Red Light District"
    levelnum = 1
    volumenum = 0
    keys = ["Blue", "Red", "Yellow"]
    location_defs = [
        {"name": "Blue Key Card", "id": 27, "type": "sprite"},
        {"name": "Sewers Jetpack", "id": 51, "type": "sprite"},
        {"name": "Sewers Night Vision Goggles", "id": 52, "type": "sprite"},
        {"name": "Sewers Steroids", "id": 53, "type": "sprite"},
        {"name": "Sewers Holo Duke", "id": 54, "type": "sprite"},
        {"name": "Vent Pipebombs", "id": 63, "type": "sprite"},
        {
            "name": "MP Steroids outside Strip Floor",
            "id": 120,
            "type": "sprite",
            "mp": True,
        },
        {"name": "Night Vision Goggles behind Curtains", "id": 170, "type": "sprite"},
        {"name": "Strippers Chaingun", "id": 174, "type": "sprite"},
        {"name": "Yellow Key Card", "id": 179, "type": "sprite"},
        {"name": "Dark Area Atomic Health", "id": 183, "type": "sprite"},
        {"name": "Toilets Night Vision Goggles", "id": 186, "type": "sprite"},
        {"name": "Pornography Store Shelves Pipebombs", "id": 188, "type": "sprite"},
        {"name": "Pornography Store Shelves Armor", "id": 189, "type": "sprite"},
        {"name": "Video Booth RPG", "id": 192, "type": "sprite"},
        {"name": "Pornography Store Corner Holo Duke", "id": 208, "type": "sprite"},
        {"name": "Red Key Card", "id": 249, "type": "sprite"},
        {"name": "Sewers Atomic Health", "id": 260, "type": "sprite"},
        {"name": "Sewers Pipebombs", "id": 265, "type": "sprite"},
        {"name": "Attic Medkit", "id": 278, "type": "sprite"},
        {"name": "MP Outside Ledge Jetpack", "id": 366, "type": "sprite", "mp": True},
        {"name": "Outside Ledge Armor", "id": 367, "type": "sprite"},
        {"name": "Strip Club Entrance Shotgun", "id": 391, "type": "sprite"},
        {
            "name": "Video Booth Steroids",
            "id": 407,
            "type": "sprite",
            "sprite_type": "trashcan",
        },
        {"name": "Chaingun near Blue Key Card", "id": 442, "type": "sprite"},
        {"name": "Vent Atomic Health", "id": 497, "type": "sprite"},
        {"name": "Pornography Store Shotgun", "id": 515, "type": "sprite"},
        {"name": "MP Bar RPG", "id": 751, "type": "sprite", "mp": True},
        {"name": "Pornography Store Atomic Health", "id": 822, "type": "sprite"},
        {"name": "Construction Site Medkit", "id": 823, "type": "sprite"},
        {
            "name": "MP DukeTag Outside Ledge Spawn Pipebombs",
            "id": 824,
            "type": "sprite",
            "mp": True,
        },  # This appears inaccessible in single player
        {"name": "Secret Strip Club Vents", "id": 91, "type": "sector"},
        {"name": "Secret Hidden Ledge behind Curtains", "id": 107, "type": "sector"},
        {"name": "Secret Pornography Store Corner", "id": 158, "type": "sector"},
        {"name": "Secret Pornography Store Shelves", "id": 161, "type": "sector"},
        {"name": "Secret Pornography Store Dark Area", "id": 172, "type": "sector"},
        {"name": "Secret Behind Strippers", "id": 177, "type": "sector"},
        {"name": "Secret Attic Hidden Compartment", "id": 187, "type": "sector"},
        {"name": "Secret Sewers", "id": 218, "type": "sector"},
        {"name": "Exit", "id": 0, "type": "exit"},
    ]

    def main_region(self) -> Region:
        r = self.rules
        ret = self.region(self.name)

        streets = self.region(
            "Streets",
            [
                "Secret Pornography Store Shelves",
                "Pornography Store Shelves Armor",
                "Pornography Store Shelves Pipebombs",
                "Pornography Store Shotgun",
                "Secret Pornography Store Dark Area",
                "Dark Area Atomic Health",
                "Video Booth Steroids",
                "Video Booth RPG",
                "Toilets Night Vision Goggles",
                "Chaingun near Blue Key Card",
                "Blue Key Card",
            ],
        )
        self.connect(ret, streets, r.can_crouch)

        streets_ledge = self.region(
            "Streets Ledge",
            [
                "MP Outside Ledge Jetpack",
                "Outside Ledge Armor",
                "Pornography Store Atomic Health",
            ],
        )
        self.connect(streets, streets_ledge, r.jump)

        store_corner = self.region(
            "Pornogrpahy Store Corner",
            [
                "Pornography Store Corner Holo Duke",
                "Secret Pornography Store Corner",
            ],
        )
        # can't fit up with jetpack
        self.connect(streets, store_corner, r.can_jump)

        strip_club = self.region(
            "Strip Club",
            [
                "Strip Club Entrance Shotgun",
                "MP Steroids outside Strip Floor",
                "MP Bar RPG",
                "Red Key Card",
            ],
        )
        self.restrict("Red Key Card", r.can_crouch)
        self.connect(streets, strip_club, self.yellow_key)

        sewers = self.region(
            "Sewers",
            [
                "Secret Sewers",
                "Sewers Steroids",
                "Sewers Pipebombs",
                "Sewers Atomic Health",
                "Sewers Night Vision Goggles",
                "Sewers Holo Duke",
                "Sewers Jetpack",
            ],
        )
        # One way connection only
        self.connect(strip_club, sewers, r.true)

        construction_site = self.region(
            "Construction Site", ["Construction Site Medkit", "Yellow Key Card"]
        )
        self.connect(
            streets,
            construction_site,
            (self.blue_key | (r.glitched & r.can_crouch)) & r.jump,
        )  # Can press button from outside

        # Can get to sewers, but the unlock for the door is on the other side only, so no connection to strip club
        self.connect(construction_site, sewers, r.explosives)
        # Can't survive pipe bomb or RPG explosion going up from the sewer
        self.connect(
            strip_club,
            construction_site,
            r.difficulty("medium")
            & ((r.devastator & r.jetpack(50)) | r.tripmine & r.jetpack(100)),
        )

        dance_floor = self.region(
            "Dance Floor",
            [
                "Secret Strip Club Vents",
                "Vent Atomic Health",
                "Vent Pipebombs",
                "Secret Behind Strippers",
                "Strippers Chaingun",
                "Secret Hidden Ledge behind Curtains",
                "Night Vision Goggles behind Curtains",
                "Attic Medkit",
                "Secret Attic Hidden Compartment",
                "Exit",
            ],
        )
        # Can't do anything in this without jumping, but does not require crouch to enter the vent
        self.connect(strip_club, dance_floor, self.red_key & r.jump)
        # Need to be able to run or jetpack to reach ledge
        self.restrict(
            "Secret Hidden Ledge behind Curtains",
            r.can_sprint | r.jetpack(50),
        )
        self.restrict(
            "Night Vision Goggles behind Curtains",
            r.can_sprint | r.jetpack(50),
        )

        return ret
