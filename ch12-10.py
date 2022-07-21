import numpy as np

A = np.array([[6,3,2],[3,5,1],[2,1,7]])
detA = np.linalg.det(A)

print(f'detA = {detA:0.4f}')
