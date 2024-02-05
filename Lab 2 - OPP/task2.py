import math
from task1 import Complex

x= [2,2,2,2,2,2,2,2]

sol  = 0 
for k in range(len(x)):
    for n, val in enumerate(x):
        sol +=val * math.e ** ((-2j*k*n*math.pi)/8)

    result= Complex(sol.real, sol.imag)
    print("-----------------")
    print(k)
    print(result.__str__())
    print(result.Magnitude())
    print(result.Orientation())