from euler.smallest_multiple import decompose_to_prime_powers


def generate_s():
    answer = set()
    for a in range(1, 10):
        for b in range(1, 10):
            original = a * 10 + b
            for d in range(1, 10):
                e = a
                denominator = d * 10 + e

                for c in range(1, 10):
                    for f in range(1, 10):
                        if c == f: continue

                        bc = b * c
                        df = d * f
                        ef = e * f

                        if ((a * c) + (bc // 10)) == (df + (ef // 10)):
                            if (bc % 10) == (ef % 10):
                                if bc == df:
                                    # print((original, c, denominator, f))
                                    answer.add((original, denominator))

    return answer


def q33():
    bottoms = 0
    answers = generate_s()
    # print(answers)
    for a, b in answers:
        top, bottom = min(a, b), max(a, b)

        top_decomposed = decompose_to_prime_powers(top)
        for b_number, b_powers in decompose_to_prime_powers(bottom).items():
            powers = (b_powers - top_decomposed.get(b_number, 0))
            bottoms += powers and b_number ** powers

        # print(top, bottom, bottoms)

    return bottoms


print(q33())
