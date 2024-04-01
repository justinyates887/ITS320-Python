#Justin Yates

#Write a program that utilizes a loop to read a set of five floating-point values from user input.
#Ask the user to enter the values, then print the following data:

#Total
#Average
#Maximum
#Minimum
#Interest at 20% for each original value entered by the user.
#Use the formula: Interest_Value = Original_value + Original_value*0.2

import sys
from dependency_injector import containers, providers
from input_handler import InputHandler
from menu import Menu
from stats import Stats
from plot import Plot

class Container(containers.DeclarativeContainer):

    menu = providers.Singleton(Menu)
    input_handler = providers.Singleton(InputHandler, menu=menu)
    stats = providers.Singleton(Stats)
    plot = providers.Singleton(Plot)

def main():
    container = Container()
    container.wire(modules=[sys.modules[__name__]])

    input_handler = container.input_handler()
    stats = container.stats()
    menu = container.menu()
    plot = container.plot()

    menu.header("CTA 4")

    while(len(input_handler.get_list()) < 5):
        input_handler.ask()

    stats.set_list(input_handler.get_list())
    stats.get_stats(0.2)

    menu.line_break()
    menu.value_table(stats.get_object())
    menu.line_break()
    menu.interest_table(input_handler.get_list(), stats.get_object()['Interest'])
    menu.line_break()

    if input_handler.show_plot(input("Would you like to visualize compund interest over 5 years? (Y/N): ")):
        plot.set_parameters(input_handler.ask_list_choice(), 0.2)
        plot.visualize()

    menu.footer("Justin Yates")
    main() if input_handler.run_again(input("Would you like to start over? (Y/N): ")) else None

if __name__ == "__main__":
    main()