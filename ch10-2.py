import numpy as np	
	
def f(x):
    return x**2*np.exp(-x)

n = 4 
a = 2.0
b = 4.0
h = (b - a)/n
x = np.linspace(a,b,n+1)

sums = f(x[0]) + f(x[n])
for i in range(1,n):
    if i%2 == 0:
        sums += 2 * f(x[i])
    else:
        sums += 4 * f(x[i])
sums = h*sums/3
print(f'I = {sums:0.4f}')
