from euler.util.multiplications import decompose_to_prime_powers, multiply, gcd_powers, multiply_out_numbers_in_powers


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
    answers = generate_s()
    # print(answers)

    top_decomposed, bottom_composed = {}, {}
    for a, b in answers:
        top, bottom = min(a, b), max(a, b)

        top_decomposed = multiply(top_decomposed, decompose_to_prime_powers(top))
        bottom_composed = multiply(bottom_composed, decompose_to_prime_powers(bottom))

    gcd = gcd_powers(top_decomposed, bottom_composed)
    return multiply_out_numbers_in_powers(bottom_composed) / multiply_out_numbers_in_powers(gcd)


print(q33())
