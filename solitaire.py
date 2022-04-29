from CardGame import CardGame

class Solitaire:
    
    def __init__(self):
        self.deck = CardGame.CreateDeck("solitaire")
        self.stack = []
        self.listOfColumns = []
        self.listOfFinishedPiles = []

    def InitializeBoard(self):
        for i in range(1, 8):
            listToAppend = []
            for num in range(i):
                CardGame.TransferCard(self.deck, listToAppend)

            self.listOfColumns.append(listToAppend)

game = Solitaire()

game.InitializeBoard()

for lst in game.listOfColumns:
    print(f"{len(lst) - 1} hidden cards, {lst[-1]}")