def lininterp(x):
    equ = f0 + (f1 - f0)/(x1 - x0) * (x - x0)
    return equ

x0 = 2.0
x1 = 5.0
f0 = 0.2706
f1 = 0.0336

xw = 3.3

intp = lininterp(xw) 

print(f'f(x) = {intp:0.4f}')
