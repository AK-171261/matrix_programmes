'''
Matrix addition and subtraction are element by element operation.
No of row in matrix1 = No of row in matrix2
No of column in matrix1 = No of column in matrix2
m1 = [[10,20], [30,40], m2 = [[1,2],[3,4]]
res = m1+m2
[[11,22],[33,44]]
'''
'''
Matrix multiplication is not element by element operation.
No. of column in matrix1 (p*n) = No.of rows in matrix2 (n*q)
result = p*q
Note:
1.Number of rows in matrix1 (p)
2.Number of rows in matrix2 or No.of column in matrix1 (n)
3.Number of column in matrix2 (q)
'''


def matrix_addition(row, column):
    matrix1 = [[int(input("Enter Element for matrix1: ")) for j in range(column)] for i in range(row)]
    print("Matrix1: ")
    for i in range(row):
        for j in range(column):
            print(format(matrix1[i][j], "<5"), end=" ")
        print()

    matrix2 = [[int(input("Enter the element for matrix2: ")) for i in range(column)] for j in range(row)]
    print("Matrix2: ")
    for i in range(row):
        for j in range(column):
            print(format(matrix2[i][j], "<5"), end=" ")
        print()

    res = [[0 for j in range(column)] for i in range(row)]
    for i in range(row):
        for j in range(column):
            res[i][j] = matrix1[i][j] + matrix2[i][j]

    print("Addition result: ")
    for i in range(row):
        for j in range(column):
            print(format(res[i][j], "<5"), end=" ")
        print()


def matrix_subtraction(row, column):
    matrix1 = []
    for i in range(row):
        temp_lst = list()
        for j in range(column):
            temp_lst.append(int(input("Enter element for Matrix1: ")))
        matrix1.append(temp_lst)

    print("Matrix1: ")
    for i in range(row):
        for j in range(column):
            print(format(matrix1[i][j], "<5"), end=" ")
        print()

    matrix2 = list()
    for i in range(row):
        temp_lst = list()
        for j in range(column):
            temp_lst.append(int(input("Enter element for Matrix2: ")))
        matrix2.append(temp_lst)

    print("matrix2: ")
    for i in range(row):
        for j in range(column):
            print(format(matrix2[i][j], "<5"), end=" ")
        print()

    result = list()
    for i in range(row):
        temp_lst = list()
        for j in range(column):
            temp_lst.append(0)
        result.append(temp_lst)

    for i in range(row):
        for j in range(column):
            result[i][j] = matrix1[i][j] - matrix2[i][j]
    print("Subtraction result: ")
    for i in range(row):
        for j in range(column):
            print(format(result[i][j], "<5"), end=" ")
        print()


def matrix_multiplication(num1, num2, num3):
    matrix1 = [[int(input("Enter values for matrix1: ")) for j in range(num2)] for i in range(num1)]
    print("matrix1: ")
    for i in matrix1:
        for j in range(len(i)):
            print(format(i[j], "<5"), end=" ")
        print()
    matrix2 = [[int(input("Enter values for matrix2: ")) for j in range(num3)] for i in range(num2)]
    print("matrix2: ")
    for i in matrix2:
        for j in range(len(i)):
            print(format(i[j], "<5"), end=" ")
        print()
    res = [[int(0) for j in range(num3)] for i in range(num1)]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                res[i][j] = res[i][j] + matrix1[i][k] * matrix2[k][j]
    for i in res:
        for j in i:
            print(format(j, "<3"), end=" ")
        print()


def default(num1, num2):
    return "Incorrect operation"


switcher = {
    1: matrix_addition,
    2: matrix_subtraction,
    3: matrix_multiplication,
}


def switch(operation, num1, num2, num3):
    if operation == 1 or operation == 2:
        return switcher.get(operation, default)(num1, num2)
    if operation == 3:
        return switcher.get(operation, default)(num1, num2, num3)


print('''You can perform operation
1. Addition
2. Subtraction
3. Multiplication''')

if __name__ == "__main__":
    choice = int(input("Select operation from 1,2,3: "))
    if choice == 1 or choice == 2:
        row_no = int(input("Enter Row number: "))
        col_no = int(input("Enter Column number: "))
        switch(choice, row_no, col_no)
    elif choice == 3:
        p = int(input("Enter Row number for matrix1: "))
        q = int(input("Enter Column number for matrix1 and Row for matrix2: "))
        n = int(input("Enter Column number for matrix2: "))
        switch(choice, p, q, n)
