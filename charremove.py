s = input("Enter a string: ")
ch = input("Enter the character to be removed: ")
r = ""
for i in s:
    if i != ch:
        r += i
print(r)
