import numpy as np 
import scipy.linalg 

A = np.array([[2,1,0],[1,4,-1],[0,-1,7]])
b = np.array([4,6,19])

L = scipy.linalg.cholesky(A, lower=True)
LT = L.T
invLT = np.linalg.inv(LT)
invL = np.linalg.inv(L)

x = invLT @ (invL @ b)
print(f'x = {x}')
