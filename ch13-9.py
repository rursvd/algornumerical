# Gaussian elimination method
# Ax = b	
	
import numpy as np

A = np.array([[2,1,0],[1,4,-1],[0,-1,7]])
b = np.array([4,6,19])

C = np.column_stack((A,b))
print(f'C = {C}')

a21a11 = -A[1,0]/A[0,0]
a31a11 = -A[2,0]/A[0,0]
G1 = np.array([[1,0,0],[a21a11,1,0],[0,0,1]])
G2 = np.array([[1,0,0],[0,1,0],[a31a11,0,1]])

D = G2 @ G1 @ C 
d32d22 = -D[2,1]/D[1,1]
G3 = np.array([[1,0,0],[0,1,0],[0,d32d22,1]])

S = G3 @ D
print(f'S = {S}')
print(f'A = {S[:,:-1]}')
print(f'b = {S[:,-1]}')
