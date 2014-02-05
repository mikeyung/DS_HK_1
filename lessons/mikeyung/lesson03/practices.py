from numpy import array, dot
from numpy.linalg import inv

X = array([[1, 1], [1, 2], [1, 3], [1, 4]])
y = array([[1], [2], [3], [4]])

# X.T means transpose X
# inv is inverse
# dot is dot product

n = inv(dot(X.T, X))
k = dot(X.T, y)
coef_ = dot(n, k)

print "====="
print "X:", X
print "y:", y
print "n:", n
print "k:", k
print "coef_:", coef_

def regression(input, response):
    return dot(inv(dot(input.T, input)), dot(input.T, response))

print "====="
from numpy import *
arrayOne = arange(15).reshape(3, 5)
arrayTwo = arange(15).reshape(5, 3)
vector = array([10, 15, 20])
print "arrayOne:", (arrayOne)
print "arrayTwo:", (arrayTwo)
print "vector:", (vector)

print "====="
matrixOne = matrix('1 2 3; 4 5 6')
matrixTwo = matrix('1 2; 3 4; 5 6')

print "matrixOne:", matrixOne
print "matrixTwo:", matrixTwo

print "====="
a1 = array([ [1, 2], [3, 4] ])
a2 = array([ [1, 3], [2, 4] ])
m1 = matrix('1 2; 3 4')
m2 = matrix('1 3; 2 4')
print "a1:", a1
print "a2:", a2
print "m1:", m1
print "m2:", m2

# array multiplication is element multiplication
# where matrix multiplication is linear multiplication

print "a1 * a2:", a1 * a2
print "m1 * m2:", m1 * m2

# Looks like the dot() make the array and matrix multiplication the same ?

print "====="
print "dot(a1,a2)", dot(a1,a2)
print "dot(m1,m2)", dot(m1,m2)

print "====="

# .T Transposes the array or matrix:
print "a1.T", a1.T
# .I returns the matrix inverse:
# matrix multipy by it's own inverse will become an Identity matrix
print "m1.I", m1.I
# eye(value) creates an identity matrix:
iFive = eye(5)
print "iFive:", iFive
