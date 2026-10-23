n = int(input("Enter a number: "))
n = abs(n)
if n == 0:
    print("The count of ",n, " is 1")
else:
    count = 0
    num = n
    while n >= 1:
        n = n // 10
        count += 1
    print("The number of digits in ",num, " is ",count)
        