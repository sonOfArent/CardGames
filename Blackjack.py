from CardGame import CardGame
from CustomFunctions import CustomFunctions
from Player import Player

class BlackjackGame():
    # We need to add the different functions we'll need here, to play a game of BlackJack. This will include everything done that is unique to BlackJack.
    
    def __init__(self):
        self.deck = CardGame.CreateDeck()
        self.players = CardGame.Populate()
        self.endPlayers = []
        self.scores = []
        for player in self.players:
            card = CardGame.TransferCard(self.deck, player.hand)

    rules = """
    So here's the way the game is played:
        a) The dealer hands one card to each player.
        b) Each player decides if they're going to hit (draw another card), or fold (stick with the hand value they have).
        c) The closer they reach 21, the better their hand is, but if they go over, they bust (lose).
        d) The player closest to 21 wins!
    """

    @staticmethod
    def Hit(deck, hand):
        card = CardGame.TransferCard(deck, hand)
        print(card)

    @staticmethod
    def Fold(player, playerLst, scoreLst, endPlayerLst):
        # Take player out of loop, and record his score.
        CardGame.SwitchTurn(playerLst)
        playerLst.remove(player)
        endPlayerLst.append(player)
        scoreLst.append(BlackjackGame.CheckHandValue(player.hand))
        print(f"Player {player.name} folded, with {BlackjackGame.CheckHandValue(player.hand)} hand score!")

    @staticmethod
    def CheckHandValue(hand):
        handValue = 0

        values = [] # We want to pass in the values of the cards, not the card objects theselves.
        for card in hand:
            values.append(card.value)

        ints, strings = CustomFunctions.MixedSort(values)

        for i in ints:
            handValue += i
        
        for string in strings:
            if string in ["J", "Q", "K"]:
                handValue += 10
        
        for string in strings:
            if string == "A":
                if handValue <= 10:
                    handValue += 11
                else:
                    handValue += 1 
                
        return handValue

    @staticmethod
    def HandState(hand):
        handValue = BlackjackGame.CheckHandValue(hand)
        state = ""

        if handValue < 21:
            state = "Still in the game."
        elif handValue == 21:
            state = "Win!"
        elif handValue > 21:
            state = "Bust!"
        
        return state, handValue

    @staticmethod
    def Choice(player):
        print(f"Your hand, {player.hand}, is worth {BlackjackGame.CheckHandValue(player.hand)}.\n")
        
        choice = None
        while choice not in ["h", "f"]:
            if choice is not None:
                print("Please try again! ")
            choice = input("Would you like to (h)it or (f)old?\n")
        
        return choice

    @staticmethod
    def TakeTurn(player, playerLst, deck, hand, scoreLst, endPlayerLst):
        choice = BlackjackGame.Choice(player)

        match choice:
            case "h":
                BlackjackGame.Hit(deck, hand)
                state, handValue = BlackjackGame.HandState(hand)
                print(state, handValue, hand)
                return state, handValue
            case "f":
                BlackjackGame.Fold(player, playerLst, scoreLst, endPlayerLst)


game = BlackjackGame()
while len(game.players) > 0:

    currentPlayer = game.players[0]

    state, handValue = game.TakeTurn(game.players[0], game.players, game.deck, game.players[0].hand, game.scores, game.endPlayers)

    print(state)
    if handValue >= 21:
        game.players.remove(currentPlayer)
        game.endPlayers.append(currentPlayer)
        game.scores.append(handValue)
        print(f"It is now {game.players[0]}'s turn!")

    elif handValue < 21:
        if len(game.players) > 1:
            CardGame.SwitchTurn(game.players)
        else:
            print("Turn kept, last player in!")

print(f"""Game Ended, scores are as follows:
{game.endPlayers[0]}: {game.scores[0]}!
{game.endPlayers[1]}: {game.scores[1]}!
{game.endPlayers[2]}: {game.scores[2]}!
""")

# TODO: So before I attempt to switch the turns, I need to check for if there are any players left in the game.
# TODO: I need to reconfigure the file because I need to have both a BlackjackRound and a BlackjackGame function. I need to configure it because there are several rounds in a game, and the way I have it set up right now, it reinitializes everything at file startup. This wouldn't be too bad an issue, except for the fact that I'd like to do several things, such as implement a database system for player stats and also play several rounds with the same deck.
# TODO: In the while loop, hand and value don't have values when a player folds. Instead of fixing this like I should, I'm going to rewrite a bunch of this code to fix it and reroute everything.

