arr = list(map(int,input("Enter the elements: ").split()))
e = 0
o = 0
for i in arr:
    if i % 2 == 0:
        e += 1
    else:
        o += 1
print("The count of even numbers is: ",e)
print("The count of odd numbers is: ",o)