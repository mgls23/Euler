from random import randint


def sigma(list_, start=0, end=-1):
    sigma_ = 1
    for value in list_[start:end]: sigma_ *= value
    return sigma_


def _first_n_free_of(list_, n, element=0):
    """
    [e(0), e(1), e(2), ... e(i-n), e(i-n+1), ... e(i-1), e(i)]
                          |             window               |

    :return the first i for which the previous 'window' does not contain
        the element
    """
    if element in list_[:n]:
        last_zero_reversed = list(reversed(list_[:n])).index(0)
        index = n - last_zero_reversed
        non_zeros = 0

        while index < len(list_):
            if list_[index] == element:
                non_zeros = 0

            else:
                non_zeros += 1
                if non_zeros == n:
                    return index + 1

            index += 1

        return index
    else:
        return n


def find_max(list_, w=4):
    assert len(list_) >= w, "Stupid"

    start = _first_n_free_of(list_, w)

    last = list_[start - w]
    max_ = sigma(list_, start - w, start)
    s = 0

    for i, value in enumerate(list_[start:], start):
        if value > last:
            if s < w:
                if s == 0:
                    max_ = (max_ // last) * value
                else:
                    left = sigma(list_, i - w - s, i - w + 1)
                    right = sigma(list_, i - s, i + 1)

                    if right > left:
                        max_ = right * sigma(list_, i - w + 1, i - s)
                        s = 0
                    else:
                        s += 1
            else:
                current = sigma(list_, i - w + 1, i + 1)
                if current > max_:
                    max_ = current
                    s = 0
                else:
                    s += 1

        else:
            s += 1

        last = list_[i - w + 1]

    return max_, locals()


def brute_force(list_, window_size=4):
    max_ = -1
    for index in range(len(list_) - window_size + 1):
        max_ = max(sigma(list_, index, index + window_size), max_)

    return max_


def unit_test(list_, window=4):
    answer, dict_ = find_max(list_, window)
    should_be = brute_force(list_, window)

    assert answer == should_be, locals()
    # if answer != should_be:
    #     print('\n{}\n{}'.format(pprint(dict_), pprint(locals())))
    #     exit(0)


def test():
    window = 4
    for _ in range(100000):
        random_list = [randint(0, 100) for _ in range(10)]
        unit_test(random_list, window)


test()
