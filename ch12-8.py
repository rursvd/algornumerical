import numpy as np	
	
x = np.array([1,2])
A = np.array([[30,40],[50,60]])

# case 1: Ax
ax = A @ x
print(f'Ax = {ax}')

# case 2: xTA
xa = x.T @ A
print(f'xTA = {xa}')
