b = int(input("Enter the base number: "))
e = int(input("Enter the exponent: "))
n = 1
for i in range(e):
    n = n * b
print( b, "raised to the power",e, "is ",n)
print(b**e)