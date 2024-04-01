from Interfaces.stats_interface import StatsInterface

class Stats(StatsInterface):
    
    __list = []
    __object = {}

    def __init__(self):
        self.__list = []
        self.__object = {}

    def set_list(self, list):
        self.__list = list

    def get_object(self):
        return self.__object

    def get_stats(self, interest_rate):
        self.__object['Total'] = self.__total()
        self.__object['Average'] = self.__average()
        self.__object['Max'] = self.__max()
        self.__object['Min'] = self.__min()
        self.__object['Interest'] = self.__interest(interest_rate)

    def __total(self):
        return sum(self.__list)

    def __average(self):
        return self.__total() / len(self.__list)

    def __max(self):
        return max(self.__list)

    def __min(self):
        return min(self.__list)
    
    def __interest(self, rate):
        return [value + value * rate for value in self.__list]