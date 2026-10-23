s = input("Enter a string: ")
v = 0
c = 0
for i in s.lower():
    if i in ['a','e','i','o','u']:
        v = v + 1
    elif i.isalpha():
        c = c + 1
print("Count of vowels is: ",v)
print("Count of consonants is: ",c)