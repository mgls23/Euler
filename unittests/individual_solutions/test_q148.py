from individual_solutions.q148 import q148


def test_q148_simple():
	# Multiple of 7 :: +multiple of 6
	assert q148(7) == 6

	assert q148(8) == 11  # + 5
	assert q148(9) == 15  # + 4
	assert q148(10) == 18  # + 3
	assert q148(11) == 20  # + 2
	assert q148(12) == 21  # + 1
	assert q148(13) == 21  # + 0

	# Multiple of 7 :: +multiple of 6
	assert q148(14) == 12  # + 12
