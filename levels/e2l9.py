from BaseClasses import Region

from ..base_classes import D3DLevel


class E2L9(D3DLevel):
    name = "Overlord"
    levelnum = 8
    volumenum = 1
    keys = []
    location_defs = [
        {"id": 7, "name": "Timed Wall RPG", "type": "sprite"},
        {"id": 8, "name": "Control Room Armor", "type": "sprite"},
        {"id": 9, "name": "Waterfall Armor", "type": "sprite"},
        {"id": 10, "name": "Vents Pipebombs 1", "type": "sprite"},
        {"id": 12, "name": "Overlord Tunnel Medkit", "type": "sprite"},
        {"id": 13, "name": "Broken Wall Medkit", "type": "sprite"},
        {"id": 14, "name": "Waterfall Night Vision Goggles", "type": "sprite"},
        {"id": 15, "name": "Waterfall Scuba Gear", "type": "sprite"},
        {"id": 16, "name": "Hidden Wall Atomic Health", "type": "sprite"},
        {"id": 39, "name": "Hidden Wall Armor", "type": "sprite"},
        {"id": 69, "name": "Waterfall Tripmine", "type": "sprite"},
        {"id": 70, "name": "Overlord Tripmine 1", "type": "sprite"},
        {"id": 71, "name": "Overlord Tripmine 2", "type": "sprite"},
        {"id": 73, "name": "Overlord Atomic Health", "type": "sprite"},
        {"id": 78, "name": "Combination Lock Scuba Gear", "type": "sprite"},
        {"id": 81, "name": "Control Room Night Vision Goggles", "type": "sprite"},
        {"id": 83, "name": "Control Room Chaingun", "type": "sprite"},
        {"id": 84, "name": "Vents Center Atomic Health", "type": "sprite"},
        {"id": 86, "name": "Waterfall Atomic Health", "type": "sprite"},
        {"id": 93, "name": "Waterfall Shrinker", "type": "sprite"},
        {"id": 94, "name": "Overlord Tunnel Devastator", "type": "sprite"},
        {"id": 96, "name": "Waterfall RPG", "type": "sprite"},
        {"id": 100, "name": "Reactor Freezethrower", "type": "sprite"},
        {"id": 102, "name": "Start Underwater Shotgun", "type": "sprite"},
        {"id": 104, "name": "Start Underwater Atomic Health", "type": "sprite"},
        {"id": 159, "name": "Vents Pipebombs 2", "type": "sprite"},
        {"id": 395, "name": "Waterfall Holo Duke", "type": "sprite"},
        {"id": 396, "name": "Overlord Tunnel Jetpack", "type": "sprite"},
        {"id": 413, "name": "Timed Wall Medkit", "type": "sprite"},
        {"id": 415, "name": "Timed Wall Atomic Health", "type": "sprite"},
        {"id": 424, "name": "Waterfall Wall Pipebombs 1", "type": "sprite"},
        {"id": 425, "name": "Waterfall Wall Pipebombs 2", "type": "sprite"},
        {"id": 203, "name": "Secret Hidden Reactor Wall", "type": "sector"},
        {"id": 219, "name": "Secret Timed Overlord Wall", "type": "sector"},
        {"id": 225, "name": "Secret Waterfall Wall", "type": "sector"},
        {"id": 246, "name": "Secret Timed Reactor Wall", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
    must_dive = True

    def main_region(self) -> Region:
        r = self.rules
        # lucky us, we start underwater so we can swim without dive until we surface!
        ret = self.region(
            self.name,
            [
                "Start Underwater Shotgun",
                "Start Underwater Atomic Health",
                "Combination Lock Scuba Gear",
                "Secret Hidden Reactor Wall",
                "Hidden Wall Atomic Health",
                "Hidden Wall Armor",
                "Broken Wall Medkit",
                "Waterfall Tripmine",
                "Waterfall Armor",
                "Waterfall Shrinker",
                "Waterfall Scuba Gear",
                "Waterfall Night Vision Goggles",
                "Waterfall RPG",
                "Waterfall Holo Duke",
                "Waterfall Atomic Health",
            ],
        )
        self.restrict("Waterfall Holo Duke", r.dive(100))

        reactor = self.region(
            "Reactor",
            ["Reactor Freezethrower", "Secret Timed Reactor Wall", "Timed Wall RPG"],
        )
        self.connect(ret, reactor, r.jump)

        waterfall_wall = self.region(
            "Waterfall Wall",
            [
                "Secret Waterfall Wall",
                "Waterfall Wall Pipebombs 1",
                "Waterfall Wall Pipebombs 2",
            ],
        )
        self.connect(ret, waterfall_wall, r.explosives)

        vents = self.region(
            "Ventilation Shafts",
            [
                "Vents Center Atomic Health",
                "Vents Pipebombs 1",
                "Vents Pipebombs 2",
                "Control Room Night Vision Goggles",
                "Control Room Chaingun",
                "Control Room Armor",
            ],
        )
        # It's slow, but going via waterfall room gets you in with no sprint requirements
        self.connect(ret, vents, r.jump)

        overlord_chamber = self.region(
            "Overlord Chamber",
            [
                "Overlord Tripmine 1",
                "Overlord Tripmine 2",
                "Overlord Atomic Health",
                "Secret Timed Overlord Wall",
                "Timed Wall Medkit",
                "Timed Wall Atomic Health",
                "Exit",
            ],
        )
        # Why fight when you can just press the exit button
        self.restrict("Exit", r.can_kill_boss_2 | r.glitched)
        self.connect(vents, overlord_chamber, r.true)

        overlord_tunnel = self.region(
            "Overlord Tunnel",
            [
                "Overlord Tunnel Devastator",
                "Overlord Tunnel Jetpack",
                "Overlord Tunnel Medkit",
            ],
        )
        self.connect(overlord_chamber, overlord_tunnel, r.jump & r.dive(100))
        return ret
