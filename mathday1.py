import sympy
from sympy import oo
#使用python求lim(x->1) (x^2-1)/(x-1)
x=sympy.symbols('x')
f=(x**2-1)/(x-1)
print(sympy.limit(f,x,1))
