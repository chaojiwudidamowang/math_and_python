import sympy
import numpy

x=sympy.Symbol('x')
f=sympy.sin(sympy.ln(x))
print(sympy.limit(f,x,1))