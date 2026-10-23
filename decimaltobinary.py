n = int(input("Enter a decimal number: "))
if n == 0:
    print("0")
else:
    b = ""
    while n > 0:
        num = str(n % 2)
        b = num + b
        n = n // 2 
    print(b)