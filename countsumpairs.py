# n,k = map(int,input().split())
# arr = list(map(int,input().split()))
# d = {}
# s = set()
# count = 0
# for i in arr:
#     d[i] = k - i
# for i in arr:
#     complement = k - i
#     if complement in d and i not in s:
#         count += 1
#         s.add(i)
#         s.add(complement)
# print(count)


n, k = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] + arr[j] == k:
            count += 1
print(count)
