from CardGame import CardGame

class Solitaire:
    
    def __init__(self):
        self.deck = CardGame.CreateDeck()


game = Solitaire()

for card in game.deck:
    print(card)

