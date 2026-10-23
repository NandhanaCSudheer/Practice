s = input("Enter the string: ")
l = []
for i in s:
    if i not in l:
        l.append(i)
t = ""
for i in l:
    t = t + i

# print(t)
# c = ''.join(l)   
# print(c)
