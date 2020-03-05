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
        lower_bound = 10 ** (digit - 1)
        upper_bound = 10 ** digit

        lower_index = ceil(self.to_index(lower_bound))
        upper_index = int(self.to_index(upper_bound))

        return [self.to_number(index) for index in range(lower_index, upper_index)]
