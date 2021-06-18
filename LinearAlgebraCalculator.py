from functions import *

def main():
  keepUsing = ""
  while (keepUsing != "N"):
      print("HELLO, WELCOME TO THE LINEAR ALGEBRA MATRIX CALCULATOR. THE PROJECT IS CURRENTLY QUARANTINE/DEVELOPMENT")
      print("What would you like to do today\n")
  
      print("A.Gauss jordan elimination for RREF")
      print("B.Scalar matrix multiplication")
      print("C.Matrix matrix multiplication")
      print("D.Matrix transpose")
  
      choice = input("")
      choice = choice.upper()
  
      if (choice == "A"):
          print("lorem ipsum")
    
      if (choice == "B"):
           #Input rows and columns
           Rows = int(input("Enter the number of rows:"))
           Columns = int(input("Enter the number of columns:"))
           #input the matrix and the scalar value
           matrix = InputMatrix(Rows,Columns)
           scalar = int(input("Enter the scalar you wish to multiply the matrix by:\n"))
       
           # For printing the matrix
           print("")
           for i in range(Rows):
              for j in range(Columns):
                   print(matrix[i][j], end = " ")
              print()
       
              #printing the rest
           print("Your matrix in array form is{}:".format(matrix))
           print("Your matrix has {} rows and {} columns".format(Rows,Columns))
           print("Your scalar multiplication value is {}".format(scalar))
      
           #performing the actual calculation
           print("Performing multiplication now:\n")
           x = ScalarMultiplication(matrix,scalar,Rows,Columns)

           #print the new array
           for i in range(Rows):
              for j in range(Columns):
                   print(x[i][j], end = " ")
              print()
           print("Your new matrix in array form is{}:".format(x))
       

      if (choice == "C"):
          #check for validity and do the bulk of this part
               
               #Input rows and columns for matrix 1
               Row1 = int(input("Enter the number of rows:"))
               Column1 = int(input("Enter the number of columns:"))
               Matrix1 = InputMatrix(Row1,Column1)

               #Input rows and columns for matrix 2
               Row2= int(input("Enter the number of rows:"))
               Column2 = int(input("Enter the number of columns:"))
               Matrix2 = InputMatrix(Row2,Column2)
               
               if (Column1 != Row2):
                    print("Invalid calculation, m X n matrix 1 and n X p matrix 2 must have the same n value. I;e 2x3 times 3x4")
               
               else:
                   #just showing the user what they have
                   print("matrix 1 in matrix mode is:\n")
                   for i in range(Row1):
                      for j in range(Column1):
                           print(Matrix1[i][j], end = " ")
                      print()
                   print("matrix 1 in array mode is:\n{}".format(Matrix1))
                   print("matrix 1 has {} rows and {} columns".format(Row1,Column1))
                   print("")
                   
                   print("matrix 2 in matrix mode is:\n")
                   for i in range(Row2):
                      for j in range(Column2):
                           print(Matrix2[i][j], end = " ")
                      print()
                   print("matrix 2 in array mode is:\n{}".format(Matrix2))
                   print("matrix 2 has {} rows and {} columns".format(Row2,Column2))
                   print("")

                   #doing the calculation now
                   x = MatrixMultiplication(Matrix1,Matrix2,Row1,Row2,Column1,Column2)
                   print("matrix x in matrix mode is:\n")
                   for i in range(Row1):
                      for j in range(Column2):
                           print(x[i][j], end = " ")
                      print()
                   print("matrix x in array mode is:\n{}".format(x))
                   print("matrix x has {} rows and {} columns".format(Row1,Column2))
                   print("")

      if (choice == "D"):
           #input the matrix
           Rows = int(input("Enter the number of rows:"))
           Columns = int(input("Enter the number of columns:"))
           matrix = InputMatrix(Rows,Columns)

           #show the user what they have so far
           print("your matrix in matrix mode is:\n")
           for i in range(Rows):
               for j in range(Columns):
                    print(matrix[i][j], end = " ")
               print()
           print("matrix in array mode is:\n{}".format(matrix))
           print("matrix x has {} rows and {} columns".format(Rows,Columns))
          
           #performing the actual calculation
           transpose = Transpose(matrix,Rows,Columns)
           print("your transpose in matrix mode is:\n")
           for i in range(Columns):
               for j in range(Rows):
                    print(transpose[i][j], end = " ")
               print()
           print("matrix in array mode is:\n{}".format(transpose))
           print("matrix x has {} rows and {} columns".format(Columns,Rows))



      else:
          print("{} is not a valid input, please select one of the following options by typing the corresponding letter".format(choice))
      
      keepUsing = input("Would you like to keep going Y/N:")
      keepUsing = keepUsing.upper()
     
  print("Thank you for using!")  

if __name__ == "__main__":
    main()
