prices = list(map(int, input().split()))
max_profit = 0
# for f in range(len(prices)):
#     s = f+1
#     while s < len(prices):
#         if prices[s] > prices[f]:
#             max_profit = max(max_profit , prices[s]-prices[f])
#             s+=1
#         s+=1
# print(max_profit)

minSoFar = prices[0]
for i in range(1, len(prices)):
    minSoFar = min(minSoFar, prices[i])
    max_profit = max(max_profit, prices[i] - minSoFar)
print(max_profit)

print(prices.count(4))