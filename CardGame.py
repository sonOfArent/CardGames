import random
from Card import Card
from Player import Player

class CardGame(Card):

    @staticmethod
    def TransferCard(fromLst, toLst, card = None):
        if card == None: card = fromLst[0]

        fromLst.remove(card)
        toLst.append(card)

        return card
    
    @staticmethod
    def CreateDeck(type = None):
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
        suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
        deck = []
        
        if type == None:
            for suit in suits:
                for value in values:
                    deck.append(Card(suit, value))
        # elif type this or that, etc.

        random.shuffle(deck)
        return deck
    
    @staticmethod
    def Populate():
        playerCount = input("How many players would you like?\n")
        while type(playerCount) is not int:
            try:
                print("Trying to int-ify it...")
                playerCount = int(playerCount)

            except:
                print("Didn't work.")
                print("Please input a number!\n")
        
        print("int-ify successful!")
        playerLst = [Player() for num in range(playerCount)]

        return playerLst

    @staticmethod
    def SwitchTurn(playerLst):
        print(f"It was {playerLst[0]}'s turn.")

        movedPlayer = playerLst.pop(0)
        playerLst.append(movedPlayer)

        print(f"It's now {playerLst[0]}'s!")

    @staticmethod
    def PlayerLost(player, playerLst):
        print(f"{player} lost, and is out of the game!")
        CardGame.SwitchTurn(playerLst)
        playerLst.remove(player)



    @staticmethod
    def PlayerWon(player):
        print(f"{player} won! Game over!")


    