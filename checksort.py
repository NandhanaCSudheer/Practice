arr = list(map(int,input("Enter the elements: ").split()))
s = True
for i in range(1,len(arr)):
    if arr[i - 1] > arr[i]:
        s = False
        print("The array is not sorted!!!")
        break
if s == True:
    print("The array is sorted!!!")