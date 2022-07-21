import numpy as np	
	
def f(x):
    return x**2*np.exp(-x)

n = 3 # number of subintervals
a = 2.0
b = 4.0
h = (b - a)/n
x = np.linspace(a,b,n+1) # number of points

sums = 0.0
for i in range(n):
    sums += f(x[i]) + f(x[i+1])
result = h*sums/2
print(f'I = {result:0.4f}')
