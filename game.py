from characters import *
from interface import Interface


class Game:
    def __init__(self, interface):
        self.interface = interface
        self.player = Player()
        self.size = 9
        self.playing = True
        self.level = 1
        self.monsters = []
        self.reset()

    def reset(self):
        self.player.location.random(self.size)
        self.monsters = []
        self.populate()

    def populate(self):
        quantity = self.level * 2

        for q in range(quantity):
            ogre = Ogre()
            ogre.location.random(self.size)
            self.monsters.append(ogre)

    def play(self):
        while self.playing:
            self.interface.display(self.player, self.monsters)
            choice = self.interface.get_choice()
            self.apply_user_input(choice)
        self.interface.show("GAME OVER")

    def apply_user_input(self, choice):
        if choice == "QUIT":
            self.playing = False
        elif choice in ["NORTH", "EAST", "SOUTH", "WEST"]:
            self.player.location.move(choice)
        else:
            print("INVALID OPTION")
        self.check_collisions()

    def check_collisions(self):
        for m in self.monsters:
            if self.player.location.row == m.location.row and self.player.location.column == m.location.column:
                self.fight(m)
                if m.health <= 0:
                    for item in m.inventory:  # TAKE THE MONSTERS STUFF
                        self.player.collect(item)
                    self.monsters.remove(m)
                else:
                    self.interface.show("GAME OVER")
                    exit(0)

        if len(self.monsters) == 0:
            self.level += 1
            self.reset()

    def fight(self, monster):
        while monster.health > 0 and self.player.health > 0:
            self.player.attack(monster)
            monster.attack(self.player)
            print(self.player)
            print(monster)
        print("FIGHT OVER")
