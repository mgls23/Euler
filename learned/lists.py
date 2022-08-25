# https://stackoverflow.com/questions/14836228/is-there-a-standardized-method-to-swap-two-variables-in-python
from typing import List


def list_swap(numbers: List[int]):
    # Swapping the 2 variables are commonly done in the format
    # x, y = y, x
    # However, this will result in erraneous behaviour
    numbers[0], numbers[numbers[0]] = numbers[numbers[0]], numbers[0]
