from Interfaces.string_interface import StringInterface

class StringHandler(StringInterface):

    __string_list = []
    __altered_list = []

    def __init__(self, menu):
        self.__string_list = []
        self.__altered_list = []
        self.menu = menu

    def set_string_list(self, string_list):
        self.__string_list = string_list

    def alter_strings(self):
        return self.__alter_strings()
    
    def print_altered_list(self):
        if self.__validate_altered_list():
            self.menu.line_break()
            concatenated_string = self.__altered_list[0]
            reversed_string = self.__altered_list[1]
            print("| {:<13} | {:<9} |".format("Concatenated", "Reversed"))
            print("| {:<13} | {:<9} |".format(concatenated_string, reversed_string))
        else:
            print("Error: Insufficient strings provided.")
    
    def __validate_altered_list(self):
        return len(self.__altered_list) == 2
    
    def __alter_strings(self):
        concatenated_strings = self.__string_list[0] + self.__string_list[1]
        reversed_string = self.__string_list[2][::-1]
        self.__altered_list = [concatenated_strings, reversed_string]
        return self.__altered_list