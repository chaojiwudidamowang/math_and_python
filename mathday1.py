from cmath import sin
import imp
import sympy
import numpy as np
from sympy import oo
#from sympy import sin

#使用python求lim(x->1) (x^2-1)/(x-1)
x=sympy.symbols('x')
f=(x**2-1)/(x-1)
print(sympy.limit(f,x,1))

#求lim(x->0) sinx/(3x+x^3)
f=sympy.sin(x)/(3*x+x**3)
print(sympy.limit(f,x,0))  

#求y=arcsin根号下sinx的导数
from sympy import *
from sympy.abc import x,y,z,f
print(diff(asin(sqrt(sympy.sin(x)))))