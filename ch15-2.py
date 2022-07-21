import numpy as np
import numpy.linalg

XT = np.array([[1,1,1,1,1],[1,2,3,4,5]])
X = XT.T
y = np.array([8.5,7.7,6.9,4.5,2])

beta = np.linalg.inv(XT @ X)@(XT @ y)

print(f'beta0 = {beta[0]:0.2f}')
print(f'beta1 = {beta[1]:0.2f}')

yhat = X @ beta
print(f'yhat = {yhat}')
