def merge_sort(arr):
    merge_sort_helper(arr, 0, len(arr) - 1)

def merge_sort_helper(arr, lo, hi):
    if hi <= lo:
        return
    mid = (lo + hi) // 2
    arr1 = arr[lo:mid+1]
    arr2 = arr[mid+1:hi+1]
    merge_sort_helper(arr1, 0, len(arr1) - 1)
    merge_sort_helper(arr2, 0, len(arr2) - 1)
    merge(arr1, 0, len(arr1) - 1, arr2, 0, len(arr2) - 1, arr, lo)

def merge(arr1, lo1, hi1, arr2, lo2, hi2, arr, lo):
    i = lo1
    j = lo2
    k = lo

    while i <= hi1 and j <= hi2:
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1

    while i <= hi1:
        arr[k] = arr1[i]
        i += 1
        k += 1

    while j <= hi2:
        arr[k] = arr2[j]
        j += 1
        k += 1

# ok!
def test_merge():
    n = 5
    # arr1 = [ 2 * k + 1 for k in range(n) ]
    # arr2 = [ 2 * (k + 1) for k in range(n) ]
    arr1 = 4 * [1]
    arr2 = 3 * [2]
    arr = (len(arr1) + len(arr2)) * [0]
    print('arr1:', arr1)
    print('arr2:', arr2)
    merge(arr1, 0, len(arr1) - 1, arr2, 0, len(arr2) - 1, arr, 0)
    print('merged arr1, arr2: ', arr)

# ok!
def test_merge_sort():
    from datetime import datetime
    from random import seed, randint

    seed(datetime.now())
    n = 101
    arr = [randint(1, 100) for i in range(n)]
    print('original array: ', arr, ' sum: ', sum(arr))
    merge_sort(arr)
    print('merge_sorted array: ', arr, ' sum: ', sum(arr))

if __name__ == '__main__':
    test_merge_sort()
