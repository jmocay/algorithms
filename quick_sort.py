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

from datetime import datetime
from random import seed, randint

if __name__ == '__main__':

    seed(datetime.now())

    n = 100
    arr = n * [0]
    for i in range(n):
        arr[i] = randint(1, 100)

    print(arr, sum(arr))
    quicksort(arr)
    print(arr, sum(arr))
