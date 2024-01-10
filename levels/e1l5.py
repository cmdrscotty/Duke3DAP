from BaseClasses import Region

from ..base_classes import D3DLevel


class E1L5(D3DLevel):
    name = "The Abyss"
    levelnum = 4
    volumenum = 0
    keys = ["Blue"]
    location_defs = [
        {"name": "Battlelord Medkit", "id": 4, "type": "sprite"},
        {"name": "Battlelord Atomic Health 1", "id": 11, "type": "sprite"},
        {"name": "Battlelord Atomic Health 2", "id": 12, "type": "sprite"},
        {"name": "Waterfall Chaingun", "id": 24, "type": "sprite"},
        {"name": "MP Start Chaingun", "id": 78, "type": "sprite", "density": 5},
        {"name": "Battlelord Jetpack", "id": 79, "type": "sprite"},
        {"name": "Battlelord Armor", "id": 80, "type": "sprite"},
        {"name": "Cracked Wall End Atomic Health", "id": 112, "type": "sprite"},
        {"name": "Fire Pit Pipe Bombs", "id": 131, "type": "sprite"},
        {"name": "Top of Spaceship Atomic Health", "id": 216, "type": "sprite"},
        {"name": "Spaceship Shaft RPG", "id": 221, "type": "sprite"},
        {"name": "Spaceship Shaft Chaingun", "id": 222, "type": "sprite"},
        {"name": "Fire Pit Night Vision Goggles", "id": 262, "type": "sprite"},
        {"name": "Canyon Chaingun", "id": 291, "type": "sprite"},
        {"name": "MP Secret Fire Pit Armor", "id": 294, "type": "sprite", "density": 5},
        {"name": "Pipebombs near Blue Gate", "id": 311, "type": "sprite"},
        {"name": "Start Shotgun", "id": 316, "type": "sprite"},
        {"name": "Earthquake Atomic Health 1", "id": 373, "type": "sprite"},
        {"name": "Earthquake Atomic Health 2", "id": 374, "type": "sprite"},
        {"name": "Blue Key Card", "id": 375, "type": "sprite"},
        {"name": "Cracked Wall Middle Atomic Health", "id": 410, "type": "sprite"},
        {"name": "Fire Pit RPG", "id": 439, "type": "sprite"},
        {"name": "Dancing Shaman Atomic Health 1", "id": 466, "type": "sprite"},
        {"name": "Dancing Shaman Atomic Health 2", "id": 472, "type": "sprite"},
        {"name": "Dancing Shaman Atomic Health 3", "id": 473, "type": "sprite"},
        {"name": "Red Waterfall Pipe Bombs", "id": 524, "type": "sprite"},
        {"name": "Start Protective Boots", "id": 604, "type": "sprite"},
        {"name": "Bottom of Ruins Protective Boots", "id": 682, "type": "sprite"},
        {"name": "Fire Place Medkit", "id": 689, "type": "sprite"},
        {"name": "Toxic River Protective Boots", "id": 698, "type": "sprite"},
        {"name": "Start RPG", "id": 718, "type": "sprite"},
        {"name": "Secret Fire Pit Night Vision Goggles", "id": 726, "type": "sprite"},
        {"name": "Secret Fire Pit Medkit", "id": 727, "type": "sprite"},
        {"name": "Toxic River Holo Duke", "id": 733, "type": "sprite"},
        {"name": "Toxic River Medkit", "id": 734, "type": "sprite"},
        {"name": "Ruins Staircase Shotgun", "id": 737, "type": "sprite"},
        {"name": "Fire Pit Steroids", "id": 738, "type": "sprite"},
        {"name": "Cracked Wall Bottom Atomic Health", "id": 740, "type": "sprite"},
        {"name": "Cracked Wall Protective Boots", "id": 741, "type": "sprite"},
        {"name": "Cracked Wall Medkit", "id": 742, "type": "sprite"},
        {"name": "Spaceship Entrance Armor", "id": 744, "type": "sprite"},
        {"name": "Earthquake Night Vision Goggles", "id": 817, "type": "sprite"},
        {"name": "Red Waterfall Cave Protective Boots", "id": 868, "type": "sprite"},
        {
            "name": "MP Shrinker Room Steroids",
            "id": 876,
            "type": "sprite",
            "density": 5,
        },
        {
            "name": "MP Cracked Wall Bottom Pipebombs",
            "id": 879,
            "type": "sprite",
            "density": 5,
        },
        {"name": "Canyon Pillars RPG", "id": 884, "type": "sprite"},
        {"name": "MP Fire Pit Jetpack", "id": 1032, "type": "sprite", "density": 5},
        {"name": "MP Fire Place RPG", "id": 1039, "type": "sprite", "density": 5},
        {
            "name": "MP Ruins Staircase Atomic Health",
            "id": 1041,
            "type": "sprite",
            "density": 5,
        },
        {
            "name": "MP Ruins Staircase Armor",
            "id": 1042,
            "type": "sprite",
            "density": 5,
        },
        {
            "name": "MP Bottom of Ruins Shotgun",
            "id": 1044,
            "type": "sprite",
            "density": 5,
        },
        {"name": "Fire Pit Atomic Health", "id": 1046, "type": "sprite"},
        {"name": "Secret Fire Pit Atomic Health 1", "id": 1047, "type": "sprite"},
        {"name": "Secret Fire Pit Atomic Health 2", "id": 1048, "type": "sprite"},
        {"name": "Secret Red Waterfall Passage", "id": 7, "type": "sector"},
        {"name": "Secret Dancing Shaman", "id": 21, "type": "sector"},
        {"name": "Secret Top of Spaceship", "id": 257, "type": "sector"},
        {"name": "Secret Fire Pit Hidden Wall", "id": 354, "type": "sector"},
        {"name": "Secret Fire Pit Teleporter", "id": 440, "type": "sector"},
        {"name": "Secret Fire Pit Ledge", "id": 441, "type": "sector"},
        {"name": "Exit", "id": 0, "type": "exit"},
    ]
    events = ["Earthquake", "Canyon Explosion"]
    has_boss = True

    def main_region(self) -> Region:
        r = self.rules
        ret = self.region(
            self.name,
            [
                "Start RPG",
                "Start Shotgun",
                "Start Protective Boots",
                "MP Start Chaingun",
                "Blue Key Card",
                "Canyon Chaingun",
                "Toxic River Medkit",
                "Toxic River Holo Duke",
                "Toxic River Protective Boots",
                "Earthquake Night Vision Goggles",
            ],
        )
        self.restrict("Blue Key Card", r.jump)  # It's juust out of reach
        self.restrict("Earthquake Night Vision Goggles", r.jump)

        blue_gate = self.region("Beyond Blue Key Gate", ["Pipebombs near Blue Gate"])
        self.connect(
            ret,
            blue_gate,
            self.blue_key | (r.difficulty("hard") & r.crouch_jump) | r.jetpack(50),
        )

        fault_trigger = self.region(
            "Earthquake Trigger",
            [
                "Earthquake",
                "Secret Fire Pit Night Vision Goggles",
                "Secret Fire Pit Medkit",
            ],
        )
        self.connect(
            blue_gate, fault_trigger, r.jump
        )  # jetpack also gets here without blue key by above logic

        beyond_fault = self.region(
            "After Earthquake",
            [
                "Earthquake Atomic Health 1",
                "Earthquake Atomic Health 2",
                "Ruins Staircase Shotgun",
                "MP Fire Place RPG",
                "Fire Place Medkit",
                "MP Ruins Staircase Atomic Health",
                "MP Ruins Staircase Armor",
                "Fire Pit Steroids",
                "Secret Fire Pit Hidden Wall",
                "Fire Pit Pipe Bombs",
                "Fire Pit Atomic Health",
                "Secret Fire Pit Teleporter",
                "MP Shrinker Room Steroids",
                "Bottom of Ruins Protective Boots",
                "MP Bottom of Ruins Shotgun",
            ],
        )
        self.connect(fault_trigger, beyond_fault, self.event("Earthquake"))

        small_ledges = self.region(
            "Ledges after Earthquake",
            [
                "MP Ruins Staircase Atomic Health",
                "MP Ruins Staircase Armor",
                "Secret Fire Pit Atomic Health 1",
                "Secret Fire Pit Atomic Health 2",
                "MP Secret Fire Pit Armor",
                "Secret Fire Pit Ledge",
                "Fire Pit RPG",
                "Waterfall Chaingun",
                "Canyon Explosion",
                "Fire Pit Night Vision Goggles",
                "MP Fire Pit Jetpack",
            ],
        )
        # always have like 20 jetpack left from earthquake at this point, should all be fine
        self.connect(beyond_fault, small_ledges, r.jump)
        # Would get stuck in the room afterward otherwise
        self.restrict("Canyon Explosion", r.can_shrink | r.crouch_jump)

        # anything beyond here on pure jetpack uses 50 fuel to get to the red canyon area and make progress
        # it might be possible in just 50 to get here, but that seems a harsh requirement
        red_waterfall = self.region(
            "Red Waterfall",
            [
                "Red Waterfall Cave Protective Boots",
                "Red Waterfall Pipe Bombs",
                "Dancing Shaman Atomic Health 1",
                "Dancing Shaman Atomic Health 2",
                "Dancing Shaman Atomic Health 3",
                "Secret Dancing Shaman",
                "Secret Red Waterfall Passage",
            ],
        )
        self.connect(beyond_fault, red_waterfall, r.can_jump | r.jetpack(100))
        self.restrict("Secret Red Waterfall Passage", r.explosives)

        ship_entrance = self.region(
            "Ship Entrance",
            [
                "MP Cracked Wall Bottom Pipebombs",
                "Cracked Wall Bottom Atomic Health",
                "Cracked Wall Middle Atomic Health",
                "Cracked Wall Protective Boots",
                "Cracked Wall Medkit",
                "Cracked Wall End Atomic Health",
                "Canyon Pillars RPG",
                "Spaceship Entrance Armor",
                "Secret Top of Spaceship",
                "Top of Spaceship Atomic Health",
            ],
        )
        self.connect(
            beyond_fault,
            ship_entrance,
            self.event("Canyon Explosion") & (r.can_jump | r.jetpack(100)),
        )

        spaceship = self.region(
            "Spaceship",
            [
                "Spaceship Shaft RPG",
                "Spaceship Shaft Chaingun",
                "Battlelord Medkit",
                "Battlelord Atomic Health 1",
                "Battlelord Atomic Health 2",
                "Battlelord Jetpack",
                "Battlelord Armor",
                "Exit",
            ],
        )
        # Big drop, can't get back
        self.connect(ship_entrance, spaceship, r.true)
        # Clip to DM exit near boss drop
        self.restrict(
            "Exit",
            r.can_kill_boss_1
            | (r.glitched & r.difficulty("hard") & r.steroids & r.can_jump),
        )

        return ret
