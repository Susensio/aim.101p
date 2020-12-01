# Programming for the Puzzled -- Srini Devadas
# The Disorganized Handyman
# A recursive sorting algorithm based on pivoting where a pivot is selected
# and the list split into three lists: the first containing elements smaller
# than the pivot, second elements equal to the pivot, and the third containing
# elements greater than the pivot. These sublists are recursively sorted.


# This procedure selects a pivot and partitions the list into 3 sublists
# It only uses one element worth of additional storage for the pivot!
def pivotPartitionClever(lst, start, end):
    moves = 0
    iterations = 0

    pivot = lst[end]
    bottom = start - 1
    top = end

    done = False
    while not done:

        while not done:
            iterations += 1
            # Move rightward from left searching for element > pivot
            bottom += 1
            if bottom == top:
                done = True
                break
            if lst[bottom] > pivot:
                moves += 1
                lst[top] = lst[bottom]
                # print (lst, 'bottom =', bottom, 'top = ', top)
                break

        while not done:
            iterations += 1
            # Move leftward from right searching for element < pivot
            top -= 1
            if top == bottom:
                done = True
                break
            if lst[top] < pivot:
                moves += 1
                lst[bottom] = lst[top]
                # print (lst, 'bottom =', bottom, 'top = ', top)
                break

    lst[top] = pivot
    # print (lst)
    return top, moves, iterations


def quicksort(lst, start=0, end=None):
    total_moves = 0
    total_iterations = 0
    if end is None:
        end = len(a) - 1
    if start < end:
        # print ('Partition start: bottom =', start - 1, 'top = ', end)
        # print (lst)
        split, moves, iterations = pivotPartitionClever(lst, start, end)
        total_moves += moves
        total_iterations = iterations
        # print ('Partition end')
        moves, iterations = quicksort(lst, start, split - 1)
        total_moves += moves
        total_iterations += iterations

        moves, iterations = quicksort(lst, split + 1, end)
        total_moves += moves
        total_iterations += iterations
    return total_moves, total_iterations


if __name__ == "__main__":
    a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
    print('Initial list is:', a)
    moves, iterations = quicksort(a)
    print('Sorted list is:', a)
    assert moves == 9
    assert iterations == 24
    print(f"{iterations=}")

    already_sorted = list(range(100))
    moves, iterations = quicksort(already_sorted)
    assert moves == 0
    print("\nSorted list sorting")
    print(f"{iterations=}")

    random = [0] * 100
    random[0] = 29
    for i in range(100):
        random[i] = (9679 * random[i-1] + 12637 * i) % 2287
    moves, iterations = quicksort(random)
    print("\nRandom list sorting")
    print(f"{iterations=}")

    b = [4, 4, 65, 2, -31, 0, 99, 83, -31, 782, 1]
