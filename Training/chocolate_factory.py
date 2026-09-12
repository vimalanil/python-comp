arr = list(map(int, input().split()))
i = 0
while i<len(arr):
    if arr[i] == 0:
        a = arr.pop(i)
        i+=1
        arr.append(a)
print(arr)

# f = 0
# s = 0

# for f in range(len(arr)):
#     if arr[f] != 0:
#         arr[s] , arr[f] = arr[f],arr[s]
#         s += 1
# print(arr)      


