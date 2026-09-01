def binsearch(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1  

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binsearch(arr, target, mid + 1, right)
    else:
        return binsearch(arr, target, left, mid - 1)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binsearch(arr, 5)) 




