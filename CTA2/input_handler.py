from Interfaces.input_interface import InputInterface

class InputHandler(InputInterface):

    __max_string = 0
    __string = ""

    def __init__(self, max_string):
        self.__max_string = max_string

    def ask(self):
        var = input(f"Please enter a random string under {self.__max_string} chars: ")
        self.__string = var if self.__validate_input(len(var)) else self.ask()

    def get_string(self):
        return self.__string

    def __validate_input(self, string_length):
        return True if(string_length > 0 and string_length < self.__max_string) else False