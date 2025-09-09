import logging
from functools import lru_cache

BRITISH_COINS = [1, 2, 5, 10, 20, 50, 100, 200]


def coin_sums(total: int, coins: list[int]):
	@lru_cache(maxsize=None)
	def _count_ways(amount: int, min_index: int):
		if amount == 0:
			logging.debug(f'R: {amount}, M: {min_index}, Ans: 1')
			return 1

		if amount < 0 or min_index >= len(coins):
			logging.debug(f'R: {amount}, M: {min_index}, Ans: 0')
			return 0

		include = _count_ways(amount - coins[min_index], min_index)
		exclude = _count_ways(amount, min_index + 1)
		answer = include + exclude

		logging.debug(f'R: {amount}, M: {min_index}, Ans: {answer}')
		return answer

	return _count_ways(total, 0)


def q31():
	return coin_sums(200, BRITISH_COINS)


if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG)

	assert coin_sums(1, BRITISH_COINS) == 1
	assert coin_sums(2, BRITISH_COINS) == 2
	assert coin_sums(5, BRITISH_COINS) == 4
	assert coin_sums(11, BRITISH_COINS) == 12
	assert q31() == 73682
