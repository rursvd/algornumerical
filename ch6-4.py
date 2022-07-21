x = 1.0
		
exptay = [1,x,x**2/2,x**3/6,x**4/24]
		
sums = 0
for i in range(5):
	sums += exptay[i]
	print(f'{i+1} term(s) : = {sums:0.4f}')
