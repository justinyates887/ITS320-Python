from Interfaces.input_interface import InputInterface

class InputHandler(InputInterface):

    __list = []

    def __init__(self, menu):
        self.__list = []
        self.menu = menu

    def get_list(self):
        return self.__list

    def ask(self):
        number = input(f"[{len(self.__list) + 1}] Please enter a number: ")
        if(self.__validate_input(number)):
            self.__list.append(float(number))
        else:
            print("Invalid input, please try again.")
            self.ask()

    def ask_list_choice(self):
        self.menu.line_break()
        print("Available principal values:")
        for idx, value in enumerate(self.__list, start=1):
            print(f"{idx}. {value}")

        choice_idx = input("Please enter the index of the principle value you want to choose: ")
        self.menu.line_break()
        return self.__validate_list_choice(choice_idx)

    def show_plot(self, choice):
        return choice.lower() == 'y'

    def run_again(self, choice):
        return choice.lower() == 'y'

    def __validate_input(self, value):
        return value.isdigit()
    
    def __validate_list_choice(self, choice_idx):
        try:
            choice_idx = int(choice_idx)
            if 1 <= choice_idx <= len(self.__list):
                return self.__list[choice_idx - 1]
            else:
                print("Invalid choice. Please enter a valid index.")
                return None
        except ValueError:
            print("Invalid input. Please enter a valid integer index.")
            return None