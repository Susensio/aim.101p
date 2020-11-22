from random import randint, seed

seed(0)
random_array = [randint(-100, 100) for _ in range(6)]
random_array_sorted = sorted(random_array)


def quicksort(array):
    if len(array) == 0:
        return []
    if len(array) == 1:
        return array

    smaller = []
    bigger = []
    pivots = []
    pivot = array[-1]

    for number in array:

        if number < pivot:
            smaller.append(number)
        elif number > pivot:
            bigger.append(number)
        else:
            pivots.append(number)

    return quicksort(smaller) + pivots + quicksort(bigger)


def test_quicksort():
    assert quicksort(random_array) == random_array_sorted
