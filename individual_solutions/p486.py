import logging
from typing import List


# Actually need to extend cards as a List (of ints)
def brute_force(max_cards: int, incomplete_cards: List[int]) -> bool:
	""" Given the state of a particular board, returns whether the next player (B) can win
	given that it is current player (A)'s turn

	Returns
	-------
		True  - A loses, B wins
		False - A wins,  B loses
	"""
	if len(incomplete_cards) == 0:
		return True

	if len(incomplete_cards) == 1:
		# there is only 1 suit remaining, A can just play max_cards, which exhausts B's moves
		# the only scenario in which this cannot happen is if this is already at max_cards
		return incomplete_cards[0] == max_cards

	for index in range(len(incomplete_cards)):
		for possible_move in range(incomplete_cards[index] + 1, max_cards + 1):
			duplicate = incomplete_cards[:]
			duplicate[index] =
			if brute_force(max_cards, duplicate):
				return True

	return False


def simulate():
	for number_of_cards in range(1, 4):
		for number_suits in range(1, 2):
			print()


def q486():
	print(brute_force())
	return -1


if __name__ == '__main__':
	import sys
	from euler.util.decorators import timed_function

	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

	assert (timed_function(q486)() == -1)
