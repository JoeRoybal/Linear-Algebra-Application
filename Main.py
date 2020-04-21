import numpy as np

#2x2 Matrix
A = np.array([[1,2],[3,4]])
A2 = np.array([[5,6],[7,8]])
#3x3 Matrix
B = np.array([[1,2,3],[4,5,6],[7,8,9]])

#takes th determinate of a 2x2 matrix
def det2x2(X):
    R1,R2 = X
    a,b = R1
    c,d = R2
    determiniate = (a+d)-(b+c)
    print (determiniate)


#for a 2x2 matrix
#regular formula is
# A^-1 = 1/det(A) * [[d, -b],[-c,a]]
def a_inverse2x2():
    pass

det2x2(A)