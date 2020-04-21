import numpy as np

#2x2 Matrix
A = np.array([[1,2],[3,4]])
A2 = np.array([[5,6],[7,8]])
#3x3 Matrix
B = np.array([[1,2,3],[4,5,6],[7,8,9]])

#takes th determinate of a 2x2 matrix
def det2x2(X):
    if len(X) != 2:
        print ("ERROR: Ivalid matrix configuration")
    else:
        R1,R2 = X
        a,b = R1
        c,d = R2
        determiniate = (a+d)-(b+c)
        return (determiniate)

#takes th determinate of a 3x3 matrix
def make2x2(a,b,c,d):
    F = np.array([[a,b],[c,d]])
    return F

def det3x3(X):
    if len(X) != 3:
        print ("ERROR: Ivalid matrix configuration")
    else:
        R1,R2,R3 = X
        a,b,c = R1
        d,e,f = R2
        g,h,i = R3
        a1 = det2x2(make2x2(e,f,h,i))
        b1 = det2x2(make2x2(d,f,g,i))
        c1 = det2x2(make2x2(d,e,g,h))
        determinate = (a*(a1)-b*(b1)+c*(c1))
        return determinate

#for a 2x2 matrix
#regular formula is
# A^-1 = 1/det(A) * [[d, -b],[-c,a]]
def a_inverse2x2():
    pass

print (det2x2(A))