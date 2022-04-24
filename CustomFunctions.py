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
