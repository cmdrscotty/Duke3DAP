from BaseClasses import Region

from ..base_classes import D3DLevel


class E2L10(D3DLevel):
    name = "Spin Cycle"
    levelnum = 9
    volumenum = 1
    keys = []
    location_defs = [
        {"id": 36, "name": "Beta Shrinker", "type": "sprite"},
        {"id": 37, "name": "Gamma Freezethrower", "type": "sprite"},
        {"id": 38, "name": "Delta RPG", "type": "sprite"},
        {"id": 39, "name": "Alpha Chaingun", "type": "sprite"},
        {"id": 61, "name": "Gamma Medkit", "type": "sprite"},
        {"id": 141, "mp": True, "name": "MP Alpha Holo Duke", "type": "sprite"},
        {"id": 142, "mp": True, "name": "MP Beta Jetpack", "type": "sprite"},
        {
            "id": 143,
            "mp": True,
            "name": "MP Gamma Night Vision Goggles",
            "type": "sprite",
        },
        {"id": 144, "mp": True, "name": "MP Delta Jetpack", "type": "sprite"},
        {"id": 162, "name": "Beta Atomic Health", "type": "sprite"},
        {"id": 179, "name": "Alpha Medkit", "type": "sprite"},
        {"id": 199, "name": "Delta Atomic Health", "type": "sprite"},
        {"id": 206, "name": "Alpha Shotgun", "type": "sprite"},
        {"id": 207, "name": "Alpha Pipebombs", "type": "sprite"},
        {"id": 210, "name": "Delta Shotgun", "type": "sprite"},
        {"id": 211, "name": "Delta Shrinker", "type": "sprite"},
        {"id": 224, "name": "Alpha Armor", "type": "sprite"},
        {"id": 225, "name": "Gamma Night Vision Goggles", "type": "sprite"},
        {"id": 226, "name": "Beta Medkit", "type": "sprite"},
        {"id": 257, "name": "Center Holo Duke", "type": "sprite"},
        {"id": 258, "name": "Center Devastator", "type": "sprite"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]

    def main_region(self) -> Region:
        r = self.rules
        # Nothing to see here
        ret = self.region(self.name, [loc["name"] for loc in self.location_defs])
        # Just step onto one of the enemies to cross the gap
        self.restrict("Exit", r.jump | r.difficulty("medium"))
        return ret
