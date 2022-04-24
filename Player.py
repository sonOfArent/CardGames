class Player:
    def __init__(self):
        self.name = input("What is this player's name?\n")
        self.hand = []

    def __repr__(self):
        return self.name

