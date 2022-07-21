import numpy as np

W = np.array([[25,65],[29,73],[23,55],[21,52]])

print(W[:,0])
tavg = np.average(W[:,0])
tvar = np.var(W[:,0])
print(f'tavg = {tavg}')
print(f'tvar = {tvar}')

print(W[:,1])
havg = np.average(W[:,1])
hvar = np.var(W[:,1])
print(f'havg = {havg}')
print(f'hvar = {hvar}')
