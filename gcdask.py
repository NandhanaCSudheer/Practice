from math import gcd

n,k = map(int,input().split())
arr = list(map(int,input().split()))

count = 0
for i in range(n):
    current_gcd = 0
    for j in range(i,n):
        current_gcd = gcd(current_gcd,arr[j])
        if current_gcd == k:
            count += 1

print(count)