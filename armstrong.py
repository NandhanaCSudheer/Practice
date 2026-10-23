n = int(input("Enter a number: "))
digit = 0
org = n
while n >= 1:
    num = n % 10
    digit = digit + num * num * num
    n = n // 10
if digit == org:
    print(org, "is an armstrong number")
else:
    print(org, "is not an armstrong number")