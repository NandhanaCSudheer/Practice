s = input("Enter a string: ")
rev = ""
for i in s[-1::-1]:
    rev = rev + i
print(rev)

"""
s = input("Enter a string: ")
rev = ''.join(reversed(s))
print(rev)

"""