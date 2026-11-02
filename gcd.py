a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
# a = x
# b = y

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

# while b:
#     a,b = b, a % b
# print("GCD of ",x, "and ",y, " is ",a)
# print("LCM of ",x, "and ",y, " is ",(x * y)//a)