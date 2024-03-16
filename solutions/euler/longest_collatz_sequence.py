import math

# If the number is a power of 2, we know how this would be
collatz_sequence = {int(math.pow(2, index - 1)): index for index in range(1, 1000)}


def collatz_length(number):
	assert number > 0, ""

	count = 0
	sequence = []

	while number not in collatz_sequence:
		sequence.append(number)

		if number == 1: break

		# Next Collatz Sequence
		number = int(number / 2) if number % 2 == 0 else 3 * number + 1
		count += 1

	sequence_length = collatz_sequence[number] + count

	for index, starting_number in enumerate(sequence[1:], 1):
		collatz_sequence[starting_number] = sequence_length - index

	return sequence_length
