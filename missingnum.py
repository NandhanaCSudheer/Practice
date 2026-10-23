n = int(input("Enter the size: "))
arr = list(map(int,input("Enter the elements: ").split()))
m = 1
for i in range(1,n-1):
    if arr[i] - arr[i - 1] != 1:
        m = (i - 1) + 1
        break
print("The missing number is: ",m)

"""
n = int(input("Enter N: "))
arr = list(map(int, input("Enter the elements: ").split()))
total = n * (n + 1) // 2
s = sum(arr)
print("Missing number:", total - s)

"""