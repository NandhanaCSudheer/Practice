n = int(input("Enter the binary number: "))
l = []
d = 0
while n >= 1:
    num = n % 10
    l.append(num)
    n = n // 10
for i in range(0,len(l)):
    a = l[i] * (2**i)
    d += a
print(d)

"""
n = int(input("Enter the binary number: "))
decimal = 0
power = 0

while n > 0:
    digit = n % 10
    decimal += digit * (2 ** power)
    power += 1
    n = n // 10

print(decimal)

"""