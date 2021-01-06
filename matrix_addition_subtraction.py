'''
Matrix addition and subtraction are element by element operation.
No of row in matrix1 = No of row in matrix2
No of column in matrix1 = No of column in matrix2
m1 = [[10,20], [30,40], m2 = [[1,2],[3,4]]
res = m1+m2
[[11,22],[33,44]]
'''


def matrix_addition(row, column):
    matrix1 = [[int(input("Enter Element for matrix1: ")) for j in range(col)] for i in range(row)]
    print("Matrix1: ")
    for i in range(row):
        for j in range(col):
            print(format(matrix1[i][j], "<5"), end=" ")
        print()

    matrix2 = [[int(input("Enter the element for matrix2: ")) for i in range(col)] for j in range(row)]
    print("Matrix2: ")
    for i in range(row):
        for j in range(col):
            print(format(matrix2[i][j], "<5"), end=" ")
        print()

    res = [[0 for j in range(col)] for i in range(row)]
    for i in range(row):
        for j in range(col):
            res[i][j] = matrix1[i][j] + matrix2[i][j]

    print("Addition result: ")
    for i in range(row):
        for j in range(col):
            print(format(res[i][j], "<5"), end=" ")
        print()


row = int(input("Enter the matrix row Number: "))
col = int(input("Enter the matrix column Number: "))
matrix_addition(row, col)