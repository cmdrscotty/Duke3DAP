from BaseClasses import Region

from ..base_classes import D3DLevel


class E2L2(D3DLevel):
    name = "Incubator"
    levelnum = 1
    volumenum = 1
    keys = ["Yellow"]
    location_defs = [
        {"name": "MP Underwater Jetpack", "id": 34, "type": "sprite", "density": 5},
        {"name": "Overgrown Passage Jetpack", "id": 67, "type": "sprite"},
        {"name": "Wall Panel Freezethrower", "id": 69, "type": "sprite"},
        {"name": "Underwater Devastator", "id": 82, "type": "sprite"},
        {"name": "Drone Alcove Atomic Health", "id": 99, "type": "sprite"},
        {"name": "Hidden Screen Room Armor", "id": 103, "type": "sprite"},
        {
            "name": "MP Control Room Freezethrower",
            "id": 130,
            "type": "sprite",
            "density": 5,
        },
        {"name": "EDF Logo Medkit", "id": 132, "type": "sprite"},
        {"name": "Pool Steroids", "id": 133, "type": "sprite"},
        {"name": "Pool Medkit", "id": 134, "type": "sprite"},
        {"name": "Hidden Screen Room Pipebombs", "id": 171, "type": "sprite"},
        {"name": "Armory RPG", "id": 179, "type": "sprite"},
        {"name": "Pipebombs behind Turret", "id": 225, "type": "sprite"},
        {
            "name": "Beta Scuba Gear",
            "id": 264,
            "type": "sprite",
        },  # Unused beta room of the map
        {"name": "Force Field Control Atomic Health 1", "id": 266, "type": "sprite"},
        {"name": "Force Field Control Atomic Health 2", "id": 267, "type": "sprite"},
        {"name": "Force Field Control Chaingun", "id": 268, "type": "sprite"},
        {
            "name": "Beta Medkit",
            "id": 285,
            "type": "sprite",
        },  # Unused beta room of the map
        {
            "name": "Beta Steroids",
            "id": 325,
            "type": "sprite",
        },  # Unused beta room of the map
        {"name": "Armory Tripmine 1", "id": 390, "type": "sprite"},
        {"name": "Armory Tripmine 2", "id": 391, "type": "sprite"},
        {"name": "Armory Tripmine 3", "id": 392, "type": "sprite"},
        {"name": "Wall Panel Holo Duke", "id": 410, "type": "sprite"},
        {"name": "Cupboard Night Vision Goggles", "id": 432, "type": "sprite"},
        {"name": "Yellow Key Card", "id": 524, "type": "sprite"},
        {"name": "Start Shotgun", "id": 525, "type": "sprite"},
        {"name": "Control Room Pipebombs", "id": 549, "type": "sprite"},
        {"name": "Overgrown Passage Shrinker", "id": 579, "type": "sprite"},
        {"name": "Secret EDF Logo", "id": 142, "type": "sector"},
        {"name": "Secret Force Field Control Wall", "id": 153, "type": "sector"},
        {"name": "Secret Hidden Screen Room 1", "id": 155, "type": "sector"},
        {"name": "Secret Hidden Screen Room 2", "id": 156, "type": "sector"},
        {"name": "Secret Wall Panel", "id": 248, "type": "sector"},
        {"name": "Exit", "id": 0, "type": "exit"},
    ]
    events = ["Lower Walls"]
    must_dive = True

    def main_region(self) -> Region:
        r = self.rules
        ret = self.region(
            self.name,
            [
                "Start Shotgun",
                "Hidden Screen Room Pipebombs",
                "EDF Logo Medkit",  # Can just grab this through the wall!
                "Armory Tripmine 1",
                "Armory Tripmine 2",
                "Armory Tripmine 3",
                "Secret Wall Panel",
                "Wall Panel Freezethrower",
                "Wall Panel Holo Duke",
                "Force Field Control Atomic Health 1",
                "Force Field Control Atomic Health 2",
                "Force Field Control Chaingun",
                "Secret Force Field Control Wall",
                "Armory RPG",
                "Yellow Key Card",
            ],
        )

        hidden_screen_room = self.region(
            "Hidden Screen Room",
            [
                "Secret Hidden Screen Room 1",
                "Secret Hidden Screen Room 2",
                "Hidden Screen Room Armor",
            ],
        )
        # Able to clip up the corner with mouse movement and diagonal strafing
        self.connect(
            ret,
            hidden_screen_room,
            r.jump | (r.difficulty("hard") & r.can_sprint) | r.difficulty("extreme"),
        )

        early_ledges = self.region(
            "Wall Compartments",
            [
                "Drone Alcove Atomic Health",
                "Cupboard Night Vision Goggles",
                "Secret EDF Logo",
            ],
        )
        self.connect(ret, early_ledges, r.jump)

        # Can clip up to the exit switch fairly easily
        waterfall = self.region(
            "Waterfall",
            ["Pool Medkit", "Pool Steroids", "Exit", "Pipebombs behind Turret"],
        )
        self.connect(
            ret,
            waterfall,
            self.event("Lower Walls")
            | (
                # TODO: find a way to somewhat reliably clip with jetpack and no sprint
                # without sprint the clip is very inconsistent
                # & ((r.difficulty("medium") & r.jetpack(100)) | r.jetpack(200))
                # current strats are: corner-crouch and jump-clip through the door
                r.glitched
                & (
                    (r.difficulty("hard") & (r.can_sprint | r.steroids))
                    | (r.difficulty("extreme") & r.can_jump)
                )
            ),
        )
        # Cursed cumulative jetpack logic
        self.restrict(
            "Pipebombs behind Turret",
            self.event("Lower Walls") & r.jetpack(50)
            | (
                r.glitched
                & ((r.difficulty("medium") & r.jetpack(150)) | r.jetpack(250))
            ),
        )

        control_room = self.region(
            "Control Room",
            ["Control Room Pipebombs", "MP Control Room Freezethrower", "Lower Walls"],
        )
        # Only a few tripclip resistant doors left
        self.connect(
            ret,
            control_room,
            self.yellow_key
            | (
                r.difficulty("extreme")
                & r.glitched
                & r.can_jump
                & r.can_sprint
                & r.steroids
                & r.tripmine
            ),
        )

        back_cave = self.region(
            "Overgrown Passage",
            ["Overgrown Passage Shrinker", "Overgrown Passage Jetpack"],
        )
        # Can probably clip walk up the right wall, but I can't find the setup
        # Very cursed jetpack calcs
        self.connect(
            waterfall,
            back_cave,
            r.can_jump
            | self.event("Lower Walls") & r.jetpack(50)
            | (
                r.glitched
                & ((r.difficulty("medium") & r.jetpack(150)) | r.jetpack(250))
            ),
        )

        incubator_pool = self.region(
            "Incubator Pool", ["MP Underwater Jetpack", "Underwater Devastator"]
        )
        self.connect(waterfall, incubator_pool, r.can_dive)
        return ret
