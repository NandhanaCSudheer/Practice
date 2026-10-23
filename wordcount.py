s = input("Enter a sentence: ")
w = s.split()
count = 0
print(w)
for i in w:
    count = count + 1
print("The number of words in ",s, " is ",count)

#   count = len(s.split())