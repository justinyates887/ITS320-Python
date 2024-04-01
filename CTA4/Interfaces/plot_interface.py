from abc import ABC, abstractmethod

class PlotInterface(ABC):

    @abstractmethod
    def set_parameters(principle, rate, periods=12, time=5):
        pass

    @abstractmethod
    def visualize():
        pass