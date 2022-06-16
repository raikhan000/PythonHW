import numpy as np

def det4(matrix):
    A = matrix.copy()
    B = matrix.copy()
    C = matrix.copy()
    D = matrix.copy()
    A = np.delete(A, 0, 0)
    A = np.delete(A, 0, 1)
    B = np.delete(B, 0, 0)
    B = np.delete(B, 1, 1)
    C = np.delete(C, 0, 0)
    C = np.delete(C, 2, 1)
    D = np.delete(D, 0, 0)
    D = np.delete(D, 3, 1)
    def det3(matrix2):
        a = matrix2[0][0]*matrix2[1][1]*matrix2[2][2] + matrix2[2][0]*matrix2[0][1]* matrix2[1][2] + matrix2[1][0]*matrix2[2][1]*matrix2[0][2]
        b = matrix2[2][0]*matrix2[1][1]*matrix2[0][2] + matrix2[0][0]*matrix2[2][1]* matrix2[1][2] + matrix2[1][0]*matrix2[0][1]*matrix2[2][2]
        return a - b
    return matrix[0][0]*det3(A) - matrix[0][1]*det3(B) + matrix[0][2]*det3(C) -matrix[0][3]*det3(D)


lmatrix = eval(input())
matrix = np.array(lmatrix)

print(det4(matrix))

