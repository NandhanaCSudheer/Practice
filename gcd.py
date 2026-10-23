a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a >= b:
    m = b
else:
    m = a

for i in range(m,0,-1):
    x = a % i
    y = b % i
    if x == 0 and y == 0:
        gcd = i
        break

print("GCD of ",a, "and ",b, " is ",gcd)
print("LCM of ",a, "and ",b, " is ",(a * b)//gcd)