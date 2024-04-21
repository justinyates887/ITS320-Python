# Justin Yates

#Write a Python function that will work on three strings. 
#The function will return a concatenation of the first two strings and will print the third string in reverse order. 
#The function is to be called from the main program.
#In the main program, prompt the user for the three strings and pass these values to the function.

import sys
from dependency_injector import containers, providers
from input_handler import InputHandler
from menu import Menu
from string_handler import StringHandler

class Container(containers.DeclarativeContainer):

    menu = providers.Singleton(Menu)
    input_handler = providers.Singleton(InputHandler)
    string_handler = providers.Singleton(StringHandler, menu=menu)

def main():

    container = Container()
    container.wire(modules=[sys.modules[__name__]])

    input_handler = container.input_handler()
    menu = container.menu()
    string_handler = container.string_handler()

    menu.header("CTA 5")

    while (input_handler.get_list_len() < 3):
        input_handler.ask()

    string_handler.set_string_list(input_handler.get_list())
    string_handler.alter_strings()
    string_handler.print_altered_list()

    menu.footer("Justin Yates")
    main() if input_handler.run_again(input("Would you like to start over? (Y/N): ")) else None

if __name__ == "__main__":
    main()