from BaseClasses import Region

from ..base_classes import D3DLevel


class E4L7(D3DLevel):
    name = "XXX-Stacy"
    levelnum = 6
    volumenum = 3
    keys = ["Red", "Blue"]
    location_defs = [
        {"id": 8, "name": "Crusher Scuba Gear", "type": "sprite"},
        {"id": 29, "name": "Blue Holo Duke", "type": "sprite"},
        {"id": 34, "name": "Front Upper Freezethrower", "type": "sprite"},
        {"id": 35, "mp": True, "name": "MP Blue Apt. Jetpack", "type": "sprite"},
        {"id": 37, "name": "37 Pipebombs", "type": "sprite"},
        {"id": 83, "name": "Front Upper Armor", "type": "sprite"},
        {"id": 84, "name": "Front Upper Atomic Health", "type": "sprite"},
        {"id": 110, "name": "Crusher RPG", "type": "sprite"},
        {"id": 112, "name": "Crusher Medkit", "type": "sprite"},
        {"id": 165, "name": "Front Upper Blue Key Card", "type": "sprite"},
        {"id": 166, "name": "Cola Tripbomb 1", "type": "sprite"},
        {"id": 167, "name": "Cola Tripbomb 2", "type": "sprite"},
        {"id": 170, "name": "Blue Devastator", "type": "sprite"},
        {"id": 176, "name": "Outside Pipebombs", "type": "sprite"},
        {"id": 177, "name": "Front Chaingun", "type": "sprite"},
        {"id": 186, "name": "Front Protective Boots", "type": "sprite"},
        {"id": 195, "name": "Blue Secret Shrinker", "type": "sprite"},
        {"id": 207, "mp": True, "name": "MP Outside Shotgun", "type": "sprite"},
        {"id": 216, "name": "Blue Atomic Health", "type": "sprite"},
        {"id": 245, "name": "Blue Secret Night Vision Goggles", "type": "sprite"},
        {"id": 322, "name": "Blue Medkit", "type": "sprite"},
        {"id": 331, "name": "Front Steroids", "type": "sprite"},
        {"id": 365, "mp": True, "name": "MP Blue Jetpack", "type": "sprite"},
        {"id": 372, "name": "Blue Area Red Key Card", "type": "sprite"},
        {"id": 420, "name": "Blue Shotgun", "type": "sprite"},
        {"id": 591, "name": "Blue Apt. RPG", "type": "sprite"},
        {"id": 65, "name": "Blue Secret", "type": "sector"},
        {"id": 232, "name": "Crate Secret", "type": "sector"},
        {"id": 265, "name": "Blue Apt. Secret", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
    def main_region(self) -> Region:
        r = self.rules
        ret = self.region(
            self.name,
            [
                "MP Outside Shotgun",
                "Outside Pipebombs",
                "Front Protective Boots",
                "Front Chaingun",
                "Front Steroids",
                "MP Front Jetpack",
            ],
        )

        front_upper = self.region(
            "Front Upper",
            [
                "Front Upper Armor",
                "Front Upper Atomic Health",
                "Front Upper Freezethrower",
                "Front Upper Blue Key Card",
                "Crate Secret",
            ],
        )
        self.connect(ret, front_upper, r.jump)

        blue_key_area = self.region(
            "Blue Key Area",
            [
                "Blue Medkit",
                "Blue Shotgun",
                "MP Blue Jetpack",
                "Blue Area Red Key Card",
                "Blue Holo Duke",
                "Blue Devastator",
                "Blue Atomic Health",
                "Blue Apt. Secret",
                "Blue Apt. RPG",
                "MP Blue Apt. Jetpack",
            ],
        )
        # One way, cant go back without crouching
        self.connect(ret, blue_key_area, (self.blue_key & r.jump) |
                     (r.crouch_jump & r.steroids))
        
        blue_dive = self.region(
            "Blue Dive Area",
            [
                "Blue Secret Shrinker",
                "Blue Secret",
                "Blue Secret Night Vision Goggles",
                "Cola Tripbomb 1",
                "Cola Tripbomb 2",
            ],
        )
        # Crouchjump through window skips dive and jetpack requirement
        self.connect(blue_key_area, blue_dive, (r.can_dive & r.jetpack(50)) |
                     r.crouch_jump)
        
        dive_crusher = self.region(
            "Dive Crusher",
            [
                "Crusher Scuba Gear",
                "Crusher RPG",
                "Crusher Medkit",
            ],
        )
        self.connect(blue_dive, dive_crusher, r.can_dive)

        red_key_area = self.region(
            "Red Key Area",
            [
                "Exit",
            ],
        )
        self.connect(blue_dive, red_key_area, self.red_key)