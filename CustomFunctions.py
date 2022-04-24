class CustomFunctions:
    @staticmethod
    def MixedSort(lst):
        ints = []
        strings = []

        for element in lst:
            if type(element) is int:
                ints.append(element)
            elif type(element) is str:
                strings.append(element)
        
        return ints, strings
   
    @staticmethod
    def Choice(choices, message): # Returns the choice made.
        choice = None

        while choice not in choices:
            if choice is not None:
                print("Please try again! ")
            choice = input(f"{message}\n")

        return choice
