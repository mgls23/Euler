import math


def stairs(number):
    print('Permutations')
    for i in range(number):
        print(f'{i}: {_stairs(i)}')


def _stairs(number):
    if number < 0: return 0
    if number == 0: return 1

    return _stairs(number - 1) + _stairs(number - 2) + _stairs(number - 3)


RESULTS = {}


def _permutations(number, coins_available, paths=None):
    if paths is None: paths = [[]]

    if number < 0: return False, None
    if number == 0: return True, []
    if number in RESULTS: return True, RESULTS[number]

    result = []
    for coin in coins_available:
        valid, path_generated = _permutations(number - coin, coins_available, paths)
        if not valid: break
        for path in path_generated: result.append(path + [coin])
        if not path_generated: result.append([coin])

    print(f'Finished {number}')
    RESULTS[number] = result
    return True, result


HEY = {}


def digit_sum(number, coins, max_coin):
    available_coins = sorted(list(filter(lambda coin_: coin_ <= max_coin, coins)))

    result = []
    for coin in available_coins:
        if coin == 1:
            result.append([1] * number)
            continue

        upper_range = math.floor(number / coin) + 1

        for multiplier in range(1, upper_range):
            remainder = number - coin * multiplier
            if remainder < 0: break
            valid, possibles = better(remainder, coins, coins[coins.index(coin) - 1])
            if not valid: return result
            for possible in possibles: result.append([coin] * multiplier + possible)
            if not possibles: result.append([coin] * multiplier)

    return result


def better(number, coins, max_coin=None):
    if max_coin is None: max_coin = max(coins)

    available_coins = sorted(list(filter(lambda coin_: coin_ <= max_coin, coins)))
    if not available_coins: return False, [[]]
    if number == 0: return True, [[]]

    memoization_key = (number, max_coin)
    if memoization_key in HEY: return True, HEY[memoization_key]

    result = digit_sum(number, coins, max_coin)
    # print(f'(number, max_coin)={memoization_key}, result={result}')

    HEY[memoization_key] = result
    return True, result


# noinspection PyDefaultArgument
def coin_sums(coin_total, coins_available):
    _, paths = better(coin_total, sorted(coins_available))

    unique_combinations = set(tuple(sorted(path)) for path in paths)

    return len(unique_combinations)


def combinations_debug(number, coins_available, reverse=True):
    _, paths = better(number, sorted(coins_available))

    unique_combinations = set(tuple(sorted(path, reverse=reverse)) for path in paths)
    for path in sorted(unique_combinations, reverse=reverse): print(path)

    return len(unique_combinations), sorted(unique_combinations, reverse=reverse)
