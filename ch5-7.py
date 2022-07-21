import numpy as np
		
x = np.array([1,2,3,4,5])
		
hap = 0
for i in range(1,5):
    hap = hap + x[i]
print(f'hap = {hap}')
