from Interfaces.char_interface import CharInterface

class CharHandler(CharInterface):

    __string = ""

    def set_string(self, string):
        self.__string = string

    def check_char(self):
        self.__alpha_numeric()
        self.__alphabetical()
        self.__digit()
        self.__lowercase()
        self.__uppercase()

    def __alpha_numeric(self):
        print(f"AlphaNumeric: \tTrue") if any(char.isalnum() for char in self.__string) else print(f"AlphaNumeric: \tFalse")

    def __alphabetical(self):
        print(f"Alphabetical: \tTrue") if any(char.isalpha() for char in self.__string) else print(f"Alphabetical: \tFalse")

    def __digit(self):
        print(f"Digit: \t\tTrue") if any(char.isdigit() for char in self.__string) else print(f"Digit: \t\tFalse")

    def __lowercase(self):
        print(f"Lowercase: \tTrue") if any(char.islower() for char in self.__string) else print(f"Lowercase: \tFalse")

    def __uppercase(self):
        print(f"Uppercase: \tTrue") if any(char.isupper() for char in self.__string) else print(f"Uppercase: \tFalse")