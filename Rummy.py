from Card import Card
from CardGame import CardGame
from Player import Player
from CustomFunctions import CustomFunctions

class RummyGame():

    def __init__(self):

        self.deck = CardGame.CreateDeck("rummy")
        self.players = CardGame.Populate()
        self.discardLine = []
        self.runsAndBooks = []
        CardGame.TransferCard(self.deck, self.discardLine)

    def CheckCardsForValidPlays(self, cardsToCheck, listOfLists): # Checking for every run that the chosen cards could be applied to.
        
        cardsToCheckCopy = [card for card in cardsToCheck]

        validRuns = []

        for lst in listOfLists:
            cardMash = []
            
            # Add the cards to the cardMash.
            for card in lst:
                cardMash.append(card.value)
            for card in cardsToCheckCopy:
                cardMash.append(card.value)

            # Sort it all. It sorts by < and >, so the cardMash has to be the values of the cards.
            cardMash.sort()

            if cardMash[0] == cardMash[-1]:
                type = "book"
            else:
                type = "run"


            lstIsValid = True

            if type == "run":

                for num in range(len(cardMash)):

                    if num == 0:
                        continue

                    if cardMash[num] - 1 != cardMash[num - 1]:
                        lstIsValid = False

            elif type == "book":

                if cardMash[0] != cardMash[1]:
                    lstIsValid = False

            if lstIsValid:
                validRuns.append(lst)
            
        return validRuns

    def ChooseCards(self, player):
        cardsChosen = []

        for card in player.hand:
            print(f"{player.hand.index(card) + 1}: {card}")

        if len(cardsChosen) > 1:
            print(f"Cards chosen so far:\n")

            for card in cardsChosen:
                print(card)
        else:
            print("No cards chosen so far!")

        keepAddingCards = True

        while keepAddingCards == True:
            inp = CustomFunctions.Choice([str(num + 1) for num in range(len(player.hand))], f"Which card would you like to add to the 'to play' list, {player}?")

            CardGame.TransferCard(player.hand, cardsChosen, player.hand[int(inp) + 1])

            print(f"Cards chosen so far:\n")

            for card in cardsChosen:
                print(card)

            inp = CustomFunctions.Choice(['y', 'n'], "Would you like to add another card?")

            print(f"Cards chosen so far:\n")

            for card in cardsChosen:
                print(card)

            if inp == 'n':
                keepAddingCards = False

        return cardsChosen

game = RummyGame()

for num in range(7):
    CardGame.TransferCard(game.deck, game.players[0].hand)

# toPrint = game.CheckCardsForValidPlays(game.players[0].hand[:3], listOfLists)
# print(toPrint)

# for toCheck in checks:
#     plays = rummy.CheckCardsForValidPlays(toCheck, listOfLists)
#     if len(plays) > 1:
#         plural = "lists"
#     else:
#         plural = "list"

#     print(f"The check {toCheck} fits into the {plural} {plays}.")

cardsChosen = game.ChooseCards(game.players[0])