n = int(input("Enter a number: "))
k = 0
if n < 2:
    print(n, "is not a prime")
elif n == 2:
    print(n, "is a prime number")
else:
    for i in range(2,(n//2)+1):
        if n%i == 0:
            print(n, "is not a prime")
            k = 1
            break
    if k == 0:
        print(n, "is a prime number")