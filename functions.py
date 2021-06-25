import numpy as np
import sys

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

def GaussJordan(n):
    a = np.zeros((n,n+1))
    x = np.zeros(n)
    print('Enter Augmented Matrix Coefficients:')
    for i in range(n):
        for j in range(n+1):
            a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))
    
    for i in range(n):
        if a[i][i] == 0.0:
            sys.exit('Divide by zero detected!')
         
        for j in range(i+1, n):
            ratio = a[j][i]/a[i][i]
         
            for k in range(n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]
 
    x[n-1] = a[n-1][n]/a[n-1][n-1]
 
    for i in range(n-2,-1,-1):
        x[i] = a[i][n]
     
        for j in range(i+1,n):
            x[i] = x[i] - a[i][j]*x[j]
     
        x[i] = x[i]/a[i][i]
    print("The matrix in REF is:")
    print(a)

    print('\nThe solution is: ')
    for i in range(n):
        print('X%d = %0.2f' %(i,x[i]), end = '\t')
    

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
