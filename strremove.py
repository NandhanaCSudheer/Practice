n = int(input())
str = input().split()
l = ""
l+=str[0]
l += " "
j = []
for i in range(1, len(str)):
    for b in str[i]:
        j.append(b)
    for k in j:
        if k not in l:
            l += k

print(l)