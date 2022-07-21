import numpy as np	
	
h = 0.1
time = np.arange(0.0,1.0,h)
yold = 0.5
 
for t in time:
    ynew = (1.0 + h)*yold - h*t
    print(f't={t+h:0.2f},y={ynew:0.3f}')
    yold = ynew
