from euler.util.decorators import timed_function
import logging

SINGLE, DOUBLE, TRIPLE = 1, 2, 3


def dart_score_tuple_to_string(tuple_):
	return dart_score_to_string(*tuple_)


def dart_score_to_string(multiplier, score):
	return f"{[-1, 'S', 'D', 'T'][multiplier]}{score}"


def checkout(target_score):
	valid_checkout_paths = set()
	chosen_darts = []

	def helper(remaining_score, last_score):
		if len(chosen_darts) == 3 or remaining_score <= 0:
			if chosen_darts[-1][0] == 2 and remaining_score == 0:
				combination = tuple(sorted(chosen_darts[:-1])) + (chosen_darts[-1],)
				valid_checkout_paths.add(tuple(map(dart_score_tuple_to_string, combination)))

			return

		for score in range(SINGLE, 20 + 1):
			for multiplier in range(SINGLE, TRIPLE + 1):
				new_score = score * multiplier
				if new_score < last_score and multiplier != DOUBLE: continue

				chosen_darts.append((multiplier, score))
				helper(remaining_score - new_score, new_score)
				chosen_darts.pop()

	helper(target_score, 0)
	return valid_checkout_paths


def q109():
	# print(checkout(2), len(checkout(2)))
	# print(checkout(4), len(checkout(4)))
	# print(checkout(6), len(checkout(6)))

	all_possible_scores = 0
	for possible_score in range(2, 170):
		all_possible_scores += len(checkout(possible_score))

	return all_possible_scores


if __name__ == '__main__':
	import sys

	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

	assert (timed_function(q109)() == 37820)
