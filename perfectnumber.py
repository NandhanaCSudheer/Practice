n = int(input("Enter the number: "))
tot = 0
for i in range(1,n//2 + 1):
    if n % i == 0:
        tot += i
if tot == n:
    print("The number is a perfect number")
else:
    print("The number is not a perfect number")