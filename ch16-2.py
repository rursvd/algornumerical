import numpy as np

def f(t,y):
    return -t + y
	
h = 0.1
time = np.arange(0.0,1.0,h)
yold = 0.5 

for t in time:
    k1 = f(t,yold)
    k2 = f(t + h/2, yold + h*k1/2)
    k3 = f(t + h/2, yold + h*k2/2)
    k4 = f(t + h, yold + h*k3)
    ynew = yold + h*(k1 + 2*k2 + 2*k3 + k4)/6
    print(f't={t+h:0.2f}, y={ynew:0.3f}')
    yold = ynew
