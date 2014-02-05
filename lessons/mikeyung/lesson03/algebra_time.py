#!/usr/bin/python

"""
Lesson 2 - Class work

Michael Yung
2014-01-29

"""

"""

Class Examples

Matrix Multiplication

"""

a_matrix = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ]
b_matrix = [ [1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4] ]

print "==================="
print "Class Execises - Matrix Multiplication"

import timeit as t
from numpy import array, dot

def matrixMultiplication(matrix1, matrix2):

#	print "       First Matrix :", matrix1
#	print "      Second Matrix :", matrix2

	rows_A = len(matrix1)
	cols_A = len(matrix1[0])
	rows_B = len(matrix2)
	cols_B = len(matrix2[0])

	if cols_A != rows_B:
		print "Cannot multiply the two matrices. Incorrect dimensions."
 		return
# 	else:
#		print " Output matrix size :", rows_A, cols_B

    # Create and initialize the result matrix
    
	matrix3 = [[0 for row in range(cols_B)] for col in range(rows_A)]
#	print " Matrix initialized :", matrix3

	for i in range(rows_A):
		for j in range(cols_B):
			for k in range(cols_A):
				matrix3[i][j] = matrix3[i][j] + matrix1[i][k]*matrix2[k][j]

#	print "      Output Matrix :"
	return matrix3

print matrixMultiplication(a_matrix, b_matrix)
print "Dot() :", dot(a_matrix, b_matrix)

print "Run dot() 100000 times"
print t.timeit('dot(a_matrix, b_matrix)', setup="from __main__ import dot, a_matrix, b_matrix", number = 100000)

print "Run matrixMultiplication 100000 times"
print t.timeit('matrixMultiplication(a_matrix, b_matrix)', setup="from __main__ import matrixMultiplication, a_matrix, b_matrix", number = 100000)


c_matrix = array([ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ])
d_matrix = array([ [1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4] ])

print "Run dot() 100000 times for the second time"
print t.timeit('dot(c_matrix, d_matrix)', setup="from __main__ import dot, c_matrix, d_matrix", number = 100000)
