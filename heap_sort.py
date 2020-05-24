def heap_sort(arr):
    heapify(arr)
    end = len(arr) - 1
    while end > 0:
        swap(arr, 0, end)
        end -= 1
        sift_down(arr, 0, end)

def heapify(arr):
    begin = len(arr) - 1
    while begin >= 0:
        sift_down(arr, begin, len(arr) - 1)
        begin -= 1


def sift_down(arr, begin, end):
    root = begin
    while left_child(root) <= end:
        child = left_child(root)
        least = root
        if arr[least] < arr[child]:
            least = child
        if child + 1 <= end and arr[least] < arr[child + 1]:
            least = child + 1
        if least == root:
            return
        else:
            swap(arr, root, least)
            root = least

def parent(i):
    return (i - 1) // 2

def left_child(i):
    return 2 * i + 1

def right_child(i):
    return 2 * i + 2

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

from datetime import datetime
from random import seed, randint

if __name__ == '__main__':
    n = 100
    arr = [randint(1, 100) for i in range(n)]
    print(arr, 'sum: ', sum(arr))
    heap_sort(arr)
    print('sorted: ', arr, 'sum: ', sum(arr))
