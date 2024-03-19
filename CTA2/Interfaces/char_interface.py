from abc import ABC, abstractmethod

class CharInterface(ABC):

    @abstractmethod
    def set_string(self):
        pass
    
    @abstractmethod
    def check_char(self):
        pass