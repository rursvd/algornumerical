import numpy as np

def f(x):
    return x*np.exp(-x) + 1.0	
	
N = 10	
a = -1.0
b = 1.0 
c = (a*f(b) - b*f(a))/(f(b) - f(a))

for i in range(N):
    if f(a) * f(c) < 0:
        b = c
    else: 
        a = c
    c = (a*f(b) - b*f(a))/(f(b) - f(a))
    print(f'c = {c:0.4f}')
