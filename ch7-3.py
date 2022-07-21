# Example 	
import numpy as np

A = np.array([[5,6],[9,7],[3,5],[1,2]])

b1 = np.sum(A[:,0])
b2 = np.sum(A[:,1])
print(f'b1 = {b1}')
print(f'b2 = {b2}')

c1 = np.average(A[:,0])
c2 = np.average(A[:,1])
print(f'c1 = {c1}')
print(f'c2 = {c2}')
