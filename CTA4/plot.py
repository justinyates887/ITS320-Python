import matplotlib.pyplot as plt
from Interfaces.plot_interface import PlotInterface

class Plot(PlotInterface):
    def __init__(self):
        self.principal = None
        self.rate = None
        self.periods = None
        self.time = None

    def set_parameters(self, principal, rate, periods = 12, time = 5):
        self.principal = principal
        self.rate = rate
        self.periods = periods
        self.time = time

    def visualize(self):
        # Calculate compound interest for each year
        years = list(range(1, self.time + 1))
        amounts = [self.principal * (1 + self.rate / self.periods) ** (self.periods * year) for year in years]

        # Create plot
        plt.plot(years, amounts, marker='o', linestyle='-')
        plt.title('Compound Interest Growth Over Time')
        plt.xlabel('Years')
        plt.ylabel('Amount')
        plt.grid(True)
        plt.show()