import numpy as np
import scipy.linalg 
	
A = np.array([[2,1,0],[1,4,-1],[0,-1,7]])
b = np.array([4,6,19])

P, L, U = scipy.linalg.lu(A)
invL = np.linalg.inv(L)
invU = np.linalg.inv(U)

x = invU @ (invL @ b)
print(f'x = {x}')
