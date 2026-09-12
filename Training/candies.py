t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    i = 0
    while len(a) > 1:
        a.sort()
        temp = 0
        temp = a[i]+a[i+1]
        res += temp
        a.append(temp)
        a.pop(i)
        a.pop(i)
    print(res)




