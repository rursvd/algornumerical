import numpy as np
import scipy.linalg  

A = np.array([[2,1,0],[1,4,-1],[0,-1,7]])
b = np.array([4,6,19])

P, L, U = scipy.linalg.lu(A)

print(L @ U)
