import numpy as np

def rowEchelon(A):
    """Takes a matrix and uses Gaussian
	elimination to find its row echelon form."""

    rows = len(A[0])
    for row in range(rows):
        preformRowOperation(A, row)

    return A

def preformRowOperation(A, currentRow):
    nrows = A.shape[0]
    for row in range(nrows):
        if(row > currentRow):
            A[row] -= A[row, currentRow] / A[currentRow, currentRow] * A[currentRow]