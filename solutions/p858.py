from itertools import combinations, groupby
from math import lcm
from operator import itemgetter


def list_string_to_string(string):
	for character in ['[', ']', "'", ',']:
		string = string.replace(character, ' ' * len(character))

	return string


def show_pattern_print(all_possible_subsets):
	for length, subsets in enumerate(all_possible_subsets):
		print(f"Subset of length {length}: {subsets}")

		if length < 3:
			lcms = [str(lcm(*subset)).center(len(str(subset)) - 2) for subset in subsets]
			print(f"{' ' * (len('Subset of length X: '))}{lcms}")
			continue

		groups = [list(groups_) for _, groups_ in groupby(subsets, key=lambda tuple_: tuple_[:-1])]
		max_length = len(str(groups[0]))
		for group in groups:
			lcms = [str(lcm(*subset)).center(len(str(subset)) - 2) for subset in group]

			print(list_string_to_string(str(group).rjust(max_length)))
			print(list_string_to_string(str(lcms).rjust(max_length)))


def brute_force_G(N):
	""" To understand the problem (and the behaviour of G(N) better
	we first implement the brute force version of G
	"""
	one_to_N = list(range(1, N + 1))

	all_possible_subsets = [
		[subset for subset in combinations(one_to_N, subset_size)]
		for subset_size in range(len(one_to_N) + 1)
	]
	print(all_possible_subsets)
	print()

	subsets_lcm = [[lcm(*subset) for subset in subsets] for subsets in all_possible_subsets]
	True and show_pattern_print(all_possible_subsets) or print(subsets_lcm)
	print()

	print(list(map(sorted, subsets_lcm)))
	print()

	sums_lcm = list(map(sum, subsets_lcm))
	print(sums_lcm)
	print()

	return sum(sums_lcm)


if __name__ == '__main__':
	print(brute_force_G(7))
