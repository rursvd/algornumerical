import numpy as np
import scipy.linalg  
		
A = np.array([[2,1,0],[1,4,-1],[0,-1,7]])
P, L, U = scipy.linalg.lu(A)
		
print(P @ A)
