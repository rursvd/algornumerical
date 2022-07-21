# ODE solver with ABM2 	
# dy/dt = f(t,y), y(t0) = y0

import numpy as np

# Define f(t,y) 
def f(t,y):
    return -t + y

h = 0.1
time = np.arange(0,1.0-h,h)
yold = 0.5

# Euler method (initiator)
yinit = yold + h*f(0,yold)
print(f't={time[0]+h:0.2f},y={yinit:0.3f}')

# ABM2 predictor-corrector methods
for t in time:
    yhat = yinit + 3/2*h*f(t+h,yinit) - 1/2*h*f(t,yold)
    ynew = yinit + 1/2*h*(f(t+h,yinit) + f(t+2*h,yhat))
    print(f't={t+2*h:0.2f},y={ynew:0.4f}')
    yold = yinit
    yinit = ynew
