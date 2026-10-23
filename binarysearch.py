arr = list(map(int,input("Enter the elements: ").split(' ')))
key = int(input("Enter the element to be found: "))
arr = sorted(arr)
low = 0
found = False
high = len(arr)-1
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        print(key, " found at index ",mid)
        found = True
        break
    else:
        if arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
if found == False:
    print(key, " is not in the array")