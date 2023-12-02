from BaseClasses import Region

from ..base_classes import D3DLevel


class E1L3(D3DLevel):
    name = "Death Row"
    levelnum = 2
    volumenum = 0
    keys = ["Blue", "Red", "Yellow"]
    location_defs = [
        {"name": "Control Room Secret Atomic Health", "id": 48, "type": "sprite"},
        {"name": "Control Room Vent Armor", "id": 79, "type": "sprite"},
        {"name": "Gallery Medkit", "id": 160, "type": "sprite"},
        {
            "name": "Cell Black 01 Broken Wall Atomic Health",
            "id": 185,
            "type": "sprite",
        },
        {"name": "Electric Chair Shotgun", "id": 236, "type": "sprite"},
        {"name": "Control Room Secret Pipebombs", "id": 269, "type": "sprite"},
        {"name": "Submarine Gate Scuba Gear", "id": 280, "type": "sprite"},
        {"name": "Gear Room Atomic Health", "id": 367, "type": "sprite"},
        {"name": "Cell BLock 01 RPG", "id": 411, "type": "sprite"},
        {"name": "MP Courtyard Medkit", "id": 413, "type": "sprite", "mp": True},
        {"name": "Yellow Key Card", "id": 485, "type": "sprite"},
        {"name": "Courtyard Tunnel Atomic Health 1", "id": 488, "type": "sprite"},
        {"name": "Courtyard Tunnel Atomic Health 2", "id": 489, "type": "sprite"},
        {"name": "Courtyard Tunnel Atomic Health 3", "id": 490, "type": "sprite"},
        {"name": "Submarine Engine Room Medkit", "id": 504, "type": "sprite"},
        {"name": "Underwater Pipebombs", "id": 532, "type": "sprite"},
        {"name": "Chapel Chaingun", "id": 564, "type": "sprite"},
        {"name": "MP Showers Shotgun", "id": 598, "type": "sprite"},
        {"name": "Showers Protective Boots", "id": 606, "type": "sprite"},
        {
            "name": "Hanged Monk Atomic Health",
            "id": 642,
            "type": "sprite",
            "sprite_type": "monk",
        },
        {"name": "Gallery Holo Duke", "id": 672, "type": "sprite"},
        {"name": "Chapel Rafters Armor", "id": 676, "type": "sprite"},
        {"name": "Chapel Rafters Atomic Health", "id": 677, "type": "sprite"},
        {"name": "Gear Room Night Vision Goggles", "id": 697, "type": "sprite"},
        {"name": "Blue Key Card", "id": 699, "type": "sprite"},
        {
            "name": "Submarine Gate Hidden Night Vision Goggles",
            "id": 803,
            "type": "sprite",
        },
        {"name": "Breakable Canyon Wall Steroids", "id": 813, "type": "sprite"},
        {"name": "Courtyard Pipebombs", "id": 847, "type": "sprite"},
        {"name": "Red Key Card", "id": 851, "type": "sprite"},
        {"name": "Gear Room RPG", "id": 856, "type": "sprite"},
        {
            "name": "MP Cell Block 01 Broken Wall Holo Duke",
            "id": 870,
            "type": "sprite",
            "mp": True,
        },
        {"name": "Control Room Chaingun", "id": 899, "type": "sprite"},
        {"name": "Chapel Window Steroids", "id": 902, "type": "sprite"},
        {"name": "MP Cell Block 02 Jetpack", "id": 903, "type": "sprite", "mp": True},
        {"name": "Courtyard Tunnel", "id": 76, "type": "sector"},
        {"name": "Electric Chair", "id": 296, "type": "sector"},
        {"name": "Chapel Rafters", "id": 304, "type": "sector"},
        {"name": "Chapel Window", "id": 317, "type": "sector"},
        {"name": "Behind Bed", "id": 379, "type": "sector"},
        {"name": "Submarine Engine Room", "id": 387, "type": "sector"},
        {"name": "Submarine Gate Hidden Alcove", "id": 393, "type": "sector"},
        {"name": "Breakable Canyon Wall", "id": 401, "type": "sector"},
        {"name": "Control Room Right Alcove", "id": 424, "type": "sector"},
        {"name": "Control Room Left Alcove", "id": 426, "type": "sector"},
        {"name": "Exit", "id": 0, "type": "exit"},
    ]
    events = ["Unlock Cell Blocks"]
    must_dive = True

    def main_region(self) -> Region:
        r = self.rules
        ret = self.region(self.name)

        electric_chair = self.region("Electric Chair")
        self.add_locations(["Electric Chair", "Electric Chair Shotgun"], electric_chair)
        self.connect(ret, electric_chair, r.can_crouch)

        hallway = self.region(
            "Main Hallway",
            [
                "Gallery Holo Duke",
                "Gallery Medkit",
                "Hanged Monk Atomic Health",
                "Chapel Rafters Atomic Health",
                "Chapel Rafters Armor",
                "Chapel Rafters",
                "Behind Bed",
            ],
        )
        self.connect(ret, hallway, r.jump)
        self.restrict("Behind Bed", r.can_crouch)

        altar = self.region(
            "Chapel Altar",
            ["Chapel Window Steroids", "Chapel Window", "Chapel Chaingun"],
        )
        self.connect(hallway, altar, r.jump)

        gears = self.region(
            "Gear Room",
            [
                "Gear Room RPG",
                "Blue Key Card",
                "Gear Room Night Vision Goggles",
                "Gear Room Atomic Health",
            ],
        )
        self.connect(hallway, gears, r.jump)

        # This is a bit weird, can not jetpack up, only exit from vent

        control_vent = self.region(
            "Hallway Vent",
            [
                "Control Room Vent Armor",
            ],
        )
        self.connect(hallway, control_vent, r.jetpack(50))

        control_room = self.region(
            "Control Room",
            [
                "Yellow Key Card",
                "MP Showers Shotgun",
                "Showers Protective Boots",
                "Cell Black 01 Broken Wall Atomic Health",
            ],
        )
        self.connect(hallway, control_room, self.blue_key)

        control_room_top = self.region(
            "Control Room Top",
            ["Unlock Cell Blocks"],
        )
        # Can jump on a pigcop to get up
        self.connect(
            control_room,
            control_room_top,
            self.red_key | r.jetpack(50) | (r.difficulty("medium") & r.can_jump),
        )

        control_room_ledges = self.region(
            "Control Room Top Ledges",
            [
                "Control Room Left Alcove",
                "Control Room Secret Pipebombs",
                "Control Room Right Alcove",
                "Control Room Secret Atomic Health",
                "Control Room Chaingun",
            ],
        )
        self.connect(control_room_top, control_room_ledges, r.jump)
        self.connect(control_room_top, control_vent, r.jump)

        courtyard = self.region("Courtyard")
        self.add_locations(["MP Courtyard Medkit", "Red Key Card"], courtyard)
        self.connect(control_room, courtyard, self.yellow_key)

        courtyard_ledge = self.region(
            "Courtyard Ledge",
            [
                "Courtyard Tunnel",
                "Courtyard Tunnel Atomic Health 1",
                "Courtyard Tunnel Atomic Health 2",
                "Courtyard Tunnel Atomic Health 3",
                "Courtyard Pipebombs",
            ],
        )
        self.connect(courtyard, courtyard_ledge, r.jump)

        courtyard_canyon = self.region(
            "Courtyard Canyon",
            [
                "Breakable Canyon Wall",
                "Breakable Canyon Wall Steroids",
            ],
        )
        self.connect(courtyard, courtyard_canyon, r.jump & r.explosives)
        # Technically this also gives us access to one of the cell blocks without the unlock event, but I don't see a
        # Way that transition is possible without already having access to cell blocks otherwise right now

        cell_blocks = self.region(
            "Cell Blocks",
            [
                "MP Cell Block 02 Jetpack",
                "Cell BLock 01 RPG",
                "MP Cell Block 01 Broken Wall Holo Duke",
            ],
        )
        self.connect(control_room, cell_blocks, self.event("Unlock Cell Blocks"))

        dock = self.region("Submarine Dock")
        self.add_locations(["Submarine Gate Scuba Gear"], cell_blocks)
        # Can shoot pipebombs to get to dock area, no explosive unlocks necessary!
        self.connect(cell_blocks, dock, r.true)
        # Can just walk in from the sub area
        self.connect(dock, courtyard, r.true)
        # Don't think this does anything yet, but better mark it down if we ever find an early sub clip or something
        self.connect(courtyard, control_room, self.yellow_key)

        dock_secret = self.region(
            "Submarine Dock Door Secret",
            [
                "Submarine Gate Hidden Alcove",
                "Submarine Gate Hidden Night Vision Goggles",
            ],
        )
        self.connect(dock, dock_secret, r.jump)

        submarine = self.region(
            "Submarine",
            [
                "Underwater Pipebombs",
                "Submarine Engine Room",
                "Submarine Engine Room Medkit",
                "Exit",
            ],
        )
        self.connect(dock, submarine, r.can_dive)
        return ret
