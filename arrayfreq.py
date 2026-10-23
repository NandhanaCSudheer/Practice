arr = list(map(int,input("Enter the elements: ").split()))
d = {}
for i in arr:
    d[i] = 0
for i in arr:
    d[i] += 1
print(d)

"""
for i in arr:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

"""