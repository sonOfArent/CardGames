from Card import Card
from CardGame import CardGame
from CustomFunctions import CustomFunctions
from Player import Player

class GoFish():
    def __init__(self):
        self.deck = CardGame.CreateDeck()
        self.players = CardGame.Populate()
        self.pairs = {}

        for player in self.players:
            self.pairs[player] = []
            print(f"Player {player}'s pairs: {self.pairs[player]}")

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

        playerChoice = otherPlayers[int(inp) - 1]
        return playerChoice
        
    def CheckForMatch(self, otherPlayer, card): # I need to check the value of each card in the other player's hand, and see if it matches a card in the otherPlayer's hand.

        for otherCard in otherPlayer.hand:
            if card.value == otherCard.value:
                return otherCard
        
        return False

    def TakeTurn(self):
        currentPlayer = self.players[0]
        cardChoice = self.CardChoice(currentPlayer)
        playerChoice = self.PlayerChoice(currentPlayer, cardChoice)
        matched = self.CheckForMatch(playerChoice, cardChoice)

        if type(matched) == Card:
            pair = []

            CardGame.TransferCard(currentPlayer.hand, pair, cardChoice)
            CardGame.TransferCard(playerChoice.hand, pair, matched)
            self.pairs[currentPlayer].append(pair)

        else:
            print("Go Fish!")
            CardGame.TransferCard(self.deck, currentPlayer.hand)

        print(currentPlayer.hand, self.pairs[currentPlayer])

game = GoFish()

currentPlayer = game.players[0]

for num in range(7):
    CardGame.TransferCard(game.deck, currentPlayer.hand)
    CardGame.TransferCard(game.deck, game.players[1].hand)

while True:
    game.TakeTurn()
    CardGame.SwitchTurn(game.players)

# TODO: If any hand size is 0, the game is over and that player wins.