from BaseClasses import Region

from ..base_classes import D3DLevel


class E1L6(D3DLevel):
    name = "Launch Facility"
    levelnum = 5
    volumenum = 0
    keys = ["Blue", "Red"]
    location_defs = [
        {"name": "Rocket Jetpack", "id": 0, "type": "sprite"},
        {"name": "Toxic Waste Pool Shotgun", "id": 123, "type": "sprite"},
        {"name": "Start Protective Boots", "id": 124, "type": "sprite"},
        {"name": "Outside Rocket Night Vision Goggles", "id": 385, "type": "sprite"},
        {"name": "Dark Room RPG", "id": 395, "type": "sprite"},
        {"name": "Dark Room Pipebombs 1", "id": 397, "type": "sprite"},
        {"name": "Dark Room Pipebombs 2", "id": 398, "type": "sprite"},
        {"name": "Spiral Chaingun", "id": 406, "type": "sprite"},
        {"name": "Dark Room Atomic Health", "id": 410, "type": "sprite"},
        {"name": "Blue Key Card", "id": 518, "type": "sprite"},
        {"name": "Red Key Card", "id": 539, "type": "sprite"},
        {"name": "Sewer Computers Atomic Health 1", "id": 561, "type": "sprite"},
        {"name": "Sewer Computers Atomic Health 2", "id": 562, "type": "sprite"},
        {"name": "Sewer Computers Atomic Health 3", "id": 563, "type": "sprite"},
        {"name": "Sewer Protective Boots", "id": 567, "type": "sprite"},
        {"name": "Dark Room Medkit", "id": 575, "type": "sprite"},
        {"name": "Toxic Waste Pool Atomic Health 2", "id": 588, "type": "sprite"},
        {"name": "Toxic Waste Pool Atomic Health 1", "id": 589, "type": "sprite"},
        {"name": "MP Spiral Holo Duke", "id": 625, "type": "sprite", "mp": True},
        {"name": "Vent Pipebombs", "id": 642, "type": "sprite"},
        {"name": "Launch Room Steroids", "id": 643, "type": "sprite"},
        {"name": "Start Armor", "id": 647, "type": "sprite"},
        {"name": "MP Start Steroids", "id": 690, "type": "sprite", "mp": True},
        {"name": "MP Rocket Pit Pipebombs", "id": 691, "type": "sprite", "mp": True},
        {"name": "MP Toxic Waste Pool RPG", "id": 692, "type": "sprite", "mp": True},
        {"name": "MP Rocket Chaingun", "id": 693, "type": "sprite", "mp": True},
        {"name": "MP Gate Room Shotgun", "id": 696, "type": "sprite", "mp": True},
        {"name": "Launch Room Holo Duke", "id": 697, "type": "sprite"},
        {"name": "Gate Room Armor", "id": 707, "type": "sprite"},
        {"name": "MP Start Jetpack", "id": 726, "type": "sprite", "mp": True},
        {"name": "Secret Sewer Computers", "id": 218, "type": "sector"},
        {"name": "Secret Toxic Waste Pool", "id": 224, "type": "sector"},
        {"name": "Secret Dark Room Ceiling Vent", "id": 277, "type": "sector"},
        {"name": "Secret Gate Room Wall", "id": 327, "type": "sector"},
        {"name": "Exit", "id": 0, "type": "exit"},
    ]
    must_dive = True

    def main_region(self) -> Region:
        r = self.rules
        ret = self.region(
            self.name,
            [
                "MP Start Jetpack",
                # can just walk off
                "MP Start Steroids",
                "Start Protective Boots",
                "Start Armor",
                "Spiral Chaingun",
                "MP Spiral Holo Duke",
                "Blue Key Card",
                "Dark Room Pipebombs 1",
                "Dark Room Pipebombs 2",
                "Dark Room RPG",
                "Dark Room Medkit",
                "Dark Room Atomic Health",
            ],
        )
        self.restrict("Dark Room Atomic Health", r.can_sprint | r.jump)

        waste_pool = self.region(
            "Secret Toxic Waste Pool",
            [
                "Secret Toxic Waste Pool",
                "Toxic Waste Pool Shotgun",
                "Toxic Waste Pool Atomic Health 1",
                "Toxic Waste Pool Atomic Health 2",
                "MP Toxic Waste Pool RPG",
            ],
        )
        self.connect(ret, waste_pool, r.can_dive)

        vent = self.region(
            "Dark Room Vent", ["Secret Dark Room Ceiling Vent", "Vent Pipebombs"]
        )
        # Plenty of lizard troopers to jump on
        self.connect(ret, vent, r.jetpack(50) | (r.difficulty("medium") & r.can_jump))

        launch_pad = self.region(
            "Launch Pad",
            [
                "MP Gate Room Shotgun",
                "Red Key Card",
                "Secret Gate Room Wall",
                "Gate Room Armor",
                "Outside Rocket Night Vision Goggles",
                "Rocket Jetpack",
                "MP Rocket Chaingun",
            ],
        )
        self.connect(ret, launch_pad, self.blue_key | r.crouch_jump)

        launch_room = self.region(
            "Launch Room", ["Launch Room Steroids", "Launch Room Holo Duke"]
        )
        self.connect(launch_pad, launch_room, r.can_crouch)

        rocket_pit = self.region("Rocket Pit", ["MP Rocket Pit Pipebombs", "Exit"])
        # Need to get out of the launch room again. Might be possible to activate this from outside somehow?
        self.connect(launch_room, rocket_pit, self.red_key & r.jump)

        sewer_ledge = self.region(
            "Sewer Ledge",
            [
                "Secret Sewer Computers",
                "Sewer Computers Atomic Health 1",
                "Sewer Computers Atomic Health 2",
                "Sewer Computers Atomic Health 3",
                "Sewer Protective Boots",
            ],
        )
        # Can clip up the slope by walking into the corner of it
        self.connect(rocket_pit, sewer_ledge, r.jump | r.difficulty("medium"))

        return ret
