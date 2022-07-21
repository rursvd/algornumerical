import numpy as np	
		
x = np.array([1, 2])
beta = np.array([-1, 3])
		
y1 = x @ beta
y2 = beta @ x

print(f'y1 = {y1}')	
print(f'y2 = {y2}')
