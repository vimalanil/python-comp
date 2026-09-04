s = ")())())"

def longest(s):
  stack = [-1]
  l = 0

  for i in range(len(s)):
    if s[i] == "(":
      stack.append(i)
    elif s[i] == ")":
      stack.pop()
      if not stack:
        stack.append(i)
      l = max(l,i - stack[-1])  
  return l      


print(longest(s))


