n = int(input("Enter a number: "))
sum = 0
org = n
while n >= 1:
    num = n % 10
    sum = sum + num
    n = n // 10
print("The sum of all the digits of ",org, "is ",sum)
