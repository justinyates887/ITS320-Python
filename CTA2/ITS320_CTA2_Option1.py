# Justin Yates

#Task:

#Write a Python program that performs the following tasks:
#Read from the console an arbitrary string S of length less than 50 characters.
#In the first output line, print True if S has any alphanumeric characters. Otherwise, print False. 
#In the second line, print True if S has any alphabetical characters. Otherwise, print False. 
#In the third line, print True if S has any digits. Otherwise, print False. 
#In the fourth line, print True if S has any lowercase characters. Otherwise, print False. 
#In the fifth line, print True if S has any uppercase characters. Otherwise, print False.
#Develop Python code that implements the program requirements.

from char_handler import CharHandler
from input_handler import InputHandler
from menu import Menu

def main():
    input_handler = InputHandler(50) #max string size 50
    char_handler = CharHandler()
    menu = Menu()

    input_handler.ask()
    char_handler.set_string(input_handler.get_string())

    menu.header("CT2")
    char_handler.check_char()
    menu.footer()

if __name__ == "__main__":
    main()