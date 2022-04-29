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

        # TODO: Put the rest of the card deck into the stack. Deck was really just a placeholder. 

game = Solitaire()

game.InitializeBoard()

for lst in game.listOfColumns:
    plural = ""
    if lst != game.listOfColumns[1]:
        plural = "s"
    print(f"{len(lst) - 1} hidden card{plural}, {lst[-1]}")