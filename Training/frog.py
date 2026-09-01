def possible(i, curr , k):
    jump = [-1 , +0 , +1]

    while curr < len(arr):

        if curr == len(arr)-1:
            return True
        elif arr[curr] == arr[i]:
            for j in jump:
                return possible(i+1, curr + k  , k +j)
        else:
            return False    

arr = [0, 1, 3, 5, 6, 8, 12, 17]
print(possible(0, 0 , 1))    