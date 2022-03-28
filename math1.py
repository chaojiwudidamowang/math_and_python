#1
import os
import sympy
print("hello")
x=sympy.symbols('x')
f=(x/sympy.sqrt(x*x+x))**x
print(sympy.limit(f,x,sympy.oo))
