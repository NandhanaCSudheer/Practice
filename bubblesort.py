arr = list(map(int,input("Enter the elements: ").split(' ')))
for j in range(0,len(arr)-1):
    for i in range(0,len(arr)-1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
print(arr)

#     for j in range(0,len(arr)-1-j):     avoids checking sorted elements