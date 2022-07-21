import numpy as np 
import scipy.linalg  

A = np.array([[2,1,0],[1,4,-1],[0,-1,7]])

P, L, U = scipy.linalg.lu(A)

print(f'A = {A} \n')
print(f'L = {L} \n')
print(f'U = {U} \n')

print(f'P = {P}')
