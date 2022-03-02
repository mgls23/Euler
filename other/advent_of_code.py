def q1_sample():
    return [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def parse_input():
    with open('input_01.txt') as input_file:
        raw_input = input_file.readlines()  # brings everything into memory
        return [int(line.rstrip()) for line in raw_input]


def count_increased(list_):
    differences = [one_after - before for before, one_after in zip(list_, list_[1:])]
    return len(list(filter(lambda difference: difference > 0, differences)))


def q1_1():
    original_input = parse_input()
    return count_increased(original_input)


def q1_2():
    original_input = parse_input()
    window_size = 3
    sliding_window = [sum(original_input[i:i + window_size])
                      for i in range(len(original_input) - (window_size - 1))]
    return count_increased(sliding_window)


def parse_input2():
    with open('input_02.txt') as input_file:
        raw_input = input_file.readlines()  # brings everything into memory
        return [line.rstrip() for line in raw_input]


def q2_sample_input():
    return ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']


def q2_1():
    original_input = parse_input2()

    horizontal, depth = 0, 0
    for line in original_input:
        instruction, value = line.split(' ')
        value_int = int(value)

        if instruction == 'forward':
            horizontal += value_int
        elif instruction == 'down':
            depth += value_int
        elif instruction == 'up':
            depth -= value_int

        # print(line, (horizontal, depth))

    return horizontal * depth


def q2_2():
    original_input = parse_input2()

    horizontal, depth, aim = 0, 0, 0
    for line in original_input:
        instruction, value = line.split(' ')
        value_int = int(value)

        if instruction == 'forward':
            horizontal += value_int
            depth += (aim * value_int)
        elif instruction == 'down':
            aim += value_int
        elif instruction == 'up':
            aim -= value_int

        # print(line, (horizontal, depth))

    return horizontal * depth


def run():
    # print(q1())
    print(q1_2())


if __name__ == '__main__':
    run()
