n = int(input())
k = int(input()) 
k = k % n
arr = list(map(int,input().split()))
l = []
for i in range(len(arr)-k,len(arr)):
    l.append(arr[i])


for i in range(len(arr)-k-1,-1,-1):
    arr[i+k] = arr[i]

for i in range(len(l)):
    arr[i] = l[i]
print(arr)