from solutions.p111 import find_primes_with_runs, q111


def test_function_m_example():
    expected_for_1 = [1117, 1151, 1171, 1181, 1511, 1811, 2111, 4111, 8111]

    result = find_primes_with_runs(repeating_number='1', digit=4)
    assert sorted(list(result)) == expected_for_1


def test_4_digit_sums_all():
    assert [sum(find_primes_with_runs(d, digit=4)) for d in '0123456789'] == [
        67061,
        22275,
        2221,
        46214,
        8888,
        5557,
        6661,
        57863,
        8887,
        48073,
    ]


def test_q111():
    assert [sum(find_primes_with_runs(d, digit=10)) for d in '0123456789'] == [
        38000000042,
        12882626601,
        97447914665,
        23234122821,
        4444444447,
        5555555557,
        6666666661,
        59950904793,
        285769942206,
        78455389922,
    ]

    assert q111() == 612407567715
