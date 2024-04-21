from abc import ABC, abstractmethod

class StringInterface(ABC):

    @abstractmethod
    def set_string_list(self, list):
        pass

    @abstractmethod
    def alter_strings(self):
        pass

    @abstractmethod
    def print_altered_list(self):
        pass