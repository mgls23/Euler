class Tree:
    def __init__(self):
        self._structure = []
        with open('../data/p018_tree.txt', 'r') as text_file:
            lines = text_file.readlines()

            for index, line in enumerate(lines, 1):
                numbers = line.split(' ')
                numbers = convert_to_list_of(numbers, int)

                self._structure.append(numbers)

        validate_tree(self._structure)
        print tree_to_string(self._structure)

    def find_path(self):
        while len(self._structure) > 1:
            spam = self._structure.pop(-1)
            spam2 = self._structure.pop(-1)
            new_line = []

            for index in range(len(spam) - 1):
                egg = spam2[index] + max(spam[index], spam[index + 1])
                new_line.append(egg)

            self._structure.append(new_line)

            print
            print tree_to_string(self._structure)

        self._structure.reverse()

        return self._structure[-1][-1]


class Node:
    def __init__(self, **kwargs):
        self._children = []

    def add_child(self, *children):
        self._children += list(children)


def validate_tree(double_array):
    for index, array in enumerate(double_array, 1):
        if len(array) != index:
            raise Exception(double_array)


def tree_to_string(tree, max_digit=None):
    if max_digit is None:
        max_digit = find_max_digit(tree)

    def spam(list, max_digit):
        return (' ' * max_digit).join(
            [str(string).zfill(max_digit) for string in list])

    string_list = []
    index = 0

    for array in reversed(tree):
        string = spam(array, max_digit)
        string = ' ' * index * max_digit + string
        string_list.append(string)
        index += 1

    string_list.reverse()
    string = '\n'.join(string_list)

    return string


def find_max_digit(tree):
    return 4


def convert_to_list_of(input_list, type):
    return [type(element) for element in input_list]


def q18():
    tree = Tree()
    spam = tree.find_path()
    return spam


if __name__ == '__main__':
    print q18()
