import numpy as np

def f(x):
    return x*np.exp(-x) + 1.0

N = 15
a = -1.0
b = 1.0 
c = (a + b)/2.0

for i in range(N):
    if f(a) * f(c) < 0:
        b = c
    elif f(c) * f(b) < 0:
        a = c
    else:
        print('No sign change.')
    c = (a + b)/2.0
    print(f'c = {c:0.4f}')
