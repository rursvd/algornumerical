N = 10 
xold = 0.1 

for k in range(N):
    xnew = 1.5*xold + 1
    print(f'{k+1},x={xnew:0.4f}')
    xold = xnew 
