import numpy as np
import numpy.linalg 

np.random.seed(2022)

def f(x):
    return x*np.exp(-x)

mu, sigma = 0.0, 0.04
eps = np.random.normal(mu, sigma, 50)

x = np.linspace(0,1,50)
y = f(x) + eps
xsq = x**2 # x^2

X = np.column_stack([np.ones(len(x)),x,xsq])
XT = X.T

beta = np.linalg.inv(XT @ X) @ (XT @ y)
print('beta = ',beta)

yhat = X @ beta
