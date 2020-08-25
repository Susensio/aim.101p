def simulate_ball_drops(n_balls, n_floors, hardness):
    radix = min_radix(n_balls, n_floors)
    floor = [0] * n_balls
    for ball in reversed(range(n_balls)):
        significance = radix ** (n_balls-ball)
        for digit in range(radix):
            print(digit*significance)
            if hardness <


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


# def NumberBase(radix):
#     class Number:
#         def __init__(self, number):
#             self.number = str(number)

#         def to_int(self):
#             ...

#         @classmethod
#         def from_int(n):
#             result = []
#             while n != 0:
#                 result.append(n % radix)
#                 n = n // radix

#             return ''.join(reversed(result))

#         def __str__(self):
#             base = str(radix)+"x"
#             return base+self.number

#     return Number
