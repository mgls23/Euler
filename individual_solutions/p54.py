from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from enum import IntEnum
from typing import List

from euler.util.decorators import timed_function
from euler.util.io import datafiles


class Type(IntEnum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8
    ROYAL_FLUSH = 9


@dataclass
class Hand:
    type: Type
    numbers: List[int]

    def can_own_that_geezer(self, other: Hand):
        type_number, other_type_number = int(self.type), int(other.type)
        if type_number != other_type_number: return type_number > other_type_number

        assert len(self.numbers) == len(other.numbers), "Same type of hand should have same length of numbers"

        for index, number in enumerate(self.numbers):
            if number != other.numbers[index]:
                return number > other.numbers[index]


def string_to_hand(string: List[str]) -> Hand:
    numbers, suits = Counter(), Counter()
    for number, suit in string:
        numbers[number] += 1
        suits[suit] += 1

    NUMBER, COUNT = 0, 1
    numbers_by_frequency = numbers.most_common(5)
    most_common_number_count = numbers_by_frequency[0][COUNT]
    numbers_only = [number for number, frequency in numbers_by_frequency]

    most_common_suit, most_common_suit_count = suits.most_common(4)

    # HIGH_CARD, STRAIGHT, FLUSH, STRAIGHT_FLUSH, ROYAL_STRAIGHT_FLUSH
    # NOTE: straight and flush cannot happen when there are duplicate numbers
    if most_common_number_count == 1:
        is_flush = most_common_suit_count == 5
        is_straight = sorted(numbers.values())

        if is_flush and is_straight:
            return Hand(type=Type.ROYAL_FLUSH, numbers=[])

            if


        return Hand()

    elif most_common_number_count == 2:
        # PAIR, TWO_PAIR
        if numbers_by_frequency[1][COUNT] == 1:
            return Hand(type=Type.ONE_PAIR, numbers=numbers_only)
        else:
            return Hand(type=Type.TWO_PAIR, numbers=list(sorted(numbers_only[:2])) + numbers_only[2:])

    # TRIPLE, FULL_HOUSE
    elif most_common_number_count == 3:
        if numbers_by_frequency[1][COUNT] == 1:
            return Hand(type=Type.THREE_OF_A_KIND, numbers=numbers_only[0] + list(sorted(numbers_only[1:])))
        else:
            return Hand(type=Type.FULL_HOUSE, numbers=numbers_only)

    # FOUR_OF_A_KIND
    elif most_common_number_count == 4:
        return Hand(type=Type.FOUR_OF_A_KIND, numbers=numbers_only)
    else:
        assert False, "Should not happen"


def read_hands():
    win_count = 0
    with open(datafiles('p054_poker.txt')) as file:
        games = file.readlines()
        for game in games:
            cards = game.split(' ')
            logging.debug(f'Hand={cards}')

            player_1_hand, player_2_hand = string_to_hand(cards[:5]), string_to_hand(cards[5:])
            if player_1_hand.can_own_that_geezer(player_2_hand):
                win_count += 1

    return win_count


def q54():
    return -1


if __name__ == '__main__':
    import logging
    import sys

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    # assert (timed_function(get_sum_of_hundred_decimal_digits)(2) == 475)
    assert (timed_function(q54)() == -1)
