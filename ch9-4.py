# Lagrange interpolation 	

# Data	
x0 = 2
x1 = 3
x2 = 5
f0 = 0.2706
f1 = 0.1493
f2 = 0.0336

# Interpolation point
xw = 2.3

# Linear interpolation
fintp = (xw - x1)/(x0 - x1)*f0 + (xw - x0)/(x1 - x0)*f1
print(f'f(2.6) = {fintp:0.4f}')

# Second-order interpolation
fintp2 = (xw - x1)*(xw - x2)/((x0 - x1)*(x0 - x2))*f0 \
	+ (xw - x0)*(xw - x2)/((x1 - x0)*(x1 - x2))*f1 \
	+ (xw - x0)*(xw - x1)/((x2 - x0)*(x2 - x1))*f2
print(f'f(2.6) = {fintp2:0.4f}')
