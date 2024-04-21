from Interfaces.input_interface import InputInterface

class InputHandler(InputInterface):

    __list = []

    def __init__(self):
        self.__list = []

    def get_list(self):
        return self.__list
    
    def get_list_len(self):
        return len(self.__list)

    def ask(self):
        self.__list.append(input("Please enter a string: "))

    def run_again(self, choice):
        return choice.lower() == 'y'

    def __validate_input(self, value):
        pass
    