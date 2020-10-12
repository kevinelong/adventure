from board import Board


class Interface:
    def __init__(self):
        self.default_options = {
            "0": "QUIT",
            "1": "NORTH",
            "2": "EAST",
            "3": "SOUTH",
            "4": "WEST",
        }

    def get_choice(self, options=None):
        option_list = options if options else self.default_options
        valid = False
        text = ""
        while not valid:

            for key in option_list:
                value = option_list[key]
                print(key, value)

            text = input("WHAT NOW?")

            if text in option_list:
                print(f"You chose option {text}")
                valid = True
            else:
                print(f"Invalid option {text}")
        return option_list[text]

    def show(self, text):
        print(text)

    def display(self, player, monsters):
        board = Board()
        board.place(player)
        for m in monsters:
            board.place(m)
        print(board)
