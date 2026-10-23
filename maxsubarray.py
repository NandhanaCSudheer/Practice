n = int(input())
arr = list(map(int, input().split()))
count = arr[0]
c = 1
for i in range(n):
    tot = 0
    for j in range(i,n):
        tot += arr[j]
        if tot > count:
            count = tot
            c = j - i + 1

print(count)
print(c)