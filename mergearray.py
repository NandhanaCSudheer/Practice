arr1 = list(map(int,input("Enter the first array elements: ").split()))
arr2 = list(map(int,input("Enter the second array elements: ").split()))
l = []
# for i in arr1:
#     l.append(i)
# for i in arr2:
#     l.append(i)
# print(l)


#  l = arr1 + arr2
#  arr1.extend(arr2)

i = 0
j = 0
while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        l.append(arr1[i])
        i += 1
    else:
        l.append(arr2[j])
        j += 1

while i < len(arr1):
    l.append(arr1[i])
    i += 1

while j < len(arr2):
    l.append(arr2[j])
    j += 1

print(l)