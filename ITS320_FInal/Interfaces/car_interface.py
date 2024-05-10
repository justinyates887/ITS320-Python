from abc import ABC, abstractmethod

class CarInterface(ABC):

    @abstractmethod
    def get_make(self):
        pass

    @abstractmethod
    def get_model(self):
        pass

    @abstractmethod
    def get_color(self):
        pass

    @abstractmethod
    def get_year(self):
        pass

    @abstractmethod
    def get_mileage(self):
        pass

    @abstractmethod
    def update_attributes(self, make, model, color, year, mileage):
        pass