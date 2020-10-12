from random import randint
from location import Location
from items import *


class Character:
    def __init__(self,
                 name="character",
                 description="a self character",
                 strength=9,
                 dexterity=9,
                 health=100,
                 item_count=0):

        self.strength = strength
        self.dexterity = dexterity
        self.name = name
        self.description = description
        self.health = health
        self.inventory = []
        self.location = Location()

        for i in range(item_count):
            self.add_random_item()

    def __str__(self):
        return f"NAME: {self.name}, HEALTH: {self.health}"

    def collect(self, item):
        if item.kind == "HEALTH" and (100 - self.health) >= item.health_bonus_percent:
            self.health += item.health_bonus_percent
        else:
            self.inventory.append(item)

    def display_inventory(self):
        print("INVENTORY:")
        for item in self.inventory:
            print(f"\t{item}")

    def attack(self, opponent):
        limit = self.strength
        number = randint(1, limit) + randint(1, limit) + randint(1, limit)
        number -= randint(1, opponent.dexterity)
        opponent.health -= number
        print(f"{self.name} does {number} damage to {opponent.name}")

    def add_random_item(self):
        data = [FirstAidKit(), FirstAidKit(), FirstAidKit(), Gold(100), Gold(500), Sword()]
        index = randint(0, len(data) - 1)
        self.collect(data[index])


class Ogre(Character):
    def __init__(self):
        super().__init__(name="Ogre", health=50, item_count=3)


class Player(Character):
    def __init__(self):
        super().__init__(name="Player", health=100)
