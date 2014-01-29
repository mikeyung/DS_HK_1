#!/usr/bin/python

"""
Lesson 2 - Class work

Michael Yung
2014-01-29

"""

print "Class Examples"

vector = [1,2,3]

matrix = [ [1, 2, 3, 4], 
  [5, 6, 7, 8],
  [9, 10, 11, 12] ]

print "          Vector :", vector
print "          Matrix :", matrix

#
# Multiply the original value in the vector by value
#

def vectorMultiply(vector, value):
	return [x*value for x in vector]

print " Multiply Vector :", vectorMultiply(vector, 3)

#
# len(matrix[0]) get the size of the vector in the matrix
# create a range to loop through the each of the item in vector
# 

def matrixTranspose(matrix):
     return [ [row[i] for row in matrix] for i in range(len(matrix[0]))]

print "Transpose Matrix :", matrixTranspose(matrix)

print "====="
print "Class Execises"
print "           Vector :", vector
print "           Matrix :", matrix

def vectormatrixMultiplication(vector, matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			matrix[i][j] = matrix[i][j] * vector[i]
	return matrix

print "VM Multiplication :", vectormatrixMultiplication(vector, matrix)
print "======"

matrix = [ [1, 2, 3, 4], 
  [5, 6, 7, 8],
  [9, 10, 11, 12] ]

another_matrix = [ [1, 1, 1, 1], 
  [2, 2, 2, 2],
  [3, 3, 3, 3] ]

print "====="
print "Class Execises"
print "           Matrix :", matrix
print "   Another Matrix :", another_matrix

def matrixMultiplication(matrix1, matrix2):
	for i in range (len(matrix1)):
		for j in range(len(matrix1[0])):
			matrix3[i][j] = matrx1[i][j] * matrix2[i][j] 
	return matrix3

print "MM Multiplication :", matrixMultiplication(matrix, another_matrix)

