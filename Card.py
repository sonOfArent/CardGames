class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        if self.suit in ["Red", "Black"]:

            if self.value == 1:
                return f"{self.suit} Ace"
            if self.value == 11:
                return f"{self.suit} Jack"
            if self.value == 12:
                return f"{self.suit} Queen"
            if self.value == 13:
                return f"{self.suit} King"

            else:
                return f"{self.suit} {self.value}"

        else:
            if self.value in [1, 11, 12, 13]:
                if self.value == 1:
                    return f"Ace of {self.suit}"
                if self.value == 11:
                    return f"Jack of {self.suit}"
                if self.value == 12:
                    return f"Queen of {self.suit}"
                if self.value == 13:
                    return f"King of {self.suit}"

            else:
                return f"{self.value} of {self.suit}"