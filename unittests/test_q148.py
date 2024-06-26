from solutions.p148 import q148, brute_force, slightly_faster


# def test_is_brute_force_correct():
# 	assert brute_force(100 - 1) == 2361


# def test_brute_force_against_better():
# 	assert brute_force(7) == slightly_faster(7 + 1, debug_output=False)
# 	assert brute_force(100) == slightly_faster(100 + 1, debug_output=False)


# def test_multiples_of_7s():
# 	for i in range(49, 10 ** 4, 49):
# 		assert slightly_faster(i) == q148(i), i


# def test_better_against_optimal():
# 	# Complete parts first
# 	for power in range(1, 5):
# 		number = 7 ** power
# 		assert slightly_faster(number) == q148(number)

# 	# Weird cases
# 	seven_0, seven_1, seven_2, seven_3 = (7 ** power for power in range(4))
# 	combinations = [
# 		seven_3 + seven_1,
# 		seven_3 + seven_2 + seven_1,

# 		3 * seven_3 + 5 * seven_2 + seven_1 + 4 * seven_0
# 	]

# 	for number in combinations:
# 		assert slightly_faster(number) == q148(number)

# 	for number in range(6, 100):
# 		assert slightly_faster(number) == q148(number)


# def test_q148_simple():
# 	# Multiple of 7 :: +multiple of 6
# 	assert q148(7) == 6

# 	assert q148(8) == 11  # + 5
# 	assert q148(9) == 15  # + 4
# 	assert q148(10) == 18  # + 3
# 	assert q148(11) == 20  # + 2
# 	assert q148(12) == 21  # + 1
# 	assert q148(13) == 21  # + 0

# 	# Multiple of 7 :: +multiple of 6
# 	assert q148(14) == 12  # + 12
