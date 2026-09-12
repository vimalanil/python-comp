ar = list(map(int, input().split()))
n = ar.pop(0)
op = []
for i in range(len(ar)):
    if ar[i] == 1:
        op.append(ar[i+1])
    if ar[i] == 2:
        if not len(op):
            print("No patient", end=" ")
        else:
            # op.sort()
            # temp = op.pop(0)
            higest_priority = min(op)
            op.remove(higest_priority)
            print(higest_priority, end=" ")
    
