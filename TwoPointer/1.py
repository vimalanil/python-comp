nums = [1, 2, 3, 4, 5]

l = 0
r = len(nums)-1
print(l,r)

while l < r :
    nums[r] , nums[l] = nums[l] , nums[r]
    l += 1
    r -= 1

print(nums)