import numpy as np
import rowEchelon as re

def myLU3(A):
    """ Takes a 3x3 numpy array and computes its
    LU decomposition without partial pivoting
    and assuming that no row swaps are required. """
    U = np.copy(A)
    U = re.rowEchelon(U)

    L = np.zeros_like(A)
    nrows = L.shape[0]
    ncolumns = L.shape[1]
    for row in range(nrows):
        for column in range(row, ncolumns):
            if(row == column):
                L[row, column] = 1
            else:
                sum_L = 0
                for offDiagonal in range(row):
                    sum_L += L[column, offDiagonal] * U[offDiagonal, row]
                L[column, row] = (A[column, row] - sum_L) / U[row, row]

    return L, U
    

A = np.array([[1.,2.,-1.],[-2.,-5.,3.],[-1.,-3.,0.]])
L, U = myLU3(A)
print(f"Is L in the correct form? {np.allclose(np.triu(L),np.eye(3))}")
print(f"Is U in the correct form? {np.allclose(U,np.triu(U))}")
print(f"Do L and U multiply to A? {np.allclose(L @ U, A)}")