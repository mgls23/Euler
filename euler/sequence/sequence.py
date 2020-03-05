from abc import abstractmethod, ABC
from math import ceil


class Sequence(ABC):
    @staticmethod
    @abstractmethod
    def to_number(index):
        pass

    @staticmethod
    @abstractmethod
    def to_index(number):
        pass

    @classmethod
    def generate_numbers_with(cls, digit):
        lower_bound = 10 ** (digit - 1)
        upper_bound = 10 ** digit

        lower_index = ceil(cls.to_index(lower_bound))
        upper_index = int(cls.to_index(upper_bound))

        return list(map(cls.to_number, range(lower_index, upper_index)))
