# Justin Yates

import sys
from dependency_injector import containers, providers
from input_handler import InputHandler
from car import Car
from dealership import Dealership
from menu import Menu

class Container(containers.DeclarativeContainer):

    menu = providers.Singleton(Menu)
    car = providers.Singleton(Car, make="default_make", model="default_model", color="default_color", year=0, mileage=0)
    dealership = providers.Singleton(Dealership)
    input_handler = providers.Singleton(InputHandler, car=car, dealership=dealership, menu=menu)

def main():

    container = Container()
    container.wire(modules=[sys.modules[__name__]])

    input_handler = container.input_handler()
    menu = container.menu()
    car = container.car()
    dealership = container.dealership()

    menu.header("CTA 5")

    while True:
        print(f"\nMenu:")
        print("1. Add vehicle")
        print("2. Remove vehicle")
        print("3. View Vehicles")
        print("4. Export to text file")
        print("0. End program")

        choice = input("Enter your choice: ")

        if choice == '1':
            input_handler.ask()
        elif choice == '2':
            input_handler.ask_removal_index()
        elif choice == '3':
            input_handler.view_inventory()
        elif choice == '4':
            dealership.export_inventory_to_text_file("inventory.txt")
        elif choice == '0':
            print("Ending program...")
            break
        else:
            print("Invalid choice. Please try again.")

    menu.footer("Justin Yates")

if __name__ == "__main__":
    main()