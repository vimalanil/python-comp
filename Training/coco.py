arr = list(map(int, input().split()))
i = 0
while i < len(arr):
    if arr[i] == 0:
        a = arr.pop(i)
        i += 1
        arr.append(a)

print(arr)        