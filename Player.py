class Player:
    def __init__(self):
        self.name = input("What is this player's name?\n")
        self.hand = []
        self.user = ""

    def __repr__(self):
        return self.name
    
    def InitializeUser(self): # Create a new user in the database.
        pass

    def LinkUser(self): # Link the player to the corresponding name in the database.
        pass

    def CheckForUser(self): # Choose whether to initialize user or link user.
        pass  