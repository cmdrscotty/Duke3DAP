from BaseClasses import Region

from ..base_classes import D3DLevel


class E2L6(D3DLevel):
    name = "Tiberius Station"
    levelnum = 5
    volumenum = 1
    keys = ["Blue", "Red"]
    location_defs = [
        {"id": 32, "name": "Timed Wall RPG", "type": "sprite"},
        {"id": 42, "name": "Toxic Room Protective Boots", "type": "sprite"},
        {"id": 43, "name": "Toxic Room Scuba Gear", "type": "sprite"},
        {"id": 45, "name": "Underwater Night Vision Goggles", "type": "sprite"},
        {"id": 46, "name": "Underwater Medkit", "type": "sprite"},
        {"id": 115, "name": "Toxic Room Wall Jetpack", "type": "sprite"},
        {"id": 181, "name": "Supplies Medkit", "type": "sprite"},
        {"id": 346, "name": "Supplies Armor 1", "type": "sprite"},
        {"id": 347, "name": "Supplies Armor 2", "type": "sprite"},
        {"id": 348, "name": "Blue Key Card", "type": "sprite"},
        {"id": 430, "name": "Water Fountain Pipebombs 1", "type": "sprite"},
        {"id": 431, "name": "Water Fountain Pipebombs 2", "type": "sprite"},
        {"id": 490, "name": "Armory Shrinker", "type": "sprite"},
        {"id": 507, "name": "Timed Devastator", "type": "sprite"},
        {"id": 508, "name": "Monitor Room Shotgun", "type": "sprite"},
        {"id": 509, "name": "Monitor Room Holo Duke", "type": "sprite"},
        {"id": 526, "name": "Corridor Wall Steroids", "type": "sprite"},
        {"id": 527, "name": "Timed Room Atomic Health", "type": "sprite"},
        {"id": 540, "name": "Toxic Alcove Atomic Health 1", "type": "sprite"},
        {"id": 541, "name": "Toxic Alcove Atomic Health 2", "type": "sprite"},
        {"id": 544, "name": "Corridor Wall Explosion RPG", "type": "sprite"},
        {"id": 545, "name": "Toxic Room Freezethrower", "type": "sprite"},
        {"id": 549, "name": "Exit Vent Medkit", "type": "sprite"},
        {"id": 551, "name": "Exit Room Chaingun", "type": "sprite"},
        {"id": 567, "name": "Bathroom Tripmine 1", "type": "sprite"},
        {"id": 568, "name": "Bathroom Tripmine 2", "type": "sprite"},
        {"id": 607, "name": "Armory Night Vision Goggles", "type": "sprite"},
        {"id": 608, "name": "Corridor Wall Night Vision Goggles", "type": "sprite"},
        {
            "id": 609,
            "density": 5,
            "name": "MP Toilet Night Vision Goggles",
            "type": "sprite",
        },
        {"id": 610, "name": "Red Key Card", "type": "sprite"},
        {"id": 67, "name": "Secret Toxic Alcove 1", "type": "sector"},
        {"id": 72, "name": "Secret Toxic Alcove 2", "type": "sector"},
        {"id": 136, "name": "Secret Corridor Wall", "type": "sector"},
        {"id": 145, "name": "Secret Toxic Room Wall", "type": "sector"},
        {"id": 166, "name": "Secret Water Fountain Wall", "type": "sector"},
        {"id": 258, "name": "Secret Supplies", "type": "sector"},
        {"id": 288, "name": "Secret Vent Wall Crack", "type": "sector"},
        {"id": 309, "name": "Secret Timed Wall", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
    events = ["Explode Wall"]
    must_dive = True

    def main_region(self) -> Region:
        r = self.rules
        ret = self.region(self.name, [])

        entry_room = self.region(
            "Entry Room",
            [
                "Supplies Armor 1",
                "Supplies Armor 2",
                "Secret Supplies",
                "Supplies Medkit",
                "Armory Shrinker",
                "Armory Night Vision Goggles",
                "Water Fountain Pipebombs 1",
                "Water Fountain Pipebombs 2",
                "Secret Water Fountain Wall",
                "Blue Key Card",
                "Monitor Room Shotgun",
                "Secret Vent Wall Crack",
                "Timed Devastator",
                "Secret Corridor Wall",
                "Corridor Wall Steroids",
                "Corridor Wall Night Vision Goggles",
                "Bathroom Tripmine 1",
                "Bathroom Tripmine 2",
                "MP Toilet Night Vision Goggles",
                "Corridor Wall Explosion RPG",
            ],
        )
        # sad, jetpack doesn't work
        self.connect(ret, entry_room, r.can_jump)
        self.restrict("Secret Vent Wall Crack", r.jump & r.explosives)

        early_ledges = self.region(
            "Early Ledges", ["Timed Room Atomic Health", "Monitor Room Holo Duke"]
        )
        self.connect(entry_room, early_ledges, r.jump)
        self.restrict("Monitor Room Holo Duke", r.can_crouch)

        toxic_room = self.region(
            "Toxic Room",
            [
                "Toxic Room Protective Boots",
                "Toxic Room Scuba Gear",
                "Toxic Room Freezethrower",
                "Toxic Alcove Atomic Health 1",
                "Toxic Alcove Atomic Health 2",
                "Secret Toxic Alcove 1",
                "Secret Toxic Alcove 2",
            ],
        )
        self.connect(entry_room, toxic_room, r.jump | self.blue_key)

        toxic_dive = self.region(
            "Toxic Dive",
            ["Underwater Night Vision Goggles", "Red Key Card", "Underwater Medkit"],
        )
        self.connect(toxic_room, toxic_dive, r.can_dive)

        toxic_room_wall = self.region(
            "Toxic Room Breakable Wall",
            ["Secret Toxic Room Wall", "Toxic Room Wall Jetpack", "Explode Wall"],
        )
        self.connect(toxic_room, toxic_room_wall, r.explosives)

        exit_vent = self.region("Exit Room Vent", ["Exit Vent Medkit"])
        self.connect(
            entry_room, exit_vent, r.jetpack(50) | (r.difficulty("medium") & r.can_jump)
        )

        timed_wall = self.region(
            "Timed Wall Secret", ["Secret Timed Wall", "Timed Wall RPG"]
        )
        self.connect(
            exit_vent,
            timed_wall,
            r.jetpack(50) | (r.can_jump & self.event("Explode Wall")),
        )

        exit_room = self.region("Exit Room", ["Exit", "Exit Room Chaingun"])
        self.connect(toxic_room, exit_room, self.red_key)
        self.connect(exit_vent, exit_room, r.true)
        self.restrict("Exit", r.jump)
        return ret
