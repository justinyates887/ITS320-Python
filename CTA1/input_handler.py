class InputHandler:

    __input_one = 0
    __input_two = 0

    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
    
    def ask(self):
        var = int(input(f"Please enter a number between {self.lower_bound} and {self.upper_bound} \n"))
        self.__set_attributes(var) if self.__validate_input(var) else None

    def get_input_one(self):
        return self.__input_one
    
    def get_input_two(self):
        return self.__input_two
    
    def __validate_input(self, number):
        if int(number) < self.lower_bound or int(number) > self.upper_bound:
            print(f"Error: please stay within the bounds {self.lower_bound} and {self.upper_bound}\n")
            return False
        return True

    def __set_attributes(self, number):
        if self.__input_one == 0:
            self.__input_one = number
        else:
            self.__input_two = number
