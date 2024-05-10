from abc import ABC, abstractmethod

class DealershipInterface(ABC):
    
    @abstractmethod
    def add_vehicle(self, vehicle):
        pass

    @abstractmethod
    def remove_vehicle(self, vehicle):
        pass

    @abstractmethod
    def export_inventory_to_text_file(self, filename):
        pass