# ODE solver with predictor-corrector methods	
# dy/dt = f(t,y), y(t0) = y0
	
import numpy as np
		
def f(t,y):
    return -t + y
			
h = 0.1
time = np.arange(0,1.0,h)
yold = 0.5
		
# Predictor-corrector methods 		
for t in time:
    yhat = yold + h*f(t,yold)
    ynew = yold + h*(f(t,yold) + f(t+h,yhat))/2
    print(f't={t+h:0.2f},y={ynew:0.3f}')
    yold = ynew
