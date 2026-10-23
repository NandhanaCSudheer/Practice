n = int(input())
words = []
for i in range(n):
    words.append(input())

res = ""
for i in range(len(words[0])):
    ch = words[0][i]
    flag = 1
    for j in range(1,n):
        if i >= len(words[j]) or ch != words[j][i]:
            flag = 0
            break

    if flag == 1:
        res += ch
print(res)