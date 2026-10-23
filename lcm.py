a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if a == 0 or b == 0:
    lcm = 0
else:
    if a >= b:
        j = a
    else:
        j = b
    m = a * b
    for i in range(j,m+1):
        x = i % a
        y = i % b
        if x == 0 and y == 0:
            lcm = i
            break
print("LCM of ",a," and ",b, " is ",lcm)

