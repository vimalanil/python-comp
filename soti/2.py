s = "abba"

def longestsubstring(s):
  left = 0
  right = 0
  longest = 0

  for i in range(len(s)):
    if s[right] in s[left:right]:
      for i in range(left,left+len(s[left:right])):
        if s[right] == s[i]:
          left = i+1
    else:
      longest = max(longest,len(s[left:right])+1)
      right+=1

  return longest   

print(longestsubstring(s))        