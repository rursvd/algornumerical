import numpy as np
import numpy.linalg

def R2(y,yhat,ybar):
    SSR = np.sum((y - yhat)**2)
    SST = np.sum((y - ybar)**2)
    R2 = 1 - SSR/SST
    return R2   

x = np.array([1,2,3,4,5]) 
y = np.array([8.5,7.7,6.9,4.5,2])
ybar = np.average(y)

# linear interpolation
XT = np.array([[1,1,1,1,1],[1,2,3,4,5]])
X = XT.T
beta = np.linalg.inv(XT @ X) @ (XT @ y)
yhat = X @ beta

# polynomial interpolation
xsq = x**2 # x^2
X = np.column_stack([np.ones(len(x)),x,xsq])
XT = X.T
beta2 = np.linalg.inv(XT @ X) @ (XT @ y)
yhat2 = X @ beta2

# R2 calculation
R2_linear = R2(y,yhat,ybar) 
R2_poly = R2(y,yhat2,ybar)

print(f'R2_linear = {R2_linear:0.4f}')
print(f'R2_poly = {R2_poly:0.4f}')
