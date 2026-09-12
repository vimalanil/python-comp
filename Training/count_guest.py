Enter = list(map(int, input().split()))
Leave = list(map(int, input().split()))
max_guest = 0
guest = []
guest.append(Enter[0]-Leave[0])
for i in range(1,len(Enter)):
    guest.append(Enter[i]-Leave[i]+guest[i-1])
print(max(guest))