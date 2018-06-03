from random import randint


def sigma(list_, start=0, end=-1):
    sigma_ = 1
    for value in list_[start:end]: sigma_ *= value
    return sigma_


def find_max(list_, w=4):
    assert len(list_) >= w, "Stupid"

    last = list_[0]
    max_ = sigma(list_, 0, w)
    s = 0

    for i, value in enumerate(list_[w:], w):
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

        last = list_[i - w + 1]

    return max_


def brute_force(list_, window_size=4):
    max_ = -1
    for index in range(len(list_) - window_size + 1):
        max_ = max(sigma(list_, index, index + window_size), max_)

    return max_


def unit_test(list_, window=4):
    answer = find_max(list_, window)
    should_be = brute_force(list_, window)

    assert answer == should_be, locals()


def test():
    window = 4
    for _ in range(10000):
        random_list = [randint(0, 100) for _ in range(10)]
        unit_test(random_list, window)


test()
