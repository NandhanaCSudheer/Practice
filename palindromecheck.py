n = int(input("Enter a number: "))
rev = 0
org = n
while n >= 1:
    num = n % 10
    rev = rev * 10 + num
    n = n // 10
if org == rev:
    print(org, "is a palindrome number")
else:
    print(org, "is not a palindrome number")