from abc import ABC, abstractmethod

class InputInterface(ABC):

    @abstractmethod
    def get_income(self):
        pass
    
    @abstractmethod
    def ask(self):
        pass