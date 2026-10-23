s = input().strip()

stack = []
pairs = {']':'[','}':'{',')':'('}
valid = 1

for i in s:
    if i in "[{(":
        stack.append(i)
    elif i in "]})":
        if not stack or stack[-1] != pairs[i]:
            valid = 0
            break
        stack.pop()
    
if not stack and valid:
    print("Valid")
else:
    print("Invalid")