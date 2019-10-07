from enum import Enum
from itertools import groupby


class ShorthandEnum(Enum):
    @classmethod
    def match_by_value(cls, value):
        for enum_entry in cls:
            if enum_entry.value == value:
                return enum_entry

        raise Exception(f'No match for {value} in class={cls} found')

    @classmethod
    def match_by_first_name(cls, string_):
        matches = []
        for enum_entry in cls:
            if enum_entry.name[0] == string_:
                matches.append(enum_entry)

        return matches[-1]


class HandValue(ShorthandEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

    @classmethod
    def from_string(cls, string_):
        try:
            return cls.match_by_value(int(string_))
        except ValueError as e:
            return cls.match_by_first_name(string_)

    def numerical_value(self):
        return self.value


class Suit(ShorthandEnum):
    DIAMOND = 1
    HEART = 2
    SPADES = 3
    CLOVES = 4


class Card:
    def __init__(self, value, suit, **kwargs):
        self.value = value
        self.suit = suit

        for k, v in kwargs.items(): setattr(self, k, v)

    @classmethod
    def from_string(cls, string_):
        hand_value = HandValue.from_string(string_[0])
        suit = Suit.match_by_first_name(string_[1])
        return cls(hand_value, suit, debug_input=string_)

    def __str__(self):
        return f'Value={self.value}, Suit={self.suit}'

    def debug_validate(self):
        print(f'Original={self.debug_input}, Parsed={self.value}, {self.suit}')


class Hand:
    def __init__(self):
        self.cards = []

    def add_card_from_string(self, string_):
        created_card = Card.from_string(string_)
        self.cards.append(created_card)

    def validate(self):
        assert (len(self.cards) == 5)
        for card in self.cards: card.debug_validate()

    def solve(self):
        self.cards.sort(key=HandValue.numerical_value)
        groups = groupby(self.cards, key=HandValue.numerical_value)

        is_straight = True
        first = self.cards[0].numerical_value()
        for offset, card in enumerate(self.cards[1:], 1):
            is_straight = is_straight and card.numerical_value() + offset == first


class PokerGame:
    def __init__(self):
        self.player1_hand = Hand()
        self.player2_hand = Hand()
        self.winner = None

    @classmethod
    def from_string(cls, line):
        cards = line.split(' ')
        assert len(cards) == 10, f'Expected number of cards = 10, line={line}'

        game = PokerGame()
        for i in range(5):
            game.player1_hand.add_card_from_string(cards[i])

        for i in range(5, 10):
            game.player2_hand.add_card_from_string(cards[i])

        game.player1_hand.validate()
        game.player2_hand.validate()

        return game

    def solve(self, show_workings=False):
        self.winner = 1
        self.winner = 2

    def has_player_1_won(self):
        return self.winner == 1


def q54():
    number_of_times_player_1_wins = 0

    with open('../data/p054_poker.txt') as input_file:
        for line in input_file:
            game = PokerGame.from_string(line.strip('\n'))
            game.solve(show_workings=True)
            number_of_times_player_1_wins += game.has_player_1_won() and 1 or 0


q54()
