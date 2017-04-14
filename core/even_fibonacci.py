# TODO :: Refactor
import argparse

N = 'N'


class NotSupportedException(Exception):
    pass


class FibonacciIterator:
    """ FibonacciIterator that calculates and stores calculated
    fibonacci sequence values. N.B. This excludes the 1st 1

        (x) 1, 2, 3, 5, 8, 13, ...
        ( ) 1, 1, 2, 3, 5, 8, 13, ...
    """

    def __init__(self, *args):
        self.sequence = list(args)

    def _calculate_next(self):
        """Calculates and stores the next Fibonacci Sequence"""
        self.sequence.append(self.sequence[-1] + self.sequence[-2])

    def calculate_nth_fibonacci(self, n):
        """Calculates and returns nth fibonacci sequence"""
        if n < 1:
            raise NotSupportedException('')

        # See if that value has been calculated already
        while len(self.sequence) < n:
            self._calculate_next()

        # nth => n-1th in the list [0th of list is 1st Fibonnaci]
        return self.sequence[n - 1]

    def peek(self):
        return self.sequence[-1]

    def back_trace(self):
        return self.sequence[:]

    def set_upper_bound(self, upper_bound):
        if upper_bound < 1:
            raise NotSupportedException('')

        while self.peek() < upper_bound:
            self._calculate_next()

        # Discard any entries that are bigger than the upper bound
        while self.peek() > upper_bound:
            self.sequence.pop(-1)

        # Return the last entry
        return self.peek()


class NFibonacciIterator(FibonacciIterator):
    """Fibonacci Iterator that only contains nth progression

    If N=3, the sequence generated would be:

        3, 13, 55, ...
    => [1], [2], (3), [5], [8], (13), [21], [34], (55)"""

    def __init__(self, N=1, offset=0, fibonacci_iterator=FibonacciIterator(1, 2)):
        FibonacciIterator.__init__(
            self,
            fibonacci_iterator.calculate_nth_fibonacci(N + offset),
            fibonacci_iterator.calculate_nth_fibonacci(N * 2 + offset),
        )
        self.prev = fibonacci_iterator.calculate_nth_fibonacci(N * 2 - 1 + offset)
        self.N = N
        self.offset = offset

    def _calculate_next(self):
        # Create a new iterator with the saved term and the new
        iterator = FibonacciIterator(self.prev, self.sequence[-1])

        # Update the entries and previous
        self.prev = iterator.calculate_nth_fibonacci(self.N * 2 - 1 + self.offset)
        self.sequence.append(iterator.calculate_nth_fibonacci(self.N * 2 + self.offset))


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
        FibonacciIterator.__init__(self, 2, 5)

    def _calculate_next(self):
        self.sequence.append(self.sequence[-1] * 3 - self.sequence[-2])


def configure_parser_and_extract():
    # Configure parser
    parser = argparse.ArgumentParser(description='Finds all the multiples of 3s and 5s below the given number')
    parser.add_argument(N, metavar='M', type=int, nargs='+', help='The number you wish to supply')

    # Parse the argument and extract the number to use in FizzBuzz
    args = parser.parse_args()

    # Return parsed arguments
    return args.N[0]


def run():
    # Configure Parser and extract upper bound we need
    upper_bound = configure_parser_and_extract()

    #
    fib_generator = FibonacciIterator()
    fib_generator.set_upper_bound(upper_bound)
    back_trace = [
        (index, x)
        for index, x in enumerate(fib_generator.back_trace())
        if x % 2 == 0
    ]

    #
    fib_generator = N2FibonacciIterator()
    fib_generator.set_upper_bound(upper_bound)
    back_trace = fib_generator.back_trace()
    answer = sum(back_trace)

    print(back_trace)
    print(answer)


if __name__ == '__main__':
    run()
