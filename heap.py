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

def is_heap(arr, begin, end):
    while end > begin:
        if arr[end] > arr[parent(end)]:
            return False
        end -= 1
    return True

def test_heap():
    from time import time
    from random import seed, randint
    n = 10
    seed(time())
    arr = [randint(1, n) for i in range(n)]
    print('Initial list: {}'.format(arr))
    heapify(arr, 0, len(arr)-1)
    print('Heapified list: {}'.format(arr))
    print('Is heap: {}'.format(is_heap(arr, 0, len(arr)-1)))

if __name__ == '__main__':
    test_heap()
