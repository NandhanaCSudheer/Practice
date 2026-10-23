arr = list(map(int, input("Enter the elements: ").split()))
for j in range(len(arr)-1):
    min_index = j
    for i in range(j+1, len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i
    arr[j], arr[min_index] = arr[min_index], arr[j]
print(arr)