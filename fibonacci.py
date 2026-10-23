n = int(input("Enter a number: "))
print("The first ",n," terms of fibonacci series is: ")
a = 0
b = 1
for i in range(0,n):
    c = a + b
    print(a)
    a = b
    b = c