import operator
from typing import List


def trap(self, heights):
	max_rights, max_right = [], 0
	for height in reversed(heights):
		max_right = max(max_right, height)
		max_rights.append(max_right)

	max_left, trapped_water = 0, 0
	for index, height in enumerate(heights):
		max_left = max(max_left, height)
		trapped_water += min(max_rights[index], max_left) - height

	return trapped_water


def trapping_water(self, heights: List[int]):
	max_height_index, max_height = max(enumerate(heights), key=operator.itemgetter(1))

	def trapped_water(given_heights):
		total, local_max = 0, 0
		for height in given_heights:
			local_max = max(local_max, height)
			total += local_max - height

		return total

	return trapped_water(heights[:max_height_index]) + trapped_water(heights[:max_height_index:-1])
