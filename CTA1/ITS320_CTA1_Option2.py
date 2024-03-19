# Justin Yates

# Task:
#
# Read two integers and print three lines. The first line should contain 
# integer division, //, the second line should contain float division, /,
# and the third line should contain modulo division, %. You do not need 
# to perform any rounding or formatting operations.

from input_handler import InputHandler
from div import Division

def main():

    #ideally would use interface and injection for non-instantiated members. Will most likely research for next ct

    input_handler = InputHandler(1,100) #bad practice, hard coded values

    for i in range (0,2): #bad practice, hard coded values
        input_handler.ask()

    division_handler = Division(input_handler.get_input_one(), input_handler.get_input_two())

    print("-" * 40)
    division_handler.integer_division()
    division_handler.float_division()
    division_handler.modulus_division()
    print("-" * 40)

if __name__ == "__main__":
    main()