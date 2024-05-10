from Interfaces.dealership_interface import DealershipInterface

class Dealership(DealershipInterface):

    def __init__(self):
        self.inventory = []

    def add_vehicle(self, make, model, color, year, mileage):
        vehicle = {
            "make": make,
            "model": model,
            "color": color,
            "year": year,
            "mileage": mileage
        }
        self.inventory.append(vehicle)

    def remove_vehicle(self, vehicle):
        self.inventory.remove(vehicle)

    def export_inventory_to_text_file(self, filename):
        with open(filename, 'w') as file:
            file.write("Dealership Inventory:\n")
            file.write("Inventory Number | Make          | Model         | Color         | Year | Mileage\n")
            for index, vehicle in enumerate(self.inventory, start=1):
                file.write(f"{index:<16} | {vehicle['make']:<14} | {vehicle['model']:<14} | {vehicle['color']:<14} | {vehicle['year']:<4} | {vehicle['mileage']:<7}\n")
        print("Inventory exported to", filename)
