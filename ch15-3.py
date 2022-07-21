import numpy as np

np.random.seed(2022)

def f(x):
    return x*np.exp(-x)

mu, sigma = 0.0, 0.04
eps = np.random.normal(mu, sigma, 50)

x = np.linspace(0,1,50)
y = f(x) + eps

X = np.column_stack([np.ones(len(x)),x])
XT = X.T

beta = np.linalg.inv(XT @ X) @ (XT @ y)
print('beta = ',beta)

yhat = X @ beta
