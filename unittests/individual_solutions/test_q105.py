import logging
import sys

from individual_solutions.p105 import check_sum_of_subsets_2


def test_check_sum_of_subsets_2():
	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

	assert not check_sum_of_subsets_2([85, 127, 162, 165, 167, 168, 169, 176, 190])
