arr = list(map(int,input("Enter the elements: ").split()))
l =[]
# d = {}
# for i in arr:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# for i in d:
#     if d[i] > 1:
#         l.append(i)
# print(l)

s = []
for i in arr:
    if i in l:
        s.append(i)
    else:
        l.append(i)
print(sorted(s))