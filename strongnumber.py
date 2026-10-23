n = int(input("Enter the number: "))
tot = 0
num = n
while n >= 1:
    digit = n % 10
    f = 1
    for i in range(1,digit+1):
        f *= i
    tot += f
    n = n // 10
if tot == num:
    print("The number is a strong number")
else:
    print("The number is not a strong number")
