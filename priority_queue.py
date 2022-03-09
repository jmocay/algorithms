class priority_queue(object):
    def __init__(self, items=[]):
        self.items = items[:].copy()
        heapify(self.items, 0, len(self.items)-1)

    def enqueue(self, item):
        self.items.insert(0, item)
        sift(self.items, 0, len(self.items)-1)

    def dequeue(self):
        n = len(self.items)
        if n >= 0:
            if (n > 1):
                swap(self.items, 0, n-1)
                sift(self.items, 0, n-2)
            return self.items.pop()
        return None

    def size(self):
        return len(self.items)

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

def test_priority_queue():
    from time import time
    from random import seed, randint
    n = 10
    seed(time())
    arr = [randint(1, n) for i in range(n)]
    print('Enqueuing using constructor...')
    print('Enqueued items: {}'.format(arr))
    pq = priority_queue(arr)
    arr =  []
    while pq.size() > 0:
        arr.append(pq.dequeue())
    print('Dequeued items: {}'.format(arr))

    arr = [randint(1, n) for i in range(n)]
    print('Enqueueing using enqueue method...')
    print('Enqueuing items: {}'.format(arr))
    pq = priority_queue()
    for i in range(n):
        pq.enqueue(arr[i])
    arr =  []
    while pq.size() > 0:
        arr.append(pq.dequeue())
    print('Dequeued items: {}'.format(arr))

if __name__ == '__main__':
    test_priority_queue()
