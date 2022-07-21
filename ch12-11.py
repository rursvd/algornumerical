import numpy as np

A = np.array([[6,3,2],[3,5,1],[2,1,7]])

invA = np.linalg.inv(A)
print(f'invA = {invA}')

# Verification
print()
print('A A^{-1} = ', A @ invA)
print()
print('A^{-1} A = ', invA @ A)
