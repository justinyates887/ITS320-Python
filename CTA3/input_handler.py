from Interfaces.input_interface import InputInterface

class InputHandler(InputInterface):

    __income = 0

    def get_income(self):
        return self.__income

    def ask(self):
        var = input(f"Please enter your income as a number with no commas: $")

        if self.__validate_input(var):
            self.__income = int(var)
        else:
            print("Invalid input. Please enter a valid number.")
            self.ask()

    def __validate_input(self, value):
        return value.isdigit()