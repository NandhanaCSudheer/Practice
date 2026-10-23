s = input("Enter a string: ")

rev = ""
for i in s[-1::-1]:
    rev += i

if s == s[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not palindrome")

