import numpy as np

def myRowEchelon3(A):
    #First Step
    preformRowOperation(A, 0)

    #Second Step
    preformRowOperation(A, 1)

    return A

def preformRowOperation(A, currentRow):
    nrows = A.shape[0]
    for row in range(nrows):
        if(row > currentRow):
            A[row] -= A[row, currentRow] / A[currentRow, currentRow] * A[currentRow]


U = myRowEchelon3(np.array([[2., -1. , 1.],[-2., 3., -1.],[4., -15., 7.]]))
print(np.allclose(U,np.array([[2., -1., 1.],[0., 2., 0.],[0., 0., 5.]])))