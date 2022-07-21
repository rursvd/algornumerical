import numpy as np	
	
def fxi(xi):
	return (xi+3)**2*np.exp(-(xi+3))

# three-point rule
N = 3
w = np.array([8.0/9.0,5.0/9.0,5.0/9.0])
xi = np.array([0.0,np.sqrt(3.0/5.0),-np.sqrt(3.0/5.0)])
a = 2
b = 4

sums = 0.0
for i in range(N):
	sums += w[i] * fxi(xi[i])
sums =  (b-a)*sums/2    
print(f'I={sums:0.4f}')
