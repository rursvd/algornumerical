import numpy as np

x = np.array([1.5,1.3,1.2,1.1])

# dxdt at t = 2
dxdt_f = (x[2] -  x[1])/(2-1) 
dxdt_b = (x[1] -  x[0])/(1-0) 
dxdt_c = (x[2] -  x[0])/(3-1)

print(f'forward = {dxdt_f:0.4f} m/sec')
print(f'backward = {dxdt_b:0.4f} m/sec')
print(f'central = {dxdt_c:0.4f} m/sec')
