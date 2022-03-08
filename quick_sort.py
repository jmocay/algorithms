def quicksort(arr):
    quicksort_helper(arr, 0, len(arr) - 1)

def quicksort_helper(arr, lo, hi):
    if hi <= lo:
        return
    j = partition(arr, lo, hi)
    quicksort_helper(arr, lo, j - 1)
    quicksort_helper(arr, j + 1, hi)

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

"""
    Partition the array such that:
        set pivot element to arr[hi]
        elements < pivot is on the left of the pivot
        elements >= pivot is on the right of the pivot
    Return the index of pivot after the partition
"""
def partition(arr, lo, hi):
    mid = (lo + hi) // 2
    if arr[mid] < arr[lo]:
        swap(arr, lo, mid)
    if arr[hi] < arr[lo]:
        swap(arr, lo, hi)
    if arr[mid] < arr[hi]:
        swap(arr, mid, hi)
    pivot = arr[hi]
    j = lo - 1
    i = lo
    while i < hi:
        if arr[i] < pivot:
            j += 1
            swap(arr, i, j)
        i += 1
    j += 1
    swap(arr, i, j)

    return j

if __name__ == '__main__':
    from time import time
    from random import seed, randint

    seed(time())

    n = 50000
    arr = [randint(1, n) for i in range(n)]

    if len(arr) <= 10:
        print('List before sort: {}'.format(arr))
    print('Sum of list before sort: {}'.format(sum(arr)))
    quicksort(arr)
    if len(arr) <= 10:
        print('List after sort: {}'.format(arr))
    print('Sum of list after sort: {}'.format(sum(arr)))
