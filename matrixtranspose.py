r = int(input("Enter the no.of rows of the matrix: "))
c = int(input("Enter the no.of columns of the matrix: "))

m = [[0]*c for i in range(r)]
t = [[0]*r for i in range(c)]
print()

for i in range(r):
    for j in range(c):
        m[i][j]  = int(input("Enter the elements: ")) 

print("The original matrix is: ")
for i in range(r):
    for j in range(c):
        print(m[i][j],end = "\t")
    print()

print()
print("The transpose of the matrix is: ")
for i in range(r):
    for j in range(c):
        t[j][i] = m[i][j]
for i in range(c):
    for j in range(r):
        print(t[i][j],end = "\t")
    print()