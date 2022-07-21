import numpy as np

A = np.array([[2,-1],[-1,1]])
b = np.array([1,1])

invA = np.linalg.inv(A)

x = invA @ b 
print(f'x = {x}')
