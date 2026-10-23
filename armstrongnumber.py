n = int(input("Enter a number: "))
digit = 0
count = 0
prod = 1
org = n
no = n
while n >= 1:
    num = n % 10
    n = n // 10
    count = count + 1
while no >= 1:
    num = no % 10
    digit = digit + num**count
    no = no // 10
if digit == org:
    print(org, "is an armstrong number")
else:
    print(org, "is not an armstrong number")