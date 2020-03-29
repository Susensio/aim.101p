"""Helper functions implementing basic alogrithms used across several sandboxes."""

from typing import Iterable


def count(elements: Iterable) -> dict:
    """
    >>> data = ['A','B','A']
    >>> counter = count(data)
    >>> counter['A']
    2
    >>> counter['B']
    1
    """
    counter = {}
    for el in elements:
        counter[el] = counter.get(el, 0) + 1
    return counter


def most_frequent(elements: Iterable):
    """
    >>> data = ['A', 'B', 'A']
    >>> most_frequent(data)
    'A'

    >>> data = ['A', 'B', 'A', 'B', 'C', 'B']
    >>> most_frequent(data)
    'B'

    >>> data = (_ for _ in ['Hearts', 'Spades', 'Diamonds', 'Diamonds', 'Clubs'])
    >>> most_frequent(data)
    'Diamonds'
    """
    counter = count(elements)
    return max(counter, key=counter.get)


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


def sort_by_index(elements: Iterable, indexes: Iterable):
    """Rearrange elements by indexes

    >>> data = ['a', 'b', 'c']

    >>> sort_by_index(data, (2, 1, 0))
    ('c', 'b', 'a')
    >>> sort_by_index(data, (1, 0, 2))
    ('b', 'a', 'c')
    """

    return tuple(sorted(elements)[index] for index in indexes)


def test_sorting_indexes():
    """Functions indexes_if_sorted and sort_by_index must be circular."""
    data = ['a', 'b', 'c', 'd']
    indexes = (3, 1, 0, 2)
    assert indexes_if_sorted(sort_by_index(data, indexes)) == indexes
