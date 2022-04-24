from CardGame import CardGame
from CustomFunctions import CustomFunctions

class BlackjackGame():
    # Restructuring my code, I want to make this the overall object, and initialize new BlackjackRounds in order to play each round. This way, the data from each round is saved.
    def __init__(self):
        self.deck = CardGame.CreateDeck()
        self.players = CardGame.Populate()
        self.finishedRounds = [] # Holds the finished Round objects.

    def PrintPlayerPosition(self, player): # Prints the player, the hand, and the value.
            print(f"{player}'s hand, {player.hand}, is worth {self.CheckHandValue(player.hand)}.\n")

    def Choice(self, choices, message): # Returns the choice made.
        choice = None

        while choice not in choices:
            if choice is not None:
                print("Please try again! ")
            choice = input(f"{message}\n")

        return choice

    def CheckHandValue(self, hand): # Returns value of the hand.
        handValue = 0
        
        values = []
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

    def HandState(self, hand): # Just returns the hand value and the current player state.
        handValue = self.CheckHandValue(hand)
        state = ""

        if handValue < 21:
            state = "Still in the game."
        elif handValue == 21:
            state = "Win!"
        elif handValue > 21:
            state = "Bust!"
        
        return handValue, state
        
    def RoundFinish(self, round): # add the round to the finishedRounds list.
        self.finishedRounds.append(round.scores)

    def PlayRound(self): # Play a full round.
        # currentRound = None
        currentRound = BlackjackRound()

        while len(currentRound.roundPlayers) > 0:
            currentPlayer = currentRound.roundPlayers[0]
            currentRound.TakeTurn(currentPlayer)

            if len(currentRound.roundPlayers) == 0: break

            if len(currentRound.roundPlayers) > 1:
                CardGame.SwitchTurn(currentRound.roundPlayers)
            else:
                print(f"{currentPlayer} is the last player still in!")

        # print(f"The round scores are as follows:")
        # for key, value in currentRound.scores.items():
        #     print(key, value)

        self.RoundFinish(currentRound)

    def PrintScores(self): # Iterating through the dict of dicts to retrieve the scores.
        currentRound = 0
        for roundScore in self.finishedRounds:
            currentRound += 1
            for key, value in roundScore.items():
                print(key, value, f"Round {currentRound}")
        

class BlackjackRound():

    def __init__(self):
        self.scores = {} # I can hold the player/scores in a dict instead of two separate lists.
        self.roundPlayers = [] # TODO: Sync with Game's playerList. Need copy for own mutability.
        for player in game.players:
            self.roundPlayers.append(player)
    
    def __repr__(self):
        return f"Round"

    def Hit(self, hand, retrn = False): # Basically just draws, but called fancy. Can return if desired.
        card = CardGame.TransferCard(game.deck, hand)
        if retrn: return card

    def Fold(self, player): # Shows player stats, and removes them from the roundPlayers list.
        handValue = game.CheckHandValue(player.hand)
        self.scores[player] = handValue

        self.roundPlayers.remove(player)
        
        print(f"Player {player} folds with a hand value of {handValue}!")

    def TakeTurn(self, player):
        choice = game.Choice(["h", "f"], "Would you like to (h)it or (f)old?")

        match choice:
            case "h":
                print(f"Player {player} has chosen to hit!")
                self.Hit(player.hand)
            case "f":
                print(f"Player {player} has chosen to fold!")
                self.Fold(player)

game = BlackjackGame()
game.PlayRound()

playAnother = game.Choice(["y", "n"], "Would you like to play another? type y or n.")

while playAnother == "y":
    game.PlayRound()
    game.PrintScores()

    playAnother = game.Choice(["y", "n"], "Would you like to play another? type y or n.")

