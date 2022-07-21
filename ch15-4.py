import numpy as np
import numpy.linalg	
	
x = np.array([1,2,3,4,5])
y = np.array([8.5,7.7,6.9,4.5,2])
xsq = x**2 # x^2

X = np.column_stack([np.ones(len(x)),x,xsq])
XT = X.T

beta = np.linalg.inv(XT @ X) @ (XT @ y)

print(f'beta0 = {beta[0]:0.2f}')
print(f'beta1 = {beta[1]:0.2f}')
print(f'beta2 = {beta[2]:0.2f}')

yhat = X @ beta
print(yhat)
