n = int(input("Enter the number: "))
if n < 0:
    print("Enter a positive number!!!")
elif n == 0 or n == 1:
    print("Factorial of ",n, " is 1")
else:
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print("Factorial of ",n, " is ",fact)