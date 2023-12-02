from BaseClasses import Region

from ..base_classes import D3DLevel


class E4L3(D3DLevel):
    name = "Shop-N-Bag"
    levelnum = 2
    volumenum = 3
    keys = ["Blue", "Red", "Yellow"]
    location_defs = [
        {"id": 18, "mp": True, "name": "MP Seal Chaingun", "type": "sprite"},
        {"id": 21, "name": "Warehouse Pipebombs", "type": "sprite"},
        {"id": 32, "name": "Openable Box Armor", "type": "sprite"},
        {"id": 39, "name": "Storage Upper Freezethrower", "type": "sprite"},
        {"id": 40, "name": "Storage Upper Pipebombs", "type": "sprite"},
        {"id": 41, "name": "Storage Upper Night Vision Goggles", "type": "sprite"},
        {"id": 116, "mp": True, "name": "MP Blue Vent Shrinker", "type": "sprite"},
        {"id": 121, "name": "Blue Top Crate RPG", "type": "sprite"},
        {"id": 122, "mp": True, "name": "MP Outside Shotgun", "type": "sprite"},
        {"id": 126, "mp": True, "name": "MP Behind boxes RPG", "type": "sprite"},
        {"id": 130, "name": "Shop Corridor Devastator", "type": "sprite"},
        {"id": 131, "name": "Blue Fruit Tripbomb 1", "type": "sprite"},
        {"id": 132, "name": "Blue Fruit Tripbomb 2", "type": "sprite"},
        {"id": 133, "name": "Blue Fruit Tripbomb 3", "type": "sprite"},
        {"id": 134, "name": "Storage Upper Atomic Health", "type": "sprite"},
        {"id": 139, "name": "Shop Corridor Medkit", "type": "sprite"},
        {"id": 148, "name": "Crate Shotgun", "type": "sprite"},
        {"id": 158, "name": "Yellow Cashier Devastator", "type": "sprite"},
        {"id": 194, "name": "Warehouse Upper Atomic Health", "type": "sprite"},
        {"id": 228, "name": "Exploding Box Chaingun", "type": "sprite"},
        {"id": 264, "name": "Blue Vent Atomic Health", "type": "sprite"},
        {"id": 307, "name": "Behind boxes Blue Key Card", "type": "sprite"},
        {"id": 377, "name": "Blue Seal Yellow Key Card", "type": "sprite"},
        {"id": 396, "name": "Manager Office Red Key Card", "type": "sprite"},
        {"id": 426, "name": "Manager Office Pipebombs", "type": "sprite"},
        {"id": 442, "name": "Blue Fruit Armor", "type": "sprite"},
        {"id": 445, "name": "Warehouse Night Vision Goggles", "type": "sprite"},
        {"id": 446, "mp": True, "name": "MP Shop Blue Jetpack", "type": "sprite"},
        {"id": 451, "mp": True, "name": "MP Red Storage Shotgun", "type": "sprite"},
        {"id": 452, "name": "Red Storage Holo Duke", "type": "sprite"},
        {"id": 492, "name": "Manager Office Steroids", "type": "sprite"},
        {"id": 542, "name": "Trash Comp Medkit", "type": "sprite"},
        {"id": 547, "name": "Red Storage Steroids", "type": "sprite"},
        {"id": 549, "name": "Trash Comp Protective Boots", "type": "sprite"},
        {"id": 70, "name": "Exploding Box Secret", "type": "sector"},
        {"id": 176, "name": "Shop Corridor Secret", "type": "sector"},
        {"id": 274, "name": "Yellow Cashier Secret", "type": "sector"},
        {"id": 344, "name": "Storage Upper Secret", "type": "sector"},
        {"id": 349, "name": "Openable Box Secret", "type": "sector"},
        {"id": 362, "name": "Trash Comp Secret", "type": "sector"},
        {"id": 365, "name": "Red Storage Secret", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]

    def main_region(self) -> Region:
        r = self.rules
        ret = self.region(
            self.name,
            [
                "MP Outside Shotgun",
            ],
        )

        over_fence = self.region(
            "Over fence",
            [
            ],
        )
        # Can sr50 over the fence around the corner
        self.connect(ret, over_fence, r.difficulty("hard") | r.jump)

        over_fence_container = self.region(
            "Over fence container",
            [
                "Crate Shotgun",
            ],
        )
        self.connect(over_fence, over_fence_container, r.jump)   

        over_fence_warehouse = self.region(
            "Over fence warehouse",
            [
                "Warehouse Pipebombs",
                "Warehouse Night Vision Goggles",
            ],
        )
        self.connect(over_fence, over_fence_warehouse, r.can_crouch)

        warehouse_upper = self.region(
            "Warehouse Upper",
            [
                "Warehouse Upper Atomic Health",
            ],
        )
        # I once got up here with just walk and sr50, couldnt reproduce yet
        self.connect(over_fence_warehouse, warehouse_upper, r.jump)

        shop_inside = self.region(
            "Shop Inside",
            [
                "Shop Corridor Secret",
                "Shop Corridor Devastator",
                "Shop Corridor Medkit",
                "Openable Box Secret",
                "Openable Box Armor",
            ],
        )
        # Strafe on the fence and sr40/sr50 into the shop window
        self.connect(ret, shop_inside, r.jump | r.difficulty("hard") & r.can_sprint)

        behind_boxes = self.region(
            "Behind boxes",
            [
                "MP Behind boxes RPG",
                "Behind boxes Blue Key Card",
            ],
        )
        self.connect(shop_inside, behind_boxes, r.jump)

        shop_blue = self.region(
            "Shop Blue Key Area",
            [
                "MP Shop Blue Jetpack",
            ],
        )
        self.connect(shop_inside, shop_blue, self.blue_key)

        exploding_box = self.region(
            "Exploding Box",
            [
                "Exploding Box Secret",
                "Exploding Box Chaingun",
            ],
        )
        self.connect(shop_blue, exploding_box, r.explosives)

        blue_fruits = self.region(
            "Blue Fruit Area",
            [
                "Blue Fruit Armor",
                "Blue Fruit Tripbomb 1",
                "Blue Fruit Tripbomb 2",
                "Blue Fruit Tripbomb 3",
            ],
        )
        # Can diagonal walk up in corner, easier with sprint?
        # Extreme difficulty strat needs to be double checked
        #| r.difficulty("extreme"))
        self.connect(shop_blue, blue_fruits, 
                     r.jump |
                     r.difficulty("hard") & r.can_sprint)
                     
        blue_upper = self.region(
            "Shop Blue Key Area Vent",
            [
                "Blue Vent Atomic Health",
                "Blue Top Crate RPG",
                "MP Blue Vent Shrinker",
                "MP Blue Seal Chaingun",
                "Blue Seal Yellow Key Card", 
            ],
        )
        self.connect(shop_blue, blue_upper, r.jump)

        yellow_cashier = self.region(
            "Yellow Key Cashier Area",
            [
                "Manager Office Steroids",
            ],
        )
        self.connect(shop_blue, yellow_cashier, self.yellow_key)

        manager_upper = self.region(
            "Yellow Key Cashier Area",
            [
                "Manager Office Pipebombs",
                "Manager Office Red Key Card",
            ],
        )
        # Can climb up to crates over the crack, permanently gone if blown up
        self.connect(yellow_cashier, manager_upper, r.jump | r.difficulty("medium"))
        

        yellow_cashier_secret = self.region(
            "Yellow Cashier Secret",
            [
                "Yellow Cashier Secret",
                "Yellow Cashier Devastator",
            ],
        )
        self.connect(yellow_cashier, yellow_cashier_secret, r.jump)

        storage_red = self.region(
            "Red Key Storage Area",
            [
                "Red Storage Holo Duke",
                "MP Red Storage Shotgun",
                "Red Storage Steroids",
                "Red Storage Secret",
            ],
        )
        self.connect(shop_blue, storage_red, self.red_key)

        storage_red_upper = self.region(
            "Red Key Storage Upper Area",
            [
                "Storage Upper Atomic Health",
                "Storage Upper Secret",
                "Storage Upper Freezethrower",
                "Storage Upper Pipebombs",
                "Storage Upper Night Vision Goggles",
            ],
        )
        self.connect(storage_red, storage_red_upper ,self.red_key)

        trash_compactor = self.region(
            "Trash Compactor",
            [
                "Trash Comp Protective Boots",
                "Trash Comp Medkit",
                "Trash Comp Secret",
                "Exit",
            ],
        )
        # Jump to door opening button
        self.connect(storage_red, trash_compactor, r.jump)