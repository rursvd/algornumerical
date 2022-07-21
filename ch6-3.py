import numpy as np
		
x = 1.0
		
# Taylor series of cos(x)
tay1 = 1
tay2 = tay1 - x**2/2
tay3 = tay2 + x**4/24
tay4 = tay3 - x**6/720
tay5 = tay4 + x**8/40320
		
print(f'1 term(s) : {tay1:0.4f}')
print(f'2 term(s) : {tay2:0.4f}')
print(f'3 term(s) : {tay3:0.4f}')
print(f'4 term(s) : {tay4:0.4f}')
print(f'5 term(s) : {tay5:0.4f}')
		
# Erros
exact = np.cos(x) 
err1 = (tay1 - exact)/exact * 100 
err2 = (tay2 - exact)/exact * 100 
err3 = (tay3 - exact)/exact * 100 
err4 = (tay4 - exact)/exact * 100 
err5 = (tay5 - exact)/exact * 100 
		
print(f'1 term(s) error : {abs(err1):0.1f}%')
print(f'2 term(s) error : {abs(err2):0.1f}%')
print(f'3 term(s) error : {abs(err3):0.1f}%')
print(f'4 term(s) error : {abs(err4):0.1f}%')
print(f'5 term(s) error : {abs(err5):0.1f}%')
