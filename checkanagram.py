s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
s = sorted(s1.lower())
t = sorted(s2.lower())
if s == t:
    print(s1, " and ",s2, " are anagrams")
else:
    print(s1, " and ",s2, " are not anagrams")

"""
if len(s1) != len(s2):
    print(s1, " and ",s2, " are not anagrams")
else:
    a = 0
    s1 = s1.lower()
    s2 = s2.lower()
    for i in s1:
        if s1.count(i) != s2.count(i):
            a = 1
            break
    if a == 1:
        print(s1, " and ",s2, " are not anagrams")
    else:
        print(s1, " and ",s2, " are anagrams")
        
"""