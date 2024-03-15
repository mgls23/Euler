import unittest
from unittest.mock import Mock

from solutions.p54 import Card, Hand, PokerGame, q54


class TestCard(unittest.TestCase):
	def test_card_init(self):
		# Test valid inputs
		card1 = Card(2, 'C')
		assert card1.number == 2 and card1.suit == 'C'

		card2 = Card(14, 'S')
		assert card2.number == 14 and card2.suit == 'S'

	def test_invalid_card_init(self):
		with self.assertRaises(AssertionError):
			Card(1, 'H')  # Number less than 2

		with self.assertRaises(AssertionError):
			Card(15, 'D')  # Number greater than 14

		with self.assertRaises(AssertionError):
			Card(10, 'X')  # Invalid suit

	def test_hand_rank(self):
		hand = Hand()
		hand.cards = [
			Card(2, 'H'),
			Card(3, 'H'),
			Card(4, 'H'),
			Card(5, 'H'),
			Card(6, 'H')
		]
		self.assertEqual(hand.strongest_rank(), ('straight_flush', (6, 5, 4, 3, 2)))

		hand.cards = [
			Card(2, 'H'),
			Card(2, 'D'),
			Card(2, 'S'),
			Card(2, 'C'),
			Card(6, 'H')
		]
		self.assertEqual(hand.strongest_rank(), ('four_of_a_kind', (2, 6)))

		hand.cards = [
			Card(2, 'H'),
			Card(2, 'D'),
			Card(3, 'H'),
			Card(3, 'D'),
			Card(3, 'S')
		]
		self.assertEqual(hand.strongest_rank(), ('full_house', (3, 2)))

		hand.cards = [
			Card(2, 'H'),
			Card(4, 'H'),
			Card(6, 'H'),
			Card(8, 'H'),
			Card(10, 'H')
		]
		self.assertEqual(hand.strongest_rank(), ('flush', (10, 8, 6, 4, 2)))

		hand.cards = [
			Card(2, 'H'),
			Card(3, 'D'),
			Card(4, 'H'),
			Card(5, 'D'),
			Card(6, 'S')
		]
		self.assertEqual(hand.strongest_rank(), ('straight', (6, 5, 4, 3, 2)))

		hand.cards = [
			Card(2, 'H'),
			Card(2, 'D'),
			Card(2, 'S'),
			Card(5, 'H'),
			Card(6, 'H')
		]
		self.assertEqual(hand.strongest_rank(), ('three_of_a_kind', (2, 6, 5)))

		hand.cards = [
			Card(2, 'H'),
			Card(2, 'D'),
			Card(3, 'H'),
			Card(3, 'D'),
			Card(6, 'S')
		]
		self.assertEqual(hand.strongest_rank(), ('two_pairs', (3, 2, 6)))

		hand.cards = [
			Card(2, 'H'),
			Card(2, 'D'),
			Card(3, 'H'),
			Card(4, 'D'),
			Card(6, 'S')
		]
		self.assertEqual(hand.strongest_rank(), ('one_pair', (2, 6, 4, 3)))

		hand.cards = [
			Card(2, 'H'),
			Card(4, 'D'),
			Card(6, 'H'),
			Card(8, 'D'),
			Card(10, 'S')
		]
		self.assertEqual(hand.strongest_rank(), ('high_card', (10, 8, 6, 4, 2)))


class TestGame(unittest.TestCase):

	def test_determine_winner(self):
		game = PokerGame(number_of_players=2)

		high_numbers = (10, 9, 8, 7, 6)
		low_numbers = (5,)

		for i, stronger_rank in enumerate(Hand.RANKS):
			for weaker_rank in Hand.RANKS[i + 1:]:
				game.players[0].game_result = Mock(return_value=(stronger_rank, low_numbers))
				game.players[1].game_result = Mock(return_value=(weaker_rank, high_numbers))
				self.assertEqual(game.determine_winner(print_output=False), 1,
				                 msg=f'{stronger_rank} should always beat {weaker_rank}')

				game.players[0].game_result = Mock(return_value=(weaker_rank, high_numbers))
				game.players[1].game_result = Mock(return_value=(stronger_rank, low_numbers))
				self.assertEqual(game.determine_winner(print_output=False), 2,
				                 msg=f'{stronger_rank} should always beat {weaker_rank}')

		for rank in Hand.RANKS:
			hi_numbers = (10, 9, 8, 7, 6)
			low_numbers = (5, 4, 3, 2, 1)

			game.players[0].game_result = Mock(return_value=(rank, hi_numbers))
			game.players[1].game_result = Mock(return_value=(rank, low_numbers))
			self.assertEqual(game.determine_winner(print_output=False), 1)

			game.players[0].game_result = Mock(return_value=(rank, low_numbers))
			game.players[1].game_result = Mock(return_value=(rank, hi_numbers))
			self.assertEqual(game.determine_winner(print_output=False), 2)


def test_q54():
	assert q54() == 376


if __name__ == '__main__':
	unittest.main()
