from random import randint


class Location:
    def __init__(self, row=None, column=None):
        self.row = row
        self.column = column

    def move(self, direction):
        if direction == "NORTH":
            self.row -= 1
        elif direction == "SOUTH":
            self.row += 1
        elif direction == "EAST":
            self.column += 1
        elif direction == "WEST":
            self.column -= 1

    def random(self, size):
        self.row = randint(0, size - 1)
        self.column = randint(0, size - 1)
