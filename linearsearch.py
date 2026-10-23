arr = list(map(int,input("Enter the elements: ").split(' ')))
key = int(input("Enter the element to be found: "))
found = 0
for i in range(0,len(arr)):
    if arr[i] == key:
        print(key, " is found at index ",i)
        found = 1
        break
if found == 0:
    print(key, " is not in the array")
    