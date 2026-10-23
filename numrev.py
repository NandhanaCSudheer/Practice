n = int(input("Enter a number: "))
rev = 0
while n >= 1:
    num = n % 10
    rev = rev * 10 + num
    n = n // 10
print(rev)