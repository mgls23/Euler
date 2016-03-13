import argparse

from fizz_buzz import fizz_buzz

N = 'N'


def find_sum(x):
	# Calculate the result
	multiples = fizz_buzz(x)

	# Find the accumulative
	result = sum(multiples)

	return result


def configure_parser_and_extract():
	# Configure parser
	parser = argparse.ArgumentParser(description='Finds all the multiples of 3s and 5s below the given number')
	parser.add_argument(N, metavar='M', type=int, nargs='+', help='The number you wish to supply')

	# Parse the argument and extract the number to use in FizzBuzz
	args = parser.parse_args()

	# Return parsed arguments
	return args.N[0]


if __name__ == '__main__':
	# Configure Parser and extract upper bound we need
	upper_bound = configure_parser_and_extract()

	# Find the result
	result = find_sum(upper_bound)

	# Output the result
	print result
