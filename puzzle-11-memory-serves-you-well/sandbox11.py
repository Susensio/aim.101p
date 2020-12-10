coins_easy = [14, 3, 27, 4, 5, 15, 1]
coins_hard = [3, 15, 17, 23, 11, 3, 4, 5, 17, 23, 34, 17, 18, 14, 12, 15]

counter = 0


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
    global counter
    counter += 1
    if len(coins)-start == 0:
        return 0
    if len(coins)-start == 1:
        return coins[start]
    else:
        odd = coins[start] + coin_row(coins, start+2)
        even = coin_row(coins, start+1)
        return max(odd, even)


if __name__ == "__main__":
    print(coin_row(coins_hard))
    print(f"{counter=}")
