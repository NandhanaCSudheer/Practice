n = int(input("Enter a number: "))
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)
if n >= 0:
    print("The factorial of ",n," is ",fact(n))
else:
    print("Enter a positive number!!!")