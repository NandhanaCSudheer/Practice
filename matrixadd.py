r1 = int(input("Enter the no.of rows of first matrix: "))
c1 = int(input("Enter the no.of columns of first matrix: "))
r2 = int(input("Enter the no.of rows of second matrix: "))
c2 = int(input("Enter the no.of columns of second matrix: "))
print()
   
if r1 != r2 or c1 != c2:
    print("The row and column number should be same!!!")
else:
    m1 = [[0] * c1 for i in range(r1)]
    m2 = [[0] * c2 for i in range(r2)]
    m = [[0] * c1 for i in range(r1)]

    print("Enter the elements of the first matrix: ")
    for i in range(r1):
        for j in range(c1):
            m1[i][j] = int(input("Enter the element: "))

    print()        
    print("Enter the elements of the second matrix: ")
    for i in range(r2):
        for j in range(c2):
            m2[i][j] = int(input("Enter the element: "))

    print("The first matrix is: ")
    for i in range(r1):
        for j in range(c1):
         print(m1[i][j],end = "\t")
        print()

    print()
    print("The second matrix is: ")
    for i in range(r2):
        for j in range(c2):
            print(m2[i][j],end = "\t")
        print()
    print()

    print("The matrix after addition is: ")
    for i in range(r1):
        for j in range(c1):
            m[i][j] = m1[i][j] + m2[i][j]
    for i in range(0,r1):
        for j in range(0,c1):
            print(m[i][j],end = "\t")
        print()