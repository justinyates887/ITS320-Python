from Interfaces.tax_bracket_interface import TaxBracketInterface

class TaxBracket(TaxBracketInterface):

    #WARNING: private members cannot be constant
    __BRACKET = {
        0: .10,
        1: .15,
        2: .20,
        3: .30
    }

    def get_bracket(self):
        return self.__BRACKET
    
    def get_effective_tax_rate(self, income):
        return self.__BRACKET[self.__find_tax_bracket(income)]
    
    def __find_tax_bracket(self, income):
        if(income < 500):
            return 0
        elif(income < 1500):
            return 1
        elif(income < 2500):
            return 2
        elif(income >= 2500):
            return 3
        else:
            raise ValueError("Income was not as expected.")