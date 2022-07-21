import numpy as np

def f(x):
    return x*np.exp(-x) + 1.0

N = 8
xold = 0.0 
xmid = 0.3 

for k in range(N):
    xnew = xmid - (f(xmid) * (xmid - xold))/(f(xmid) - f(xold))
    xold = xmid
    xmid = xnew 
    print(f'{k+1}, x = {xnew:0.4f}')
