import logging

from euler.maths.multiplications import lowest_common_multiple
from euler.util.array import zero_padded


def lexicographical_ordering(number_of_dice, dice_max, dice_min=1):
	dice_range = dice_max - dice_min + 1
	scenarios = [0] * ((number_of_dice * dice_range) + 1)
	dice = zero_padded([1] * number_of_dice)

	while True:
		# logging.debug((scenarios, dice))
		scenarios[sum(dice)] += 1

		j = 1
		dice[j] += 1

		while dice[j] > dice_max:
			dice[j] = dice_min
			j += 1
			if j == len(dice):
				logging.debug((scenarios, dice))
				return scenarios

			dice[j] += 1


def graphic_6_6s():
	return lexicographical_ordering(number_of_dice=6, dice_max=6)


def graphic_9_4s():
	return lexicographical_ordering(number_of_dice=9, dice_max=4)


def nine_of_4():
	# min = 9, max = 36
	scenarios = [0] * 37

	# 7x(1) (1) [1-4]
	for index in range(7 + 1 + 1, 7 + 1 + 4 + 1):
		scenarios[index] += 1

	# 7x(1) (2) [1-4]
	for index in range(7 + 2, 7 + 2 + 4 + 1):
		scenarios[index] += 1

	# 7x(1)(3) [1-4]
	for index in range(7 + 3, 7 + 3 + 4 + 1):
		scenarios[index] += 1

	# 7x(1)(4) [1-4]
	for index in range(7 + 4, 7 + 4 + 4 + 1):
		scenarios[index] += 1


# 6x(1)(2)(1)[1-4]
# 6 + 2 + 1


def q205():
	nine_4s, six_6s = graphic_9_4s(), graphic_6_6s()
	sum4s, sum6s = sum(nine_4s), sum(six_6s)

	assert len(nine_4s) == len(six_6s)

	lcm = lowest_common_multiple(sum4s, sum6s)
	adjust_4, adjust_6 = lcm / sum4s, lcm / sum6s

	nine_4s_adjusted = list(map(lambda count: count * adjust_4, nine_4s))
	six_6s_adjusted = list(map(lambda count: count * adjust_6, six_6s))

	victory = sum(max(count - six_6s_adjusted[i], 0)
	              for i, count in enumerate(nine_4s_adjusted))

	return victory / lcm


if __name__ == '__main__':
	import sys
	from euler.util.decorators import timed_function

	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

	assert (timed_function(q205)() == -1)
