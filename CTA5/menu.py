from Interfaces.menu_interface import MenuInterface

class Menu(MenuInterface):

    __width = 40
    
    def header(self, text=""):
        print("{:=^{}}".format(text, self.__width))

    def footer(self, text=""):
        print("{:=^{}}".format(text, self.__width))

    def line_break(self):
        print("-" * self.__width)