"""Helper functions implementing basic alogrithms used across several sandboxes."""

from typing import Iterable


def indexes_if_sorted(elements: Iterable):
    """What would the indexes of each element would be in a sorted version of itself

    >>> data = ['a', 'c', 'b']
    >>> indexes_if_sorted(data)
    (0, 2, 1)

    >>> data = [2, 3, 1]
    >>> indexes_if_sorted(data)
    (1, 2, 0)

    >>> data = [10, 5, 1, 3, 7]
    >>> indexes_if_sorted(data)
    (4, 2, 0, 1, 3)
    """

    return tuple(sorted(elements).index(el) for el in elements)


def sort(elements: Iterable) -> Iterable:
    """ Implements bubble sort algorithm with O(n²) complexity
    >>> data = [3, 2, 5, 1, 4]
    >>> sort(data)
    [1, 2, 3, 4, 5]
    """
    result = list(elements)
    for i in range(len(elements)):
        for j in range(i+1, len(elements)):
            if result[j] < result[i]:
                result[i], result[j] = result[j], result[i]
    return result


def sort_by_index(elements: Iterable, indexes: Iterable):
    """Rearrange elements by indexes

    >>> data = ['a', 'b', 'c']

    >>> sort_by_index(data, (2, 1, 0))
    ('c', 'b', 'a')
    >>> sort_by_index(data, (1, 0, 2))
    ('b', 'a', 'c')
    """

    return tuple(sort(elements)[index] for index in indexes)


def test_sorting_indexes():
    """Functions indexes_if_sorted and sort_by_index must be circular."""
    data = ['a', 'b', 'c', 'd']
    indexes = (3, 1, 0, 2)
    assert indexes_if_sorted(sort_by_index(data, indexes)) == indexes


def bin_to_int(binary: str) -> int:
    """
    >>> bin_to_int('0')
    0
    >>> bin_to_int('1')
    1
    >>> bin_to_int('10')
    2
    >>> bin_to_int('1010')
    10
    """
    result = 0
    for i, bit in enumerate(reversed(binary)):
        if bit == '1':
            result += (2**i)
    # return sum((2**i)*int(bit) for i, bit in enumerate(reversed(binary)))
    return result


def int_to_bin(number: int, bits) -> str:
    """
    >>> int_to_bin(0, 1)
    '0'
    >>> int_to_bin(2, 4)
    '0010'
    >>> int_to_bin(5, 4)
    '0101'
    >>> int_to_bin(13, 4)
    '1101'
    >>> int_to_bin(255, 8)
    '11111111'
    >>> int_to_bin(256, 8)
    Traceback (most recent call last):
    ...
    ValueError: Overflow
    """
    if number > 2**bits - 1:
        raise ValueError('Overflow')
    result = ['0'] * bits
    for i in range(bits):
        if number % 2:
            result[i] = '1'
        number = number // 2
    return ''.join(reversed(result))
