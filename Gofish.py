from Card import Card
from CardGame import CardGame
from CustomFunctions import CustomFunctions
from Player import Player

class GoFish():
    def __init__(self):
        self.deck = CardGame.CreateDeck()
        self.players = CardGame.Populate()

    def CardChoice(self, player): # Returns chosen card out of the hand.
        for num in range(len(player.hand)):
            print(f"{num + 1}: {player.hand[num]}")
        
        inp = CustomFunctions.Choice([str(num) for num in range(1, len(player.hand) + 1)], "Which card would you like to play?")

        return player.hand[int(inp) - 1]

    def PlayerChoice(self, currentPlayer, card): # Returns the chosen player out of the other players.
        otherPlayers = []
        for player in self.players:
            if player is not currentPlayer:
                otherPlayers.append(player)
        
        print(f"Your hand is {player.hand}.")

        for num in range(len(otherPlayers)):
            print(f"{num + 1}: {otherPlayers[num]}")

        inp = CustomFunctions.Choice([str(num) for num in range(1, len(otherPlayers) + 1)], f"Which player would you like to ask about the {card}?")

        return otherPlayers[int(inp) - 1]
        
    def CheckForMatch(self, otherPlayer, card): # I need to check the value of each card in the other player's hand, and see if it matches a card in the otherPlayer's hand.

        for otherCard in otherPlayer.hand:
            if card.value == otherCard.value:
                return True
        
        return False

    def TakeTurn(self, currentPlayer):
        cardChoice = self.CardChoice(currentPlayer)
        playerChoice = self.PlayerChoice(currentPlayer, cardChoice)
        match = self.CheckForMatch(playerChoice, cardChoice)

        print(match, cardChoice)

game = GoFish()

currentPlayer = game.players[0]

for num in range(7):
    CardGame.TransferCard(game.deck, currentPlayer.hand)
    CardGame.TransferCard(game.deck, game.players[1].hand)

game.TakeTurn(currentPlayer)






