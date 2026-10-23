arr = list(map(int,input("Enter the elements: ").split(',')))
a = sorted(arr)
print(" The second largest element of the array is: ",a[-2])

"""
arr = list(map(int, input("Enter the elements: ").split(',')))

largest = arr[0]
second = arr[0]

for i in arr:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Second largest element:", second)

"""
"""
arr = list(map(int, input("Enter the elements: ").split(',')))

largest = float('-inf')
second = float('-inf')

for i in arr:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

if second == float('-inf'):
    print("No second largest element")
else:
    print("Second largest element:", second)

"""