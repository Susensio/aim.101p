def simulate_ball_drops(n_balls, n_floors, hardness):
    radix = min_radix(n_balls, n_floors)
    for ball in range(n_balls):
        ...


def min_radix(digits, largest):
    # Calculate radix that can represent the largest number with given digits.
    # radix ^ digits > largest
    radix = ceil(largest**(1/digits))
    return radix


def ceil(number):
    if number - int(number) == 0:
        return int(number)
    else:
        return int(number + 1)
