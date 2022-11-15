import logging
import random

from euler.util.decorators import timed_function


def investigate_1():
    # odds = 0.5
    # 2 rounds
    #   - 0.5 LOSE
    #   - 0.5 AGAIN
    #       - 0.25 WIN
    #       - 0.25 START_AGAIN

    total_outcomes = 3 * 4 * 1000
    round_numbers = 10
    lost, won = 0, 0

    def helper(round_number):
        nonlocal lost, won

        ceiling = 60
        half, quarter = ceiling // 2, ceiling // 4
        generated = random.randint(1, ceiling)

        if round_number == round_numbers:
            if generated <= half:
                lost += 1
            else:
                won += 1

            return

        if generated <= half:
            lost += 1
        elif generated <= quarter * 3:
            won += 1
        else:
            helper(round_number + 1)

    for _ in range(total_outcomes):
        helper(0)

    return lost, won


def investigate_2():
    # odds = 0.5
    # 2 rounds
    # = S1 (BEG)
    #   - 0.5 LOSE
    #   - 0.5 NEXT -> S2
    #     = S2
    #       - 0.25 START_AGAIN -> S1
    #       - 0.25 NEXT -> S3
    #         = S3
    #           - 0.125

    total_outcomes = 3 * 4 * 1000
    round_numbers = 10
    lost, won = 0, 0

    def helper(round_number):
        nonlocal lost, won

        ceiling = 60
        half, quarter = ceiling // 2, ceiling // 4
        generated = random.randint(1, ceiling)

        if round_number == round_numbers:
            if generated <= half:
                lost += 1
            else:
                won += 1

            return

        if generated <= half:
            lost += 1
        elif generated <= quarter * 3:
            won += 1
        else:
            helper(round_number + 1)

    for _ in range(total_outcomes):
        helper(0)

    return lost, won


def q499():
    print(investigate_1())
    return -1


if __name__ == '__main__':
    import sys

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    assert (timed_function(q499)() == -1)
