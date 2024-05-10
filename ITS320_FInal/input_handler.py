from Interfaces.input_interface import InputInterface

class InputHandler(InputInterface):

    def __init__(self, car, dealership, menu):
        self.__list = []
        self.car = car
        self.dealership = dealership
        self.menu = menu

    def get_list(self):
        return self.__list
    
    def get_list_len(self):
        return len(self.__list)

    def ask(self):
        self.__create_car_instance()

    def view_inventory(self):
        print("Dealership Inventory:")
        print(f"{'Inventory Number':<18} | {'Make':<14} | {'Model':<14} | {'Color':<14} | {'Year':<7} | {'Mileage':<7}")
        self.menu.line_break()
        for index, vehicle in enumerate(self.dealership.inventory):
            print(f"{index + 1:<18} | {vehicle['make']:<14} | {vehicle['model']:<14} | {vehicle['color']:<14} | {vehicle['year']:<7} | {vehicle['mileage']:<7}")

    def ask_removal_index(self):
        self.view_inventory()
        choice = input("Which vehicle number would you like to remove? ")
        if choice.isdigit():
            self.dealership.remove_vehicle(self.dealership.inventory[int(choice) -1])

    def run_again(self, choice):
        return choice.lower() == 'y'

    def __get_car_details(self):
        make = input("Enter the make of the car: ")
        model = input("Enter the model of the car: ")
        color = input("Enter the color of the car: ")
        year = input("Enter the year of the car: ")
        mileage = input("Enter the mileage of the car: ")

        if not year.isdigit() or not mileage.isdigit():
            print("Year and mileage must be numeric.")
            return self.ask()

        year = int(year)
        mileage = int(mileage)

        self.car.update_attributes(make, model, color, year, mileage)
        return make, model, color, year, mileage
    
    def __create_car_instance(self):
        details = self.__get_car_details()
        if details:
            make, model, color, year, mileage = details
            self.dealership.add_vehicle(make, model, color, year, mileage)
        else:
            return None