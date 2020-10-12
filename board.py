from characters import *


class Board:
    def __init__(self, size=9):
        self.size = size
        self.rows = []
        self.symbols = {
            "<class \'characters.Player\'>":    "^",
            "<class \'characters.Ogre\'>":      "O",
            "<class \'characters.Character\'>": "C",
        }
        self.reset()

    def get_symbol(self, item):
        t = str(type(item))
        if t in self.symbols:
            return self.symbols[t]
        else:
            return "?"

    def reset(self):
        self.rows = []
        for row_index in range(self.size):
            values = []
            for value_index in range(self.size):
                values.append(".")
            self.rows.append(values)

    def place(self, item):
        r = item.location.row - 1
        c = item.location.column - 1
        self.rows[r][c] = self.get_symbol(item)

    def __str__(self):
        output = []
        for row in self.rows:
            output.append(" ".join(row))
        return "\n".join(output)
