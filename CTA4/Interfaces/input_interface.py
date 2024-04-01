from abc import ABC, abstractmethod

class InputInterface(ABC):

    @abstractmethod
    def get_list(self):
        pass
    
    @abstractmethod
    def ask(self):
        pass

    @abstractmethod
    def ask_list_choice(self):
        pass

    @abstractmethod
    def show_plot(self):
        pass

    @abstractmethod
    def run_again(self):
        pass