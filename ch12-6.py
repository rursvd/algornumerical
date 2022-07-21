import numpy as np

A = np.array([[1,3,2],[3,5,1],[2,1,7]])
C = np.array([[100,100,100],[100,100,100],[100,100,100]])

P = A @ C
Q = C @ A
print(f'P = {P}')
print(f'Q = {Q}')
