import logging
from collections import Counter

from solutions.euler.util.io_utils import datafiles


class Card:
	SUITS = ['C', 'D', 'H', 'S']

	def __init__(self, number: int, suit: str, **kwargs):
		assert number in range(2, 15), f'Invalid number={number}'
		assert suit in self.SUITS, f'Invalid suit={suit}'

		self.number: int = number
		self.suit: str = suit

		self.debug_input = ''
		for k, v in kwargs.items(): setattr(self, k, v)

	@classmethod
	def from_string(cls, string):
		value, suit = string
		number = int({'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14, }.get(value, value))
		return cls(number, suit, debug_input=string)

	def __str__(self):
		return f'{self.suit}{self.number}'

	def debug_validate(self):
		print(f'Original={self.debug_input}, Parsed={self.number}, {self.suit}')


class Player:
	def __init__(self):
		self.hand = None

	def enter_game(self):
		self.hand = Hand()

	def game_result(self):
		assert len(self.hand.cards) == 5
		return self.hand.strongest_rank()


class Hand:
	RANKS = [
		# 'royal_flush', # To compare stronger hands, royal_flush needs not be distinct
		'straight_flush',
		'four_of_a_kind',
		'full_house',
		'flush',
		'straight',
		'three_of_a_kind',
		'two_pairs',
		'one_pair',
		'high_card',
	]

	def __init__(self):
		self.cards: list[Card] = []

	def validate(self):
		assert len(self.cards) == 5

	@staticmethod
	def rank_to_int(rank: str):
		ranks = {rank: len(Hand.RANKS) - i for i, rank in enumerate(Hand.RANKS)}
		return ranks[rank]

	def strongest_rank(self):
		self.validate()

		def attribute(x):
			return lambda obj: getattr(obj, x)

		distinct_numbers = list(map(attribute('number'), self.cards))
		number_by_count = Counter(distinct_numbers)

		# Reversed tuple means, we order by count, then by number
		# This handles any remaining single cards (where we need to order them by value) to handle ties
		numbers, counts = zip(*sorted(number_by_count.items(), reverse=True, key=lambda x: tuple(reversed(x))))

		# if numbers are distinct
		if len(numbers) == 5:
			distinct_suits = list(map(attribute('suit'), self.cards))
			suits_by_count = Counter(distinct_suits)

			is_straight = sorted(numbers) == list(range(min(numbers), min(numbers) + 5))
			is_flush = any(suit_count >= 5 for suit_count in suits_by_count.values())

			if is_straight and is_flush:
				return 'straight_flush', numbers
			if is_flush:
				return 'flush', numbers
			if is_straight:
				return 'straight', numbers

			return 'high_card', numbers

		return {
			# 4 of a kind and full house is higher than straight or flush, but not straightflush
			(4, 1): 'four_of_a_kind',
			(3, 2): 'full_house',
			# Where straight / flush would have been
			(3, 1, 1): 'three_of_a_kind',
			(2, 2, 1): 'two_pairs',
			(2, 1, 1, 1): 'one_pair',
		}[counts], numbers

	def __str__(self):
		cards_str = ', '.join(map(str, self.cards))
		return f"Cards: [{cards_str}] :: outcome = {self.strongest_rank()}"


class PokerGame:
	def __init__(self, number_of_players=2):
		self.players: list[Player] = [Player() for _ in range(number_of_players)]
		self.winner = None

	@classmethod
	def from_string(cls, number_of_players, line):
		cards = line.split(' ')
		assert len(cards) == 10, f'Expected number of cards = 10, line={line}'

		game = PokerGame(number_of_players)
		for player_index in range(number_of_players):
			cards_for_player = map(Card.from_string, (cards[player_index * 5:(player_index + 1) * 5]))
			game.players[player_index].enter_game()
			game.players[player_index].hand.cards.extend(cards_for_player)

		return game

	def determine_winner(self, print_output=True):
		outcomes = [(i, player.game_result()) for i, player in enumerate(self.players, 1)]
		winner, _, = max(outcomes, key=lambda tuple_: (Hand.rank_to_int(tuple_[1][0]), tuple_[1][1]))
		self.winner = winner

		if not print_output:
			return winner

		logging.info(f"-- GAME -- ")
		for player_index, player in enumerate(self.players, 1):
			logging.info(f"Player {player_index}: {player.hand}")
		logging.info(f'Winner: {winner}')
		logging.info('------------')

		return winner


def q54():
	number_of_players = 2
	number_of_times_player_1_wins = 0

	with open(datafiles('p054_poker.txt')) as input_file:
		for line in input_file:
			game = PokerGame.from_string(number_of_players, line.strip('\n'), )
			game.determine_winner()
			number_of_times_player_1_wins += game.winner == 1 and 1 or 0

		return number_of_times_player_1_wins


if __name__ == '__main__':
	print(q54())
