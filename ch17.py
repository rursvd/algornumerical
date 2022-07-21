# Second-order ODE solver with Euler methods	
# d^2y/dt^2 = f(t,y,dy/dt), y(t0) = y0, dy(t0)/dt = v0 
# Set 
# dy/dt = v, dv/dt = f(t,y,dy/dt)
	
import numpy as np

h = 0.1
time = np.arange(0,1.0,h)

yold = 1.0 
vold = 0.0 

for t in time:
    ynew = yold + h*vold
    vnew = vold + h*(t**2-yold)
    print(f't={t+h:0.2f},y={ynew:0.4f},v={vnew:0.4f}')
    yold = ynew
    vold = vnew
