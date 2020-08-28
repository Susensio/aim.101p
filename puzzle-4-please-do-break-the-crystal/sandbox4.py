import pytest


# def simulate_ball_drops(n_balls, n_floors, hardness):
#     radix = min_radix(n_balls, n_floors)
#     floor = [0] * n_balls
#     for digit in reversed(range(n_balls)):
#         print(f"digit:\t{digit}")
#         significance = radix ** digit
#         for digit in range(1, radix):
#             print(digit*significance)

#             max_floor_exceeded = floor > n_floors
#             if ball_broke or max_floor_exceeded:
#                 break


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
#     SUBINDEX = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

#     def __repr__(self):
#         return f"{self.__class__.__name__}({radix})"

#     class Number:
#         def __init__(self, number):
#             self._digits = list(reversed(number))

#         def to_int(self):
#             ...

#         @classmethod
#         def from_int(cls, n):
#             result = []
#             while True:
#                 result.append(n % radix)
#                 n = n // radix
#                 if n == 0:
#                     break

#             return cls(result)

#         def __str__(self):
#             return f"{self._digits} {str(radix).translate(SUBINDEX)}"

#         def __repr__(self):
#             return f"NumberBase({radix}).Number({str(self).split('_')[0]})"

#     return Number


class Base:
    """ Basic operations between arbitrary base numbers.

    >>> t = Base(3)
    >>> t
    Base(3)
    >>> t.from_int(5)
    NumberBase([1, 2], 3)
    """

    def __init__(self, base):
        self.base = base

    def __call__(self, number):
        return NumberBase(number, self.base)

    def from_int(self, number):
        return NumberBase.from_int(number, self.base)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.base})"


class NumberBase:
    SUBINDEX = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

    def __init__(self, number, base):
        self._digits = list(reversed(number))
        self.base = base

        for digit in self._digits:
            if digit >= base:
                raise OverflowError

    def to_int(self):
        result = 0
        for i, digit in enumerate(self._digits):
            result += digit*(2**i)
        return result

    @classmethod
    def from_int(cls, n, base):
        result = []
        while True:
            result.append(n % base)
            n = n // base
            if n == 0:
                break

        return cls(reversed(result), base)

    def __str__(self):
        return f"{self._digits} {str(self.base).translate(self.SUBINDEX)}"

    def __repr__(self):
        return f"NumberBase({self._digits}, {self.base})"


@pytest.mark.parametrize('number', range(5))
@pytest.mark.parametrize('base', range(2, 5))
def test_number_base(number, base):
    assert NumberBase.from_int(number, base).to_int() == number


@pytest.mark.parametrize('number', range(10))
def test_number_binary(number):
    assert NumberBase.from_int(number, 2).to_int() == number


# if __name__ == "__main__":
#     simulate_ball_drops(4, 128, 1)
b = NumberBase([1], 2)
