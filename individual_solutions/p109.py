from euler.util.decorators import timed_function
import logging

SINGLE, DOUBLE, TRIPLE = 1, 2, 3
BULLS_EYE = 25


def dart_score_tuple_to_string(tuple_):
	return dart_score_to_string(*tuple_)


def dart_score_to_string(multiplier, score):
	return f"{[-1, 'S', 'D', 'T'][multiplier]}{score}"


def checkout(target_score):
	valid_checkout_paths = set()

	def helper(remaining_score):
		if len(chosen_darts) == 3 or remaining_score <= 0:
			if remaining_score == 0:
				checkout_path = tuple(sorted(chosen_darts[1:])) + (chosen_darts[0],)
				valid_checkout_paths.add(checkout_path)

			return

		for score in list(range(1, 20 + 1)) + [BULLS_EYE]:
			multiplier_range = range(SINGLE, TRIPLE + 1)
			if score == BULLS_EYE: multiplier_range = range(SINGLE, DOUBLE + 1)
			for multiplier in multiplier_range:
				new_score = score * multiplier

				chosen_darts.append((multiplier, score))
				helper(remaining_score - new_score)
				chosen_darts.pop()

	for double_score in list(range(1, 20 + 1)) + [BULLS_EYE]:
		chosen_darts = [(DOUBLE, double_score)]
		helper(target_score - DOUBLE * double_score)

	return valid_checkout_paths


def q109():
	# LESS THAN A HUNDRED!
	all_possible_scores = 0
	for possible_score in range(2, 100):
		result = checkout(possible_score)
		all_possible_scores += len(result)

	return all_possible_scores


if __name__ == '__main__':
	import sys

	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

	assert (timed_function(q109)() == 38182)
