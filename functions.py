def InputMatrix(R,C):
    matrix = []
    print("Enter the entries rowwise:")
  
    # For user input
    for i in range(R):          # A for loop for row entries
        a =[]
        for j in range(C):      # A for loop for column entries
             a.append(int(input()))
        matrix.append(a)
  
    return matrix

def GaussJordan(matrix):
    
    return

def ScalarMultiplication(matrix,scalar,R,C):
    matrixNew = []
    for i in range(R):
        a=[]
        for j in range(C):
            a.append(matrix[i][j]*scalar)
        matrixNew.append(a)
    
    return matrixNew

def MatrixMultiplication(matrix1,matrix2,row1,row2,column1,column2):
    matrixNew = []
    for i in range(row1):
        a=[]
        for j in range(column2):
            a.append(0)
        matrixNew.append(a)

    # iterate through rows of matrix 1
    for i in range(len(matrix1)):
    #iterate through columns of Y
        for j in range(len(matrix2[0])):
    #iterate through rows of Y
            for k in range(len(matrix2)):
                matrixNew[i][j] += matrix1[i][k] * matrix2[k][j]

    return matrixNew

def Transpose(matrix,row,column):
    matrixNew = []
    for i in range(column):
        a=[]
        for j in range(row):
            a.append(0)
        matrixNew.append(a)
    
    for i in range (row):
        for j in range (column):
            matrixNew[j][i] = matrix[i][j]

    return matrixNew

def Addition(matrix1,matrix2,row,column):
    matrixNew = []
    for i in range(row):
        a=[]
        for j in range(column):
            a.append(0)
        matrixNew.append(a)

    for i in range(row):
        for j in range (column):
            matrixNew[i][j] = matrix1[i][j] + matrix2[i][j]

    return matrixNew

def Subtraction(matrix1,matrix2,row,column):
    matrixNew = []
    for i in range(row):
        a=[]
        for j in range(column):
            a.append(0)
        matrixNew.append(a)

    for i in range(row):
        for j in range (column):
            matrixNew[i][j] = matrix1[i][j] - matrix2[i][j]

    return matrixNew

#To be made
def MatrixInverse():

    return

#To be made
def MatrixDeterminant():

    return
