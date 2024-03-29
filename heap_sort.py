def heap_sort(arr):
    end = len(arr)-1
    heapify(arr, 0, end)
    while end > 0:
        swap(arr, 0, end)
        end -= 1
        sift(arr, 0, end)

def heapify(arr, begin, end):
    root = parent(end)
    while root >= begin:
        sift(arr, root, end)
        root -= 1

def sift(arr, begin, end):
    root = begin
    largest = root
    child = left_child(root)
    while child <= end:
        if arr[largest] < arr[child]:
            largest = child
        child = right_child(root)
        if child<=end and arr[largest]<arr[child]:
            largest = child
        if largest == root:
            return
        swap(arr, largest, root)
        root = largest
        child = left_child(root)

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def parent(i):
    return (i - 1) // 2

def left_child(i):
    return 2*i + 1

def right_child(i):
    return 2*i + 2

def is_sorted(arr, begin, end):
    for i in range(begin, end):
        if arr[i] > arr[i+1]:
            return False
        i += 1
    return True

def test_heap_sort():
    from time import time
    from random import seed, randint
    n = 1000
    seed(time())
    arr = [randint(1, n) for i in range(n)]
    if len(arr) <= 10:
        print('Initial list: {}'.format(arr))
    print('Sum before sort: {}'.format(sum(arr)))
    heap_sort(arr)
    if len(arr) <= 10:
        print('Sorted list: {}'.format(arr))
    print('Is sorted: {}'.format(is_sorted(arr, 0, len(arr)-1)))
    print('Sum after sort: {}'.format(sum(arr)))

if __name__ == '__main__':
    test_heap_sort()
