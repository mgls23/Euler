import logging
import operator
import pprint
from collections import defaultdict
from functools import reduce
from itertools import combinations
from typing import Iterable, List, Tuple

STARTING_PLAYER_LOSS = 0
STARTING_PLAYER_WIN = 1
UNDETERMINED = 2

WINS = defaultdict(lambda: defaultdict(set))
LOSS = defaultdict(dict)


def base_case(discs: Tuple[int]) -> Tuple[int, str]:
	if len(discs) == 0:
		return STARTING_PLAYER_LOSS, '0 pile rule'

	if len(discs) == 1:
		# IF there is only 1 pile of discs
		# Starting player will only lose if remaining pile is 0
		# Because - starting player can take any number of discs from that leaves 0 discs for the remaining player
		assert discs[0] != 0, 'Discs should be filtered and sorted'
		return STARTING_PLAYER_WIN, '1 pile rule'

	elif len(discs) == 2:
		# IF there are 2 piles of discs
		# Starting player will take away from the larger pile to even out the disc piles
		# When starting player has 2 equal piles of discs, the opponent can mirror the other's move
		# which results in the starting player's move. starting player has now given the opponent this board state
		return discs[0] != discs[1] and STARTING_PLAYER_WIN or STARTING_PLAYER_LOSS, '2 piles rule'

	assert len(discs) == 3
	for disc1, disc2 in combinations(discs, 2):
		if disc1 == disc2:
			return STARTING_PLAYER_WIN, f'Duplicate: {disc1}'

	result, message = check_memoized(*discs)
	if result != UNDETERMINED:
		return result, message

	return UNDETERMINED, ''


def check_memoized(disc1, disc2, disc3) -> Tuple[int, str]:
	if disc1 in LOSS:
		if disc2 in LOSS[disc1]:
			if LOSS[disc1][disc2] == disc3:
				save_loss(disc1, disc2, disc3)
				return STARTING_PLAYER_LOSS, f'Memoized'
			elif LOSS[disc1][disc2] <= disc3:
				return STARTING_PLAYER_WIN, f'{(disc1, disc2, disc3)} -> {(disc1, disc2, LOSS[disc1][disc2])}'

	if disc3 in WINS[disc1][disc2]:
		return STARTING_PLAYER_WIN, f'Memoized'

	return UNDETERMINED, ''


def save_loss(disc1, disc2, disc3):
	if disc2 in LOSS[disc1]:
		assert LOSS[disc1][disc2] == disc3, f'{disc1, disc2, disc3}, {LOSS}'
	else:
		LOSS[disc1][disc2] = disc3


def save_win(disc1, disc2, disc3):
	WINS[disc1][disc2].add(disc3)


def process_disc(raw_discs: Iterable[int]) -> Tuple[int]:
	non_zero_discs = list(filter(lambda entry: entry > 0, raw_discs))
	return tuple(sorted(non_zero_discs))


def print_result(status, indent_count: int, discs, comment: str = ''):
	indent = ' ' * indent_count

	status_shorthand = {
		STARTING_PLAYER_LOSS: 'L',
		STARTING_PLAYER_WIN: 'W',
		UNDETERMINED: 'U',
	}[status]
	lhs = f'{indent}{status_shorthand}: {str(discs).ljust(15)}'.ljust(40)

	print(f'{lhs}{comment}')


def brute_force(raw_discs: Tuple[int], indent_count=0):
	discs = process_disc(raw_discs)

	base_case_result, reason = base_case(discs)
	if base_case_result != UNDETERMINED:
		print_result(base_case_result, indent_count, discs, f'{reason}')
		if base_case_result == STARTING_PLAYER_LOSS:
			save_loss(*discs)

		return base_case_result

	assert len(discs) == 3
	print_result(UNDETERMINED, indent_count, discs)
	for disc_index in reversed(range(len(discs))):
		disc = discs[disc_index]
		for offset in range(1, disc + 1):
			new_discs = list(discs)
			new_discs[disc_index] -= offset
			after_move_state = process_disc(new_discs)

			if brute_force(after_move_state, indent_count + 1) == STARTING_PLAYER_LOSS:
				print_result(STARTING_PLAYER_WIN, indent_count, discs, comment=f'{discs} -> {after_move_state}')
				save_win(*discs)
				return STARTING_PLAYER_WIN

	print_result(STARTING_PLAYER_LOSS, indent_count, discs, comment=f'No more moves left')
	save_loss(*discs)
	return STARTING_PLAYER_LOSS


def xor_solution(board_state: List[int]):
	"""
	1. Convert each of the piles (number of tiles in each pillar) into binary
		e.g. 1, 2, 3
			 1 = 001
			 2 = 010
			 3 = 011

	2. If XOR product of all the numbers (of each digits) is 0, that means there are even number of 1s
		in each digits.

	3. That means the second player can always mirror the starting player's move in any given digit
		in another digit. If this is not true, XOR is not 0 in the first place
	"""
	return reduce(operator.xor, board_state) != 0 and STARTING_PLAYER_WIN or STARTING_PLAYER_LOSS


def insight():
	# n XOR 2n is always 0
	for i in range(1, 100000):
		assert xor_solution([i, i * 2]) == STARTING_PLAYER_WIN

	for i in range(1, 10000):
		result = xor_solution([i * 3])
		if result == STARTING_PLAYER_LOSS:
			print(i)


def _investigation():
	# 0 cannot be a win
	for n in range(1, 19):
		config = (n, n * 2, n * 3)

		print('-' * 50)
		print(f'START: {config}')
		brute_force(config)

	print('-' * 50)
	print('LOSING CASES')
	pprint.pprint(dict(LOSS))


def q301():
	insight()


if __name__ == '__main__':
	import sys
	from euler.util.decorators import timed_function

	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

	assert (timed_function(q301)() == -1)
