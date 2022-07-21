import numpy as np

A = np.array([[2,1,0],[1,4,-1],[0,-1,7]])
b = np.array([4,6,19])

N = 10
xold = np.array([0.0,0.0,0.0])

omega = 1.5
L = np.tril(A,-1)
U = np.triu(A,1)
D = np.diag(np.diag(A))

former = np.linalg.inv(L + D/omega) 

for k in range(N):
    latter = (D/omega - D - U) @ xold + b
    xnew = former @ latter
    xold = xnew
    print(k+1, xnew)
