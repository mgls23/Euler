import argparse

from fizz_buzz import fizz_buzz

N = 'N'

if __name__ == '__main__':
    # Configure parser
    parser = argparse.ArgumentParser(description='Finds all the multiples of 3s and 5s below the given number')
    parser.add_argument(N, metavar='M', type=int, nargs='+', help='The number you wish to supply')

    # Parse the argument and extract the number to use in FizzBuzz
    args = parser.parse_args()

    # Calculate the result
    multiples = fizz_buzz(args.N[0])

    # Find the accumulative
    result = sum(multiples)

    # Output the result
    print result
