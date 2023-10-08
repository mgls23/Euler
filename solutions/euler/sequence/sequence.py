from abc import abstractmethod, ABC
from math import ceil


class SequenceGenerator(ABC):
    @abstractmethod
    def to_number(self, index):
        pass

    @abstractmethod
    def to_index(self, number):
        pass

    def generate_numbers_with(self, digit):
        return self.generate_numbers_in_range(10 ** (digit - 1), 10 ** digit)

    def generate_numbers_in_range(self, number_start, number_end):
        lower_index = ceil(self.to_index(number_start))
        upper_index = int(self.to_index(number_end))

        return [self.to_number(index) for index in range(lower_index, upper_index)]
