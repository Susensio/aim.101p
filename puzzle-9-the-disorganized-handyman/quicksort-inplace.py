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
    pivot = lst[end]
    bottom = start - 1
    top = end

    done = False
    while not done:

        while not done:
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
    return top, moves


def quicksort(lst, start=0, end=None):
    moves = 0
    if end is None:
        end = len(a) - 1
    if start < end:
        # print ('Partition start: bottom =', start - 1, 'top = ', end)
        # print (lst)
        split, moves = pivotPartitionClever(lst, start, end)
        # print ('Partition end')
        moves += quicksort(lst, start, split - 1)
        moves += quicksort(lst, split + 1, end)
    return moves


if __name__ == "__main__":
    a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
    print('Initial list is:', a)
    moves = quicksort(a)
    print('Sorted list is:', a)
    assert moves == 9

    already_sorted = list(range(100))
    moves = quicksort(already_sorted)
    assert moves == 0

    b = [4, 4, 65, 2, -31, 0, 99, 83, -31, 782, 1]
