"""
    Given a sorted array, find the index of a given value
    in the array. Return -1 if the value is not in the array.
"""
def binary_search(arr, val):
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == val:
            return mid
        elif val < arr[mid]:
            hi = mid - 1
        else:
            lo = mid + 1

    return -1

from datetime import datetime
from random import seed, randint

if __name__ == '__main__':

    seed(datetime.now())

    n = 100
    arr = [randint(1, 100) for i in range(n)]

    arr.sort()

    i = binary_search(arr, 23)
    if i >= 0:
        print(i, arr[i] == 23, arr[i])
    else:
        print('Not found.')

    print('Not found: ', binary_search(arr, 150) == -1)
