from BaseClasses import Region

from ..base_classes import D3DLevel


class E3L3(D3DLevel):
    name = "Flood Zone"
    levelnum = 2
    volumenum = 2
    keys = ["Blue", "Red", "Yellow"]
    location_defs = [
        {"id": 1, "mp": True, "name": "MP Exit Jetpack", "type": "sprite"},
        {"id": 23, "name": "Water Surface Night Vision Goggles", "type": "sprite"},
        {"id": 24, "name": "Canyon Night Vision Goggles", "type": "sprite"},
        {"id": 42, "mp": True, "name": "MP Canyon Pillars Jetpack", "type": "sprite"},
        {"id": 50, "name": "Canyon Wall Jetpack", "type": "sprite"},
        {"id": 63, "mp": True, "name": "MP Hidden Cave Jetpack", "type": "sprite"},
        {"id": 70, "name": "Sunken Building Freezethrower", "type": "sprite"},
        {"id": 71, "name": "Inside Building Tripmine 1", "type": "sprite"},
        {"id": 72, "name": "Inside Building Tripmine 2", "type": "sprite"},
        {"id": 73, "name": "Building Ledge Shrinker", "type": "sprite"},
        {"id": 95, "name": "Inside Building Holo Duke", "type": "sprite"},
        {"id": 96, "mp": True, "name": "MP Chaingun near Red Door", "type": "sprite"},
        {
            "id": 97,
            "mp": True,
            "name": "MP Building Ledge Devastator",
            "type": "sprite",
        },
        {"id": 98, "mp": True, "name": "MP Inside Building Shotgun", "type": "sprite"},
        {"id": 114, "name": "Exit Atomic Health", "type": "sprite"},
        {"id": 168, "name": "Sunken Building Chaingun", "type": "sprite"},
        {"id": 171, "name": "Blue Key Card", "type": "sprite"},
        {"id": 172, "name": "Underwater Atomic Health", "type": "sprite"},
        {"id": 174, "name": "Underwater Armor", "type": "sprite"},
        {"id": 175, "name": "Hidden Cave Scuba Gear", "type": "sprite"},
        {"id": 178, "name": "Start Scuba Gear", "type": "sprite"},
        {"id": 190, "name": "Canyon Atomic Health", "type": "sprite"},
        {"id": 193, "name": "Hidden Cave Devastator", "type": "sprite"},
        {"id": 200, "name": "Inside Building Medkit", "type": "sprite"},
        {"id": 204, "name": "Start RPG", "type": "sprite"},
        {"id": 223, "name": "Sign Top Atomic Health", "type": "sprite"},
        {"id": 234, "name": "Inside Building Pipebombs", "type": "sprite"},
        {"id": 254, "name": "Underwater Shotgun", "type": "sprite"},
        {"id": 256, "name": "Top of Building Pipebombs", "type": "sprite"},
        {"id": 313, "name": "Inside Building Steroids", "type": "sprite"},
        {"id": 372, "name": "Building Ledge Atomic Health", "type": "sprite"},
        {"id": 387, "name": "Sunken Building Medkit", "type": "sprite"},
        {"id": 392, "name": "Yellow Key Card", "type": "sprite"},
        {"id": 407, "name": "Red Key Card", "type": "sprite"},
        {
            "id": 448,
            "mp": True,
            "name": "MP Canyon Pillars Scuba Gear",
            "type": "sprite",
        },
        {"id": 449, "mp": True, "name": "MP Sunken Building Armor", "type": "sprite"},
        {"id": 450, "mp": True, "name": "MP Underwater RPG", "type": "sprite"},
        {"id": 465, "name": "Canyon Alcove Chaingun", "type": "sprite"},
        {"id": 178, "name": "Secret Hidden Cave", "type": "sector"},
        {"id": 221, "name": "Secret Building Canyon Wall", "type": "sector"},
        {"id": 222, "name": "Secret Empty Ledge", "type": "sector"},
        {"id": 232, "name": "Secret Canyon Alcove Window", "type": "sector"},
        {"id": 259, "name": "Secret Hard Hat Area", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
    must_dive = True

    def main_region(self) -> Region:
        r = self.rules
        ret = self.region(
            self.name,
            ["Start Scuba Gear", "Start RPG", "Water Surface Night Vision Goggles"],
        )

        building_ledge = self.region(
            "Building Ledge",
            ["Building Ledge Atomic Health", "Building Ledge Shrinker"],
        )
        self.connect(ret, building_ledge, r.can_sprint & r.steroids)

        top_of_building = self.region("Top of Building", ["Top of Building Pipebombs"])
        self.connect(
            ret,
            building_ledge,
            (
                (r.can_sprint | r.steroids & r.can_jump)
                | r.jetpack(50)
                # precise but no SR50 required
                | (r.difficulty("medium") & r.can_sprint & r.steroids)
            ),
        )
        self.connect(top_of_building, building_ledge, r.true)

        building_jumps = self.region(
            "Top of Building Ledges",
            [
                "Secret Building Canyon Wall",
                "Canyon Wall Jetpack",
                "Canyon Atomic Health",
                "Canyon Night Vision Goggles",
                "MP Building Ledge Devastator",
            ],
        )
        self.connect(top_of_building, building_jumps, r.jump)

        sunken_building_top = self.region(
            "Top of Sunken Building",
            ["Sunken Building Chaingun", "MP Sunken Building Armor"],
        )
        self.connect(top_of_building, sunken_building_top, r.jump)

        underwater = self.region(
            "Underwater",
            [
                "Underwater Atomic Health",
                "Underwater Armor",
                "MP Underwater RPG",
                "Underwater Shotgun",
                "Inside Building Medkit",
            ],
        )
        self.connect(ret, underwater, r.can_dive)
        self.connect(
            underwater, sunken_building_top, r.jump
        )  # I'm sure there's a step up here somewhere

        red_door = self.region(
            "Red Door Building Top",
            [
                "Sign Top Atomic Health",
                "MP Chaingun near Red Door",
                "Blue Key Card",
                "MP Canyon Pillars Scuba Gear",
                "MP Canyon Pillars Jetpack",
                "Canyon Alcove Chaingun",
                "Secret Canyon Alcove Window",
                "Secret Empty Ledge",
            ],
        )
        self.connect(
            sunken_building_top, red_door, r.jump
        )  # 50 jetpack fuel is just enough to make it from the start

        exit_area = self.region(
            "Beyond Red Door",
            ["Secret Hard Hat Area", "Exit Atomic Health", "Exit", "MP Exit Jetpack"],
        )
        self.connect(red_door, exit_area, self.red_key)
        self.restrict(
            "Exit Atomic Health", r.jump
        )  # even no run jetpack only has enough to cross the gap on 50
        self.restrict(
            "MP Exit Jetpack", r.dive(50)
        )  # Tight, but can do the jump and dive route in 49!

        blue_door_area = self.region(
            "Beyond Blue Door",
            [
                "Sunken Building Medkit",
                "Sunken Building Freezethrower",
                "Yellow Key Card",
            ],
        )
        self.connect(underwater, blue_door_area, self.blue_key)

        hidden_water_cave = self.region(
            "Hidden Water Cave",
            [
                "Hidden Cave Scuba Gear",
                "MP Hidden Cave Jetpack",
                "Hidden Cave Devastator",
                "Secret Hidden Cave",
            ],
        )
        self.connect(underwater, hidden_water_cave, r.explosives)

        inside_building = self.region(
            "Inside the Building",
            [
                "Red Key Card",
                "Inside Building Pipebombs",
                "Inside Building Tripmine 1",
                "Inside Building Tripmine 2",
                "Inside Building Holo Duke",
                "MP Inside Building Shotgun",
                "Inside Building Steroids",
            ],
        )
        self.connect(top_of_building, inside_building, self.yellow_key)
        # There might be a super precise tripmine or steroids + devastator clip, possibly?
        self.connect(
            underwater,
            inside_building,
            self.yellow_key | r.glitched & (r.rpg | r.pipebomb),
        )
        # Can walk up, useful if has dive and yellow key but no other movement
        # This is not unrestricted because the door is still locked if we explosives clip inside!
        self.connect(inside_building, top_of_building, self.yellow_key)

        return ret
