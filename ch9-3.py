def secinterp(x):
    beta0 = f0
    beta1 = (f1 - f0)/(x1 - x0)
    beta2 = ((f2 - f1)/(x2 - x1) - (f1 - f0)/(x1 - x0))/(x2 - x0)
    equ = beta0 + beta1*(x-x0) + beta2*(x-x0)*(x-x1)
    return equ

x0 = 2.0
x1 = 4.0
x2 = 5.0
f0 = 0.2706
f1 = 0.0732
f2 = 0.0336 

xw = 3.3

intp = secinterp(xw) 

print(f'f(x) = {intp:0.4f}')
