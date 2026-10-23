n = int(input())
arr = list(map(int,input().split()))

num = set(arr)
long = 0
for i in num:
    if i - 1 not in num:
        current = 1
        length = 1

        while current + 1 in num:
            current += 1
            length += 1
        long = max(long,length)

print(long)