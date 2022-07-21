import numpy as np	
	
def f(x):
    return np.cos(x)

# three-point Gaussian quadrature
N = 3
xi = np.array([0.0,np.sqrt(3.0/5.0),-np.sqrt(3.0/5.0)])
w = np.array([8.0/9.0,5.0/9.0,5.0/9.0])

sums = 0.0

for i in range(N):
    sums += w[i] * f(xi[i])
	  
print(f'I={sums:0.4f}')
