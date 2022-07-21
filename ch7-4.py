import numpy as np	
	
A = np.array([[5,6],[9,7],[3,5],[1,2]])

a13, a23, a33, a43 = np.sum(A,axis=1)
print(a13,a23,a33,a43)
