#!/usr/bin/python

"""
Lesson 2 - Class work

Michael Yung
2014-01-29

"""

"""

Class Examples

"""

vector = [1,2,3]

matrix = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ]

#
# Multiply the original value in the vector by value
#

def vectorMultiply(vector, value):
	return [x*value for x in vector]

#
# len(matrix[0]) get the size of the vector in the matrix
# create a range to loop through the each of the item in vector
# 

def matrixTranspose(matrix):
     return [ [row[i] for row in matrix] for i in range(len(matrix[0]))]

print "==================="
print "Class Examples"
print "          Vector :", vector
print "          Matrix :", matrix
print " Multiply Vector :", vectorMultiply(vector, 3)
print "Transpose Matrix :", matrixTranspose(matrix)

"""

Class Execises

Vector Matrix Multiplication

"""
vector = [1,2,3]

matrix = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ]

print "==================="
print "Class Execises - Vector Matrix Multiplication"
print "           Vector :", vector
print "           Matrix :", matrix

def vectormatrixMultiplication(vector, matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			matrix[i][j] = matrix[i][j] * vector[i]
	return matrix

print "VM Multiplication :", vectormatrixMultiplication(vector, matrix)

"""

Matrix Multiplication

"""

a_matrix = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ]

b_matrix = [ [1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4] ]

print "==================="
print "Class Execises - Matrix Multiplication"

def matrixMultiplication(matrix1, matrix2):

	print "       First Matrix :", matrix1
	print "      Second Matrix :", matrix2

	rows_A = len(matrix1)
	cols_A = len(matrix1[0])
	rows_B = len(matrix2)
	cols_B = len(matrix2[0])

	if cols_A != rows_B:
		print "Cannot multiply the two matrices. Incorrect dimensions."
 		return
 	else:
 		print " Output matrix size :", rows_A, cols_B

    # Create and initialize the result matrix
    
	matrix3 = [[0 for row in range(cols_B)] for col in range(rows_A)]
	print " Matrix initialized :", matrix3

	for i in range(rows_A):
		for j in range(cols_B):
			for k in range(cols_A):
				matrix3[i][j] = matrix3[i][j] + matrix1[i][k]*matrix2[k][j]

	print "      Output Matrix :"
	return matrix3

print matrixMultiplication(a_matrix, b_matrix)

"""

Identity Matrix exercises - 

An identity matrix is a matrix where value = 1 
if the row and column index are the same, and 0 otherwise. 
It should build any size identity matrix you want.

"""

def iMatrix(num):

	print "==================="
	print "Class Execises - Identity Matrix"

	matrix = [[0 for row in range(num)] for col in range(num)]
	print "    Input Parameter :", num
	print " Matrix initialized :", matrix

	for row in range(num):
		for col in range(num):
			if row == col:
				matrix[col][row] = 1

	print "      Output Matrix :"
	return matrix

print iMatrix(4)
