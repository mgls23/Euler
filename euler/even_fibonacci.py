# TODO :: Refactor
import argparse
from euler.util.fibonacci import FibonacciIterator

N = 'N'


class NFibonacciIterator(FibonacciIterator):
    """Fibonacci Iterator that only contains nth progression

    If n=3, the sequence generated would be:

        3, 13, 55, ...
    => [1], [2], (3), [5], [8], (13), [21], [34], (55)"""

    def __init__(self, every_nth=1, start_index=0, iterator=FibonacciIterator()):
        FibonacciIterator.__init__(self, [
            iterator.calculate_nth(every_nth + start_index),
            iterator.calculate_nth(every_nth * 2 + start_index),
        ])

        self.previous = iterator.calculate_nth(every_nth * 2 - 1 + start_index)
        self.N = every_nth
        self.offset = start_index

    def _calculate_next(self):
        # Create a new iterator with the saved term and the new
        iterator = FibonacciIterator([self.previous, self.sequence[-1]])

        # Update the entries and previous
        self.previous = iterator.calculate_nth(self.N * 2 - 1 + self.offset)
        self.sequence.append(iterator.calculate_nth(self.N * 2 + self.offset))


class N2FibonacciIterator(FibonacciIterator):
    """The nth term is actually the (n-1)th x 3 - (n-2)th

    If we consider :: n1, n2, n3, n4, n5
        n4 = n3 + n2 (Fibonacci Progression)
        n5 = n4 + n3 (Fibonacci Progression)

    We are given n1 and n3. Let's convert n5 into n1 and n3s
        n5 = n4 + n3
        n5 = 2*n3 + n2           # Fibonacci replacement: n4 -> n3 + n2
        n2 = n3 - n1             # Fibonacci reordered:   n3 = n2 + n1

        n5 = 2*n3 + n2 = 3*n3 - n1

    the sequence can be simplified by multiplying the last entry by 3
    and subtracting the one before to obtain n5
    """

    def __init__(self):
        FibonacciIterator.__init__(self, [2, 5])

    def _calculate_next(self):
        self.sequence.append(self.sequence[-1] * 3 - self.sequence[-2])


def configure_parser_and_extract():
    # Configure parser
    parser = argparse.ArgumentParser(
        description='Finds all the multiples of 3s and 5s below the given number'
    )
    parser.add_argument(N, metavar='M', type=int, nargs='+',
        help='The number you wish to supply')

    # Parse the argument and extract the number to use in FizzBuzz
    args = parser.parse_args()

    # Return parsed arguments
    return args.N[0]


def q2():
    upper_bound = 4000000

    #
    fib_generator = FibonacciIterator()
    fib_generator.set_upper_bound(upper_bound)
    even_sequence = [
        (index, x)
        for index, x in enumerate(fib_generator.sequence)
        if x % 2 == 0
    ]

    #
    fib_generator = N2FibonacciIterator()
    fib_generator.set_upper_bound(upper_bound)
    return sum(fib_generator.sequence)


def run():
    # Configure Parser and extract upper bound we need
    upper_bound = configure_parser_and_extract()

    #
    fib_generator = FibonacciIterator()
    fib_generator.set_upper_bound(upper_bound)
    even_sequence = [
        (index, x)
        for index, x in enumerate(fib_generator.sequence)
        if x % 2 == 0
    ]

    #
    fib_generator = N2FibonacciIterator()
    fib_generator.set_upper_bound(upper_bound)
    answer = sum(fib_generator.sequence)

    print(fib_generator.sequence)
    print(answer)


if __name__ == '__main__':
    print(q2())
    run()
