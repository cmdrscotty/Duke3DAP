from BaseClasses import Region

from ..base_classes import D3DLevel


class E3L2(D3DLevel):
    name = "Bank Roll"
    levelnum = 1
    volumenum = 2
    keys = ["Blue", "Red"]
    location_defs = [
        {"id": 54, "name": "Top of Gears Protective Boots", "type": "sprite"},
        {"id": 66, "name": "Start Pipebombs", "type": "sprite"},
        {"id": 85, "name": "Vending Machine Atomic Health", "type": "sprite"},
        {"id": 96, "name": "ATM Chaingun", "type": "sprite"},
        {"id": 106, "name": "Pillar Pipebombs", "type": "sprite"},
        {"id": 223, "name": "Bank Phone Holo Duke", "type": "sprite"},
        {
            "id": 264,
            "name": "Dumpster Trashcan Steroids",
            "type": "sprite",
            "sprite_type": "trashcan",
        },
        {"id": 265, "name": "Dumpster Medkit", "type": "sprite"},
        {"id": 354, "name": "Top of Gears Jetpack", "type": "sprite"},
        {"id": 355, "name": "Red Key Card", "type": "sprite"},
        {"id": 424, "name": "Start Shotgun", "type": "sprite"},
        {"id": 425, "name": "Start Ledge RPG", "type": "sprite"},
        {"id": 440, "name": "Blue Key Card", "type": "sprite"},
        {"id": 484, "name": "Office Painting Devastator", "type": "sprite"},
        {"id": 503, "name": "Bank Painting Jetpack", "type": "sprite"},
        {"id": 506, "name": "Office Steroids", "type": "sprite"},
        {"id": 507, "name": "Office Entrance Freezethrower", "type": "sprite"},
        {"id": 511, "name": "Switch Shrinker", "type": "sprite"},
        {"id": 512, "name": "Office Entrance Pipebombs", "type": "sprite"},
        {"id": 516, "name": "Office Ledge Armor", "type": "sprite"},
        {"id": 517, "name": "Office Far Ledge Atomic Health", "type": "sprite"},
        {"id": 518, "name": "Office Far Ledge Tripmine 1", "type": "sprite"},
        {"id": 519, "name": "Office Far Ledge Tripmine 2", "type": "sprite"},
        {"id": 533, "name": "Exit Medkit", "type": "sprite"},
        {"id": 537, "name": "Gear Protective Boots", "type": "sprite"},
        {"id": 539, "name": "Gear Atomic Health", "type": "sprite"},
        {"id": 17, "name": "Secret Bank Phone", "type": "sector"},
        {"id": 119, "name": "Secret ATM", "type": "sector"},
        {"id": 190, "name": "Secret Office Painting", "type": "sector"},
        {"id": 208, "name": "Secret Bank Painting", "type": "sector"},
        {"id": 235, "name": "Secret Gears Breakable Wall", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]

    def main_region(self) -> Region:
        r = self.rules
        ret = self.region(
            self.name,
            [
                "Dumpster Medkit",
                "Start Pipebombs",
                "Start Shotgun",
                "Dumpster Trashcan Steroids",
                "Pillar Pipebombs",
                "Office Entrance Pipebombs",
                "Office Entrance Freezethrower",
                "Office Entrance",
                "Blue Key Card",
                "Office Steroids",
                "Office Ledge Armor",
                "Start Ledge RPG",
            ],
        )
        self.restrict(
            "Start Ledge RPG",
            r.jetpack(50)
            | (r.can_jump & (r.can_sprint | r.steroids))
            # need specifically an enforcer to jump up
            | (r.difficulty("hard") & r.can_jump),
        )

        far_ledge = self.region(
            "Office Far Ledge",
            [
                "Office Far Ledge Atomic Health",
                "Office Far Ledge Tripmine 1",
                "Office Far Ledge Tripmine 2",
            ],
        )
        self.connect(
            ret, far_ledge, r.jump | r.can_sprint | r.steroids
        )  # Can maybe SR50 the gap from the other ledge

        office_ledges = self.region(
            "Office Ledges",
            [
                "Vending Machine Atomic Health",
                "Office Painting Devastator",
                "Secret Office Painting",
            ],
        )
        self.connect(ret, office_ledges, r.jump)

        atm = self.region(
            "ATM",
            ["ATM Chaingun", "Secret ATM"],
        )
        self.connect(
            ret, atm, r.jump | (r.difficulty("medium") & (r.can_sprint | r.steroids))
        )  # Can run off the ledge, timing is a bit tricky with steroids + no run

        bank = self.region("Bank Entrance", ["Switch Shrinker"])
        self.connect(ret, bank, self.blue_key)

        bank_secrets = self.region(
            "Bank Entrance Secrets",
            [
                "Bank Phone Holo Duke",
                "Secret Bank Phone",
                "Secret Bank Painting",
                "Bank Painting Jetpack",
            ],
        )
        self.connect(bank, bank_secrets, r.jump)

        gears = self.region(
            "Gear Room",
            [
                "Gear Protective Boots",
                "Top of Gears Protective Boots",
                "Top of Gears Jetpack",
                "Red Key Card",
            ],
        )
        self.connect(bank, gears, r.jump)  # the trigger plates are just a bit too tall

        gears_secret = self.region(
            "Gears Secret", ["Secret Gears Breakable Wall", "Gear Atomic Health"]
        )
        self.connect(gears, gears_secret, r.explosives)

        vault = self.region("Bank Vault", ["Exit Medkit", "Exit"])
        # Can shoot rockets through the wall corner, precise setup and deadly if you get it wrong
        self.connect(
            bank,
            vault,
            self.red_key | (r.glitched & r.difficulty("hard") & (r.rpg | r.devastator)),
        )
        self.connect(gears_secret, vault, r.pipebomb)  # Can throw through crack

        return ret
