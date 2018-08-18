import numpy as np
import cmath

A = np.array([[1,3,6],[2,5,7],[12,535,755]])

rows = A.shape[0]
cols = A.shape[1]
M = range(rows)
M = np.reshape(M,(rows,1))
N = range(cols)
N = np.reshape(N,(cols,1))


mat_U = np.tile(M,(cols))
mat_V = np.tile(N,(rows)).transpose()

mat_dft2 = np.zeros((rows,cols))

mat_dft = np.zeros((rows,cols))
phase = np.zeros((rows,cols))
i=0
U = np.pi*2*mat_U*1j
V = np.pi*2*mat_V*1j

for x in range(rows):
    for y in range(cols):
        
        exp_mat = (np.exp(-U*x-V*y)*A).sum()
        mat_dft2[x][y] = np.abs(exp_mat)
print(mat_dft2)