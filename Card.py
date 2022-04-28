class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        if self.value in [num for num in range(2, 11)]:
            return (f"{self.value} of {self.suit}")
        else:
            match self.value:
                case 1:
                    return f"Ace of {self.suit}"
                case 11:
                    return f"Jack of {self.suit}"
                case 12:
                    return f"Queen of {self.suit}"
                case 13:
                    return f"King of {self.suit}"