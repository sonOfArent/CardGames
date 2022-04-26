from CardGame import CardGame
from Player import Player
from CustomFunctions import CustomFunctions


# This is a complicated card game to recreate, as the game involves many separate groups of cards co-existing in many different ways. However, it shouldn't be too much more difficult than, say, Blackjack, it'll just take a bit longer to figure some things out.

class RummyGame():

    def CheckifValid(self, card, lstToCheckAgainst): # Check if the card you're wanting to add is valid to add.
        if len(lstToCheckAgainst) < 3:
           
            # If it's not being played off of someone else...
            return False




# DONE: Already I can see an issue where if another player played some cards off of someone else, I'd have to ensure that my function can understand that. ######
# TODO: Scratch that above, I already know a way to fix that. I don't actually have to have the cards pointing back to where they were played, just that the points are registered for the person playing them.
# TODO: I can instead have all the cards migrating to the same static playedLists and figure it out from there!

# TODO: I can do it this way: I have the player input the list of cards they want to play and the player they want to play them off of. It then checks each of these cards against each of the chosen player's groups, and returns all the groups that the cards can be played off of. 
        
# TODO: Potentially, I can have the card(s) in question go through two functions: CheckForDuplicateGroup() and CheckForLineGroup(). In each, I have the card(s) go through the similar steps: for each card, if the card matches up with any of the groups, I return each group it matches up with. Then, if the  