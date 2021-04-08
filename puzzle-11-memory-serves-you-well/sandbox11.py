coins_easy = [14, 3, 27, 4, 5, 15, 1]
coins_hard = [3, 15, 17, 23, 11, 3, 4, 5, 17, 23, 34, 17, 18, 14, 12, 15]


def cache(func):
    cached = {}

    def inner(coins, start=0):
        key = tuple(coins), start
        if key in cached:
            return cached[key]
        else:
            result = func(coins, start)
            cached[key] = result
            return result

    return inner


@cache
def coin_row(coins, start=0):
    if len(coins)-start == 0:
        return 0
    if len(coins)-start == 1:
        return coins[start]
    else:
        odd = coins[start] + coin_row(coins, start+2)
        even = coin_row(coins, start+1)
        return max(odd, even)


@cache
def coin_row_backtrack(coins, start=0):
    if len(coins)-start == 0:
        return 0, []
    if len(coins)-start == 1:
        return coins[start], [coins[start]]
    else:
        # pick one
        accumulated, selected = coin_row_backtrack(coins, start+2)
        accumulated += coins[start]
        selected = [coins[start], *selected]
        pick_one = accumulated, selected

        # skip
        skip = coin_row_backtrack(coins, start+1)

        return max(pick_one, skip)


# EXERCISE 1
# Solve a variant coin row problem where if you pick a coin you can
# pick the next one, but if you pick two in a row, you have to skip two coins.
@cache
def coin_row_variant(coins, start=0):
    if len(coins)-start <= 0:    # below zero values must be handled, as double pick could overflow
        return 0, []
    if len(coins)-start == 1:
        return coins[start], [coins[start]]
    else:
        # pick two
        accumulated, selected = coin_row_variant(coins, start+4)
        accumulated += coins[start] + coins[start+1]
        selected = [coins[start], coins[start+1], *selected]
        pick_two = accumulated, selected

        # pick one
        accumulated, selected = coin_row_variant(coins, start+2)
        accumulated += coins[start]
        selected = [coins[start], *selected]
        pick_one = accumulated, selected

        # skip
        skip = coin_row_variant(coins, start+1)

        return max(pick_two, pick_one, skip)


if __name__ == "__main__":
    print(coin_row(coins_easy))

    print(coin_row_backtrack(coins_easy))

    print(coin_row_variant(coins_easy))
