import numpy as np

def fxi(xi):
    return (xi+3)**2*np.exp(-(xi+3))

# two-point rule
N = 2
w = np.array([1.0,1.0])
xi = np.array([1.0/np.sqrt(3),-1.0/np.sqrt(3)])
a = 2
b = 4

sums = 0.0
for i in range(N):
	sums += w[i] * fxi(xi[i])
sums =  (b-a)*sums/2    
print(f'I = {sums:0.4f}')
