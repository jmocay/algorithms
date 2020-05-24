"""
    Partition the array such that the elements
    where func(arr[i]) is false is on the left of the array
    while func(arr[i]) is true is on the right of the array
"""
def partition(arr, func):
    j = -1
    for i in range(len(arr)):
        if func(arr[i]):
            if j < 0:
                j = i
        else:
            if j >= 0:
                tmp = arr[j]
                arr[j] = arr[i]
                arr[i] = tmp
                j += 1
    return j

from datetime import datetime
from random import seed, randint

if __name__ == '__main__':
    seed(datetime.now())

    n = 20
    arr = [randint(1, 100) for i in range(n)]

    print(arr, sum(arr))

    is_even = lambda x: x % 2 == 0
    j = partition(arr, is_even)
    print(j, arr[j], arr, sum(arr))
