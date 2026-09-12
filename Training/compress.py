s = "aaaabbbcccdeee"
countarr = {}
res = ""
count = 1
# for i in range(len(s)):
#     countarr[s[i]] = countarr.get(s[i],0)+1
# print(countarr)

# for key,value in countarr.items():
#     temp = ""
#     temp = key + str(value)
#     res += temp
# print(res)
for i in range(len(s)):
    if i+1<len(s) and s[i]==s[i+1]:
        count += 1
    else:
        res += s[i]
        if count > 1:
            res += str(count)

        count = 1
print(res)

