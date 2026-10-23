s = input("Enter a string: ")
substr = input("Enter the substring: ")
if substr in s:
    print("Substring is present")
else:
    print("Substring not present")

    """
    s = input("Enter a string: ")
substr = input("Enter the substring: ")

found = False

for i in range(len(s) - len(substr) + 1):
    if s[i:i + len(substr)] == substr:
        found = True
        break

if found:
    print("Substring is present")
else:
    print("Substring not present")
    
    """