class Division:

    __input_one = 0
    __input_two = 0

    def __init__(self, input_one, input_two):
        self.__input_one = input_one
        self.__input_two = input_two

    def integer_division(self):
        if self.__validate_zero_division():
            print(f"Integer: \t{self.__input_one // self.__input_two}")

    def float_division(self):
        if self.__validate_zero_division():
            print(f"Float: \t{self.__input_one / self.__input_two}")

    def modulus_division(self):
        if self.__validate_zero_division():
            print(f"Modulus: \t{self.__input_one % self.__input_two}")

    def __validate_zero_division(self):
        if self.__input_two == 0:
            print("Error: Division by zero is not allowed.")
            return False
        return True