class InventoryItem:
    def __init__(self, name, kind="Treasure"):
        self.name = name
        self.kind = kind

    def __str__(self):
        return f"{self.name} {self.kind}"


class Gold(InventoryItem):
    def __init__(self, quantity):
        super().__init__("gold")
        self.quantity = quantity

    def __str__(self):
        return f"{self.quantity} {self.name} pieces."


class FirstAidKit(InventoryItem):
    def __init__(self, health_bonus_percent=25):
        super().__init__("FirstAidKit", "HEALTH")
        self.health_bonus_percent = health_bonus_percent


class Weapon(InventoryItem):
    def __init__(self, name, max_damage):
        super().__init__(name, "WEAPON")
        self.max_damage = max_damage


class Sword(Weapon):
    def __init__(self):
        super().__init__("Sword", "WEAPON")
        self.max_damage = 20

