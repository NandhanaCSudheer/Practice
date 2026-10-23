arr = list(map(int,input("Enter the elements: ").split()))
target = int(input("Enter the target: "))
# key = 0
# while key < len(arr):
#     for i in range(key+1,len(arr)):
#         if (target - arr[i]) == arr[key]:
#             print(i,key)
#             exit()
#     key += 1

d = {}
for i in range(len(arr)):
    d[arr[i]] = i
for i in arr:
    complement = target - i
    if complement in d and d[complement] != d[i]:
        print(d[i],d[complement])
        break
