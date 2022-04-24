from CardGame import CardGame
from CustomFunctions import CustomFunctions
from Player import Player

class BlackjackGame():
    # We need to add the different functions we'll need here, to play a game of BlackJack. This will include everything done that is unique to BlackJack.
    
    def __init__(self):
        self.deck = CardGame.CreateDeck()
        self.players = CardGame.Populate()
        self.endPlayers = self.players
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
        # endPlayerLst.append(player)
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
                print(state, handValue, deck, hand)
            case "f":
                BlackjackGame.Fold(player, playerLst, scoreLst, endPlayerLst)


game = BlackjackGame()
while len(game.players) > 0:

    try:
        game.TakeTurn(game.players[0], game.players, game.deck, game.players[0].hand, game.scores, game.endPlayers)
    except:
        break
    CardGame.SwitchTurn(game.players)

print(f"""Game Ended, scores are as follows:
{game.endPlayers[0]}: {game.scores[0]}!
{game.endPlayers[1]}: {game.scores[1]}!
{game.endPlayers[2]}: {game.scores[2]}!
""")

# TODO: My Fold() method is no longer removing players from the game.player list. 
# TODO: My current problem is trying to append the player to the endPlayerLst in the Fold() method. I don't know why, but I've run out of time on my break to figure it out.