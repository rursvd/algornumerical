import numpy as np	
	
def f(x):
    return np.cos(x)

# two-point Gaussian quadrature
N = 2
xi = np.array([1.0/np.sqrt(3),-1.0/np.sqrt(3)])
w = np.array([1.0,1.0])

sums = 0.0

for i in range(N):
    sums += w[i] * f(xi[i])  
	 
print(f'I={sums:0.4f}')
