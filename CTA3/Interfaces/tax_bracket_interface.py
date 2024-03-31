from abc import ABC, abstractmethod

class TaxBracketInterface(ABC):

    @abstractmethod
    def get_bracket(self):
        pass
    
    @abstractmethod
    def get_effective_tax_rate(self, income):
        pass