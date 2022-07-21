# Exponential interpolation

import numpy as np
import numpy.linalg 

np.random.seed(2022)

def f(x):
    return x*np.exp(0.2*x)

mu, sigma = 0.0, 0.6
eps = np.random.normal(mu, sigma, 50)

x = np.linspace(1,5,50)
y = f(x) + eps

# Interpolation

X = np.column_stack([np.ones(len(x)),x])
XT = X.T
ylog = np.log(y)

beta = np.linalg.inv(XT @ X) @ (XT @ ylog)
a = np.exp(beta[0])
b = beta[1]

print('a = {a:0.4f}')
print('b = {b:0.4f}')

yhat = np.exp(X @ beta)
