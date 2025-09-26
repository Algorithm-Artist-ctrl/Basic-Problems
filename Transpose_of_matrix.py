import numpy as np 
def matrix():
    matrix1 = []
    row = int(input("Enter number of rows:\n"))
    col = int(input("Enter number of columns:\n"))
    for i in range(row):
        a = []
        for j in range(col):
            num = int(input(f"Enter number for position [{i+1}][{j+1}]:\n"))
            a.append(num)
        matrix1.append(a)
    arr = np.array(matrix1)
    print("The resulting matrix is:")
    print(arr)
    transpose = arr.T
    print("The transpose of the matrix is:")
    print(transpose)
matrix()