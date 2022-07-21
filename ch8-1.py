import numpy as np	
	
# Functions
def f(x):
    return x*np.exp(-x)

# Foward difference 
def fordiff(xi):
    xpi = xi + h
    fdf = (f(xpi) - f(xi))/h
    return fdf

# Backward difference
def bacdiff(xi):
    xmi = xi - h
    bdf = (f(xi) - f(xmi))/h
    return bdf

# Central difference
def cendiff(xi):
    xpi = xi + h
    xmi = xi - h
    cdf = (f(xpi) - f(xmi))/(2*h)
    return cdf

h = 0.1
xi = 1.2

print(f'forward diff: {fordiff(xi):0.4f}')
print(f'backward diff: {bacdiff(xi):0.4f}')
print(f'centered diff: {cendiff(xi):0.4f}')
