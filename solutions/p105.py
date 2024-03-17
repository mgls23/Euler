import logging
from collections import defaultdict
from itertools import combinations

from solutions.euler.util.io_utils import datafiles

SubsetType = list


def check_subset_sums(original: SubsetType):
	# Generate every subset possible, keep sum by set.
	results = defaultdict(list)
	for sub_len in range(1, len(original) + 1):
		for subset in map(set, combinations(original, sub_len)):
			subset_sum = sum(subset)

			# While I'm tempted to use any here, I'm happier to output the other that caused the trouble
			for other in results[subset_sum]:
				if not (other & subset):
					logging.debug(f'Set {original} is not special, see {other} and {subset}')
					return False

			results[subset_sum].append(subset)

	max_so_far = 0
	for subset_sum in sorted(results):
		subset_lens = list(map(len, results[subset_sum]))
		if min(subset_lens) < max_so_far:
			logging.debug(f'Set {original} failed length check [{max_so_far, subset_sum, results[subset_sum]}]')
			return False

		max_so_far = max(subset_lens)

	logging.debug(f'Set {original} is special')
	return True


# def check_sum_of_subsets(set_a: SubsetType):
# 	set_a.sort()
# 	logging.debug(f'Original Set = {set_a}')
#
# 	# Choose lengths for set B and C
# 	for b_len in range(1, len(set_a) - 1):
# 		for c_len in range(1, len(set_a) - b_len):
#
# 			# Iterate through all combinations (based on lengths)
# 			for set_b in map(set, combinations(set_a, b_len)):
# 				for set_c in map(set, combinations(set_a, c_len)):
#
# 					# Rule: B and C are disjoint - this seems inefficient
# 					# Also, it's highly unlikely that sum of 3+ elements will be same as 1 element
# 					if not set_b.intersection(set_c):
# 						if sum(set_b) == sum(set_c):
# 							logging.debug(f'Set {set_a} is not special, see {set_b}, {set_c}')
# 							return False
#
# 	logging.debug(f'Set {set_a} is special')
# 	return True


def read_sets():
	with open(datafiles('p105_sets.txt')) as file:
		return [SubsetType(map(int, line.replace('\n', '').split(',')))
		        for line in file.readlines()]


def q105():
	return sum(map(sum, filter(check_subset_sums, read_sets())))


if __name__ == '__main__':
	import sys
	from solutions.euler.util.decorators import timed_function

	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
	assert (timed_function(q105)() == 73702)
