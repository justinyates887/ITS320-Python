# Justin Yates

#Create a program that will calculate the weekly average tax withholding for a customer, given the following weekly income guidelines:

#Income less than $500: tax rate 10%
#Incomes greater than/equal to $500 and less than $1500: tax rate 15%
#Incomes greater than/equal to $1500 and less than $2500: tax rate 20%
#Incomes greater than/equal to $2500: tax rate 30%
#Store the income brackets and rates in a dictionary.
#Write a statement that prompts the user for an income and then looks up the tax rate from the dictionary and 
#   prints the income, tax rate, and tax.

import sys
from dependency_injector import containers, providers
from input_handler import InputHandler
from tax_bracket import TaxBracket

class Container(containers.DeclarativeContainer):

    #Reference: https://dev.to/sxddhxrthx/introduction-to-dependency-injection-in-python-35c
    input_handler = providers.Singleton(InputHandler)
    tax_bracket = providers.Singleton(TaxBracket)

def main():
    container = Container()
    container.wire(modules=[sys.modules[__name__]])

    input_handler = container.input_handler()
    tax_bracket = container.tax_bracket()

    input_handler.ask()
    tax_rate = tax_bracket.get_effective_tax_rate(input_handler.get_income())

    print("=" * 40)
    print(f"Income: \t${input_handler.get_income()}")
    print(f"Tax Rate: \t{tax_rate * 100}%")
    print(f"Tax: \t\t${round(input_handler.get_income() * tax_rate, 2)}")
    print("=" * 40)

if __name__ == "__main__":
    main()