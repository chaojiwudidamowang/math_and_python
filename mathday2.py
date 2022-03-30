import sympy
import numpy

x = sympy.Symbol('x')
f = sympy.sin(sympy.ln(x))
print(sympy.limit(f, x, 1))

# 自然对数的底
print(sympy.log(sympy.E))
# 圆周率Π
print(sympy.sin(sympy.pi))
