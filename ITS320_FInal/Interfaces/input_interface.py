from abc import ABC, abstractmethod

class InputInterface(ABC):

    @abstractmethod
    def get_list(self):
        pass
    
    @abstractmethod
    def ask(self):
        pass

    @abstractmethod
    def run_again(self):
        pass

    @abstractmethod
    def view_inventory(self):
        pass

    @abstractmethod
    def ask_removal_index(self):
        pass