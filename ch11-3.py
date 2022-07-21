import numpy as np

def f(x):
    return x*np.exp(-x) + 1.0

def df(x):
    return np.exp(-x) - x*np.exp(-x)

N = 5
xold = 0.0

for k in range(N):
    xnew = xold - f(xold)/df(xold)
    print(f'{k+1}, x = {xnew:0.4f}')
    xold = xnew
