N = 10 
xold = 1

for k in range(N):
	xnew = 0.4*xold + 0.1
	err = abs((xold-xnew)/xnew) * 100
	print(f'{k+1},error={err:0.4f} %')
	xold = xnew 
