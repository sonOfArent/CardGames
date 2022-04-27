from CardGame import CardGame
from Player import Player
from CustomFunctions import CustomFunctions

class RummyGame():

    def __init__(self):

        self.deck = CardGame.CreateDeck("rummy")
        self.players = CardGame.Populate()
        self.discardLine = []
        self.runsAndBooks = []

    def CheckCardsForValidPlays(self, cardsToCheck, listOfLists): # Checking for every run that the chosen cards could be applied to.
        
        cardsToCheckCopy = [card for card in cardsToCheck]

        validRuns = []

        for lst in listOfLists:
            cardMash = []
            
            # Add the cards to the cardMash.
            for card in lst:
                cardMash.append(card)
            for card in cardsToCheckCopy:
                cardMash.append(card)

            # Sort it all.
            cardMash.sort()

            if cardMash[0].value == cardMash[-1].value:
                type = "book"
            else:
                type = "run"


            lstIsValid = True

            if type == "run":

                for num in range(len(cardMash)):

                    if num == 0:
                        continue

                    if cardMash[num].value - 1 != cardMash[num - 1].value:
                        lstIsValid = False

            elif type == "book":

                if cardMash[0].value != cardMash[1].value:
                    lstIsValid = False

            if lstIsValid:
                validRuns.append(lst)
            
        return validRuns

    def ChooseCards(self, player):
        cardsChosen = []

        keepAddingCards = True

        while keepAddingCards == True:
            inp = CustomFunctions.Choice(player.hand, f"Which card would you like to add to the 'to play' list, {player}?")

            CardGame.TransferCard(player.hand, cardsChosen, player.hand[int(inp) + 1])

            inp = CustomFunctions.Choice(['y', 'n'], "Would you like to add another card?")

            if inp == 'n':
                keepAddingCards = False

            # TODO: Change the numbers in CheckCardForValidPlays to actual cards and their values.


rummy = RummyGame()

listOfLists = [[8, 8, 8], [1, 2, 3], [5, 6, 7]]
checks = [[4, 5], [4], [8], [1, 4, 5]]

for toCheck in checks:
    plays = rummy.CheckCardsForValidPlays(toCheck, listOfLists)
    if len(plays) > 1:
        plural = "lists"
    else:
        plural = "list"

    print(f"The check {toCheck} fits into the {plural} {plays}.")

