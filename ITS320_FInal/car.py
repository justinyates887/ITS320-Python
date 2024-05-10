from Interfaces.car_interface import CarInterface

class Car(CarInterface):

    def __init__(self, make, model, color, year, mileage):
        self.__make = make
        self.__model = model
        self.__color = color
        self.__year = year
        self.__mileage = mileage

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_color(self):
        return self.__color

    def get_year(self):
        return self.__year

    def get_mileage(self):
        return self.__mileage

    def update_attributes(self, make, model, color, year, mileage):
        self.__make = make
        self.__model = model
        self.__color = color
        self.__year = year
        self.__mileage = mileage