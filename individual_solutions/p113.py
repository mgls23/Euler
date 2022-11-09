import logging


# Actually generate each one
def dynamic_programming_solution(under):
	if under < 100:
		return under

	max_digits = len(str(under))
	non_bouncy = set()

	def generate_increasing_numbers(buffer):
		number = int(''.join(map(str, buffer)))
		if len(buffer) == max_digits:
			if number <= under: non_bouncy.add(number)
			return

		non_bouncy.add(number)

		for number in range(buffer[-1], 10):
			generate_increasing_numbers(buffer + [number])

	def generate_decreasing_numbers(buffer):
		number = int(''.join(map(str, buffer)))
		if len(buffer) == max_digits:
			if number <= under: non_bouncy.add(number)
			return

		non_bouncy.add(number)

		for number in range(buffer[-1], -1, -1):
			generate_decreasing_numbers(buffer + [number])

	for first_digit in range(1, 9 + 1):
		generate_increasing_numbers([first_digit])
		generate_decreasing_numbers([first_digit])

	print(list(sorted(non_bouncy)))


def count_non_bouncy_numbers(up_to_digit):
	# We don't actually need to generate each numbers above
	# We can just multiply out the possibilities based on

	# INCREASING ONLY!
	# 1 -> (1) -> [1-9] 9
	#      (2) -> [2-9] 8
	#      (3) -> [3-9] 7
	#      ...
	#      (9) -> [  9] 1
    #                => n * (n+1) // 2
	# 2 -> (2) -> [2-9] 8
	


	# 1 -> (1) -> (1) -> [1-9] 9
	#             (2) -> [2-9] 8
	#             (3) -> [3-9] 7
	#             ...
	#             (9) -> [  9] 1
	#      (2) -> (2) -> [2-9] 8
	#             (3) -> [3-9] 7
	#             ...
	#             (9) -> [  9] 1
	#      (3) -> [3] -> [3-9] 7
	#             [4] -> [4-9] 6
	#             ...
	#             [9] -> [  9] 1
	#      ...
	#      (9) -> [9] -> [  9] 1


	return -1


def q113():
	count_non_bouncy_numbers(10 ** 6)
	return -1


if __name__ == '__main__':
	import sys
	from euler.util.decorators import timed_function

	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

	assert (timed_function(q113)() == -1)
