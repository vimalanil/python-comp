s = "hello"

stack = []

for char in s:
    stack.append(char)

res = ""

while stack:
    res += stack.pop()

print(res)