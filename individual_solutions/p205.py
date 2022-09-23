import logging
import random
from itertools import accumulate

from euler.maths.multiplications import lowest_common_multiple
from euler.util.array import zero_padded


def simple_case_2():
	#    0  1  2  3  4  5  6  7  8
	a = [0, 1, 1, 1, 0, 0, 0, 0, 2]
	b = [0, 0, 0, 0, 1, 1, 1, 1, 1]

	# b=4 [w=3/l=2]
	# b=5 [w=3/l=2]
	# b=6 [w=3/l=2]
	# b=7 [w=3/l=2]
	# b=8 [w=3/d=2]
	# w=15

	aa = list(accumulate(a))
	b_win = 0
	for i in range(1, len(a)):
		b_win += b[i] * aa[i - 1]

	print(b_win / 25)


def simple_case():
	#    0  1  2  3  4  5  6  7  8
	a = [0, 1, 1, 1, 1, 1, 0, 0, 0]
	b = [0, 0, 0, 0, 1, 1, 1, 1, 1]

	aa = list(accumulate(a))
	b_win = 0
	for i in range(1, len(a)):
		b_win += b[i] * aa[i - 1]

	print(b_win / 25)


def simulate_simpler_case():
	a = [1, 2, 3, 4, 5]
	b = [4, 5, 6, 7, 8]
	# b's WR = 3/5 * 5/5 [b=6,7,8,a=*] + 1/5 * 4/5 [b=5,a=1,2,3,4] + 1/5 * 3/5 [b=4,a=1,2,3]
	# (15 + 4 + 3) / 25
	# = 22 / 25
	# 0.88

	b_wins = 0
	simulation = 100000

	for i in range(simulation):
		an, bn = random.choice(a), random.choice(b)
		if bn > an: b_wins += 1

	print(b_wins / simulation)


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

	assert len(nine_4s) == len(six_6s)

	six_6s_cumulate = list(accumulate(six_6s))
	nine_4s_victories = sum(value * six_6s_cumulate[i]
	                        for i, value in enumerate(nine_4s[1:]))

	return round(nine_4s_victories / (sum(nine_4s) * sum(six_6s)), 7)


if __name__ == '__main__':
	import sys
	from euler.util.decorators import timed_function

	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

	assert (timed_function(q205)() == 0.5731441)
