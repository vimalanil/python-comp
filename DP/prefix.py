arr = [2, 4, 1, 3, 5]

prefix = []

# build prefix sum here
for i in range(len(arr)):
  if not prefix:
    prefix.append(arr[i])
  else:
    prefix.append(prefix[i-1] + arr[i])  

l = 1
r = 3

# find the range sum here
rsum = prefix[r] - prefix[l-1]

print(rsum)

# subarray sum using prefix sum

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix = 0
        count = 0

        freq = {0: 1}

        for num in nums:

            prefix += num

            needed = prefix - k

            if needed in freq:
                count += freq[needed]

            freq[prefix] = freq.get(prefix, 0) + 1

        return count