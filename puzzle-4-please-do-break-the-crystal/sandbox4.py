def simulate_ball_drops(n_balls, n_floors, hardness):
    radix = min_radix(n_balls, n_floors)
    floor = [0] * n_balls

    for index in reversed(range(n_balls)):
        for digit in range(1, radix):
            prev_floor = floor.copy()

            floor[index] = digit
            floor_number = decode(radix, floor)

            max_floor_exceeded = floor_number > n_floors
            if max_floor_exceeded:
                print("Max floor exceeded")
                floor = prev_floor
                break

            print(f"ball: {index}\tfloor:\t{floor_number}")

            ball_broke = hardness < floor_number
            if ball_broke:
                print("Ball broke!")
                floor = prev_floor
                break

    print(f"Hardness:{decode(radix, floor)}")


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


def encode(base, number):
    """Result is least significant digit first.
    That way, it is easier to access via index.
    """
    result = []
    while True:
        result.append(number % base)
        number = number // base
        if number == 0:
            break
    return tuple(result)


def decode(base, digits):
    """Least significant digit first
    >>> decode(3, (0, 1, 1))
    12
    """
    result = 0
    for position, digit in enumerate(digits):
        significance = base**position
        result += significance*digit
    return result


if __name__ == "__main__":
    simulate_ball_drops(4, 128, 4)
