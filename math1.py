#1
import os
from re import X
import sympy
print("hello")
x=sympy.symbols('x')
f=(x/sympy.sqrt(x*x+1))**x
print(sympy.limit(f,x,sympy.oo))