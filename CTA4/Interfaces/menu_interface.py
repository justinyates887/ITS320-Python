from abc import ABC, abstractmethod

class MenuInterface(ABC):

    @abstractmethod
    def header():
        pass

    @abstractmethod
    def line_break():
        pass

    @abstractmethod
    def value_table():
        pass

    @abstractmethod
    def interest_table():
        pass

    @abstractmethod
    def footer():
        pass