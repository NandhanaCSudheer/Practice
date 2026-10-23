arr = list(map(int,input("Enter the elements: ").split()))
mini = arr[0]
for i in range(1,len(arr)):
    if mini > arr[i]:
        mini = arr[i]
print("The minimum element of array is: ",mini)