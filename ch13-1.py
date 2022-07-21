import numpy as np

A = np.array([[2,-1],[-1,1]])
b = np.array([1,1])

Ap = np.array([[1,1],[1,2]])
detA = np.linalg.det(A)
invA = Ap/detA

x = invA @ b 
print(f'x = {x}')
