import numpy  as np

x = np.array([1,2,3,4,5]) 
y = np.array([8.5,7.7,6.9,4.5,2])
n = len(x)

beta0_nom = np.sum(y)*np.sum(x**2) - np.sum(x)*np.sum(x*y)
denom = n*np.sum(x**2) - (np.sum(x))**2 
beta0 = beta0_nom / denom

beta1_nom = n*np.sum(x*y) - np.sum(x)*np.sum(y)
beta1 = beta1_nom / denom
print(beta1_nom)
print(beta1)

print(beta0, beta1)
yhat = beta0 + beta1 * x  
print(yhat)
