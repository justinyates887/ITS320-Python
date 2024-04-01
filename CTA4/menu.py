from Interfaces.menu_interface import MenuInterface

class Menu(MenuInterface):

    __width = 40
    
    def header(self, text=""):
        print("{:=^{}}".format(text, self.__width))

    def footer(self, text=""):
        print("{:=^{}}".format(text, self.__width))

    def line_break(self):
        print("-" * self.__width)

    def value_table(self, values):
        print(f"Total: \t{values['Total']}")
        print(f"Avg: \t{values['Average']}")
        print(f"Min: \t{values['Min']}")
        print(f"Max: \t{values['Max']}")

    def interest_table(self, original_list, interest_list):
        print(f"Value \t Interest After One Period")
        for original_value, interest_value in zip(original_list, interest_list):
            print(f"{original_value} \t {interest_value}")