import numpy as np

fx = np.array([1.0,1.5,2.0,2.5,3.0])

a = 0.0
b = 4.0

n = len(fx)
N = n - 1
h = (b-a)/N

sums = 0.0
for i in range(N):
    sums += fx[i] + fx[i+1]
I = h*sums/2
print(f'I = {I:0.4f}')
