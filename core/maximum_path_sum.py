class Tree:
    def __init__(self, file_path):
        self.rows = []
        with open(file_path, 'r') as text_file:
            for line in text_file.readlines():
                numbers_string = line.split(' ')
                numbers = [int(element) for element in numbers_string]

                self.rows.append(numbers)

        self.validate_tree()

    def find_maximum_path_sum(self):
        maximums = self.rows[-1]
        for row in reversed(self.rows[:-1]):
            for index, cost in enumerate(row):
                maximums[index] = cost + max(maximums[index],
                                             maximums[index + 1])

        return maximums[0]

    def validate_tree(self):
        for index, array in enumerate(self.rows, 1):
            if len(array) != index:
                raise Exception(self.rows)

    @staticmethod
    def find_max_digit():
        # TODO (P5) :: Make this detect from self.rows
        return 4

    def __str__(self):
        max_digit = self.find_max_digit()
        maximum_length = len(self.rows[-1]) * max_digit * 2

        rows_string = [
            pad_numbers(array, max_digit).center(maximum_length)
            for index, array in enumerate(self.rows)
        ]

        return '\n'.join(rows_string)


def pad_numbers(list_, max_digit):
    return (' ' * max_digit).join([str(element).zfill(max_digit) for element in list_])


DATA_LOCATION = 'data/'


def q18():
    tree = Tree(DATA_LOCATION + 'p018_tree.txt')
    maximum_path_sum = tree.find_maximum_path_sum()
    return maximum_path_sum


def q67():
    tree = Tree(DATA_LOCATION + 'p067_triangle.txt')
    maximum_path_sum = tree.find_maximum_path_sum()
    return maximum_path_sum


if __name__ == '__main__':
    DATA_LOCATION = '../data/'

    print q18()  # 1074
    print q67()  # 7273
