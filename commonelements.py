arr1 = list(map(int,input("Enter the elements of first array: ").split()))
arr2 = list(map(int,input("Enter the elements of second array: ").split()))
l = []
for i in arr1:
    if i in arr2 and i not in l:
        l.append(i)
print("The common elements are: ",l)