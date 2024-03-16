from solutions.p17 import number_letter_counts, remove_spaces_and_hyphens, q17


def _test_translate(number: int, string: str, score: int):
	result = number_letter_counts(number)
	stripped_string = remove_spaces_and_hyphens(string)

	assert (result == score), f"{result} != {score}"
	assert (score == len(stripped_string)), f"{score} != len({stripped_string})"


def test_translate():
	# No need to test any entries in NUMBER_TO_STRING other than 1
	_test_translate(1, "one", score=3)
	_test_translate(12, "twelve", score=6)
	_test_translate(14, "fourteen", score=8)
	_test_translate(40, "forty", score=5)
	_test_translate(100, "one-hundred", score=10)
	_test_translate(256, "two-hundred and fifty-six", score=21)


def test_q17():
	assert q17() == 21124
