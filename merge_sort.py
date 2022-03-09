def sort(arr):
    merge_sort(arr, 0, len(arr)-1)

def merge_sort(arr, lo, hi):
    if lo >= hi:
        return
    mid = (lo + hi) // 2
    merge_sort(arr, lo, mid)
    merge_sort(arr, mid+1, hi)
    merge(arr, lo, mid, hi)

def merge(arr, lo, mid, hi):
    buff = arr[lo:hi+1].copy()
    i = lo
    j = mid+1
    for k in range(lo, hi+1):
        if i<=mid and j<=hi:
            if buff[i-lo] < buff[j-lo]:
                arr[k] = buff[i-lo]
                i += 1
            else:
                arr[k] = buff[j-lo]
                j += 1
        elif i<=mid:
            arr[k] = buff[i-lo]
            i += 1
        else:
            arr[k] = buff[j-lo]
            j += 1

def test_merge_sort():
    def is_sorted(arr):
        for i in range(len(arr)-1):
            if arr[i+1] < arr[i]:
                return False
        return True
    from time import time
    from random import seed, randint
    n = 1000
    arr = [randint(1, n) for i in range(n)]
    if n <= 10:
        print('Unsorted list: {}'.format(arr))
    print('List sum before sort: {}'.format(sum(arr)))
    sort(arr)
    if n <= 10:
        print('Sorted list: {}'.format(arr))
    print('List sum after sort: {}'.format(sum(arr)))
    print('List is sorted: {}'.format(is_sorted(arr)))

if __name__ == '__main__':
    test_merge_sort()