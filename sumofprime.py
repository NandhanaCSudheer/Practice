n = int(input("Enter the range: "))
tot = 2
if n == 0 or n == 1:
    print ("Sum = 0")
elif n == 2:
        print("Sum = 2")
else:
    for i in range(3,n+1):
        s = 0
        for j in range(2,i):
            if i % j == 0:
                s = 1
                break
        if s == 0:
            tot += i
    print("Sum = ",tot)