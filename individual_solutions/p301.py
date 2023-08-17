import logging
from functools import lru_cache
from itertools import combinations
from typing import Iterable, List, Tuple

STARTING_PLAYER_LOSS = 0
STARTING_PLAYER_WIN = 1
UNDETERMINED = 2

HARD_CODED_RULES = {
	1: {
		2: 3,
		4: 5,
		6: 7,
		8: 9,
		10: 11,
		12: 13,
	},
	2: {
		4: 6,
		5: 7,
		8: 10,
		9: 11,
	},
	3: {
		4: 7,
		5: 6,
		8: 11,
		9: 10,
	},
}


@lru_cache
def base_case_with_rules(discs: Tuple[int]) -> Tuple[int, str]:
	result, reason = base_case(discs)
	if result == UNDETERMINED:
		disc1, disc2, disc3 = discs
		if disc1 in HARD_CODED_RULES and disc2 in HARD_CODED_RULES[disc1]:
			if HARD_CODED_RULES[disc1][disc2] == disc3:
				return STARTING_PLAYER_LOSS, f'{disc1}{disc2}x rule'
			else:
				return STARTING_PLAYER_WIN, f'{disc1}{disc2}x rule'

	return result, reason


@lru_cache
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
			return STARTING_PLAYER_WIN, f'3 piles, but {disc1} is duplicating'

	return UNDETERMINED, ''


WINS = set()
LOSS = set()


def process_disc(raw_discs: Iterable[int]) -> Tuple[int]:
	non_zero_discs = list(filter(lambda entry: entry > 0, raw_discs))
	return tuple(sorted(non_zero_discs))


@lru_cache
def brute_force(raw_discs: Tuple[int]):
	discs = process_disc(raw_discs)

	base_case_result, reason = base_case_with_rules(discs)
	if base_case_result != UNDETERMINED:
		if base_case_result == STARTING_PLAYER_LOSS:
			# print(f'L: {str(discs).ljust(15)} REASON: {reason}')
			LOSS.add(discs)
		else:
			# print(f'W: {str(discs).ljust(15)} REASON: {reason}')
			WINS.add(discs)
		return base_case_result

	assert len(discs) == 3
	print(f'U: {discs}')
	for index, disc in enumerate(discs):
		for offset in range(1, disc + 1):
			new_discs = list(discs)
			new_discs[index] -= offset
			after_move_state = process_disc(new_discs)
			if brute_force(after_move_state) == STARTING_PLAYER_LOSS:
				# print(f'W: {str(discs).ljust(15)} MOVE: {after_move_state}')
				WINS.add(discs)
				return STARTING_PLAYER_WIN

	# print(f'L: {str(discs).ljust(15)}')
	LOSS.add(discs)
	return STARTING_PLAYER_LOSS


def q301():
	# number = 13
	# for a in range(3, 5):
	# 	for b in range(number):
	# 		for c in range(number):
	# 			brute_force((a, b, c))

	# 0 cannot be a win
	for n in range(1, 5):
		config = (n, n * 2, n * 3)

		print('-' * 50)
		print(f'START: {config}')

		outcome = brute_force(config)

	print('-' * 50)
	print('WINS')
	for win in sorted(WINS):
		print(win)

	print('LOSS')
	for loss in sorted(LOSS):
		print(loss)

	return -1


if __name__ == '__main__':
	import sys
	from euler.util.decorators import timed_function

	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

	assert (timed_function(q301)() == -1)
