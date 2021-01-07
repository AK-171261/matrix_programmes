'''
Matrix addition and subtraction are element by element operation.
No of row in matrix1 = No of row in matrix2
No of column in matrix1 = No of column in matrix2
m1 = [[10,20], [30,40], m2 = [[1,2],[3,4]]
res = m1+m2
[[11,22],[33,44]]
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


def default(num1, num2):
    return "Incorrect day"


switcher = {
    1: matrix_addition,
    2: matrix_subtraction,
}


def switch(operation, num1, num2):
    return switcher.get(operation, default)(num1, num2)


print('''You can perform operation
1. Addition
2. Subtraction''')

if __name__ == "__main__":
    choice = int(input("Select operation from 1,2 : "))
    row_no = int(input("Enter Row number: "))
    col_no = int(input("Enter Column number: "))
    switch(choice, row_no, col_no)
