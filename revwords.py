s = input("Enter a sentence: ")
r = ""
l = s.split()
for i in range(len(l)-1,-1,-1):
    r += l[i]
    r += " "
print("The reversed sentence is: ",r)

#   r = " ".join(l[::-1])