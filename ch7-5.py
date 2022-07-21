import numpy as np	
	
A = np.array([[5,6],[9,7],[3,5],[1,2]])

b1, b2 = np.sum(A,axis=0)
print(f'b1 = {b1}')
print(f'b2 = {b2}')

c1, c2 = np.average(A,axis=0)
print(f'c1 = {c1}')
print(f'c2 = {c2}')
