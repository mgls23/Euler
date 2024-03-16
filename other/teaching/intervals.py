from typing import List

EXAMPLES = [
	([[10, 16], [2, 8], [1, 6], [7, 12]], 2),
	([[1, 2], [3, 4], [5, 6], [7, 8]], 4),
	([[1, 2], [2, 3], [3, 4], [4, 5]], 2),
]

BEG, END = 0, 1


def version_1_sort_beg(intervals: List[List[int]]) -> int:
	intervals.sort(key=lambda pair: pair[BEG])

	count = 1  # to account for the last one
	min_end = intervals[0][END]
	for beg, end in intervals[1:]:
		min_end = min(min_end, end)
		if beg > min_end:
			count += 1
			min_end = end

	return count


def version_2_sort_end(intervals: List[List[int]]) -> int:
	intervals.sort(key=lambda pair: pair[END])

	count = 0
	min_end = -1
	for beg, end in intervals:
		if beg > min_end:
			count += 1
			min_end = end

	return count


def run_version_1():
	for arg, answer in EXAMPLES:
		result = version_1_sort_beg(arg)
		assert result == answer, f'Input: {arg}\nExpected {answer}, got {result}'


def run_version_2():
	for arg, answer in EXAMPLES:
		result = version_2_sort_end(arg)
		assert result == answer, f'Input: {arg}\nExpected {answer}, got {result}'


if __name__ == '__main__':
	run_version_2()
