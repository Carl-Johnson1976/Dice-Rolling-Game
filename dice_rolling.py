import random


dices = [
    """
         ___________ 
        |           |
        |           |
        |     O     |
        |           |
        |___________|
    """,
    """
         ___________ 
        |           |
        |  O        |
        |           |
        |        O  |
        |___________|
    """,
    """
         ___________ 
        |           |
        |  O        |
        |     O     |
        |        O  |
        |___________|
    """,
    """
         ___________ 
        |           |
        |  O     O  |
        |           |
        |  O     O  |
        |___________|
    """,
    """
         ___________ 
        |           |
        |  O     O  |
        |     O     |
        |  O     O  |
        |___________|
    """,
    """
         ___________ 
        |           |
        |  O     O  |
        |  O     O  |
        |  O     O  |
        |___________|
    """
]


class dice_rolling():
    def __init__(self):
        num_roll = input("How many dice you wanna roll?\n-> ")
        if num_roll.isnumeric():
            self.Play(num_roll)
        else:
            print("Please enter number.")
            self.__init__()

    def Play(self, num_roll):
        for i in range(int(num_roll)):
            self.dice_graphic()
        self.__init__()

    def dice_graphic(self):
        select = random.randint(1, 6)
        print(dices[select - 1])



dice_rolling()