from Interfaces.menu_interface import MenuInterface

class Menu(MenuInterface):
    
    def header(self, title):
        print("=" * 15 + title + "=" * 15)
        print("-" * (len(title) + 30))

    def footer(self):
        print("=" * 40)