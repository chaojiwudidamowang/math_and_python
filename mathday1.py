#from cmath import sin
from sympy.abc import x, y, z, f
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from sympy import *
import sympy
import numpy as np
from sympy import oo
#from sympy import sin

# 使用python求lim(x->1) (x^2-1)/(x-1)
x = sympy.symbols('x')
f = (x**2-1)/(x-1)
print(sympy.limit(f, x, 1))

# 求lim(x->0) sinx/(3x+x^3)
f = sympy.sin(x)/(3*x+x**3)
print(sympy.limit(f, x, 0))

# 求y=arcsin根号下sinx的导数
# diff表示对函数求导
print(diff(asin(sqrt(sympy.sin(x)))))

# 求f(x,y)=x^2+3xy+y^2在(1,2)处的偏导数
f = x**2+3*x*y+y**2
# 表示求f对于x的偏导数
diff(f, x)
diff(f, y)
fx = diff(f, x)
print(fx.evalf(subs={x: 1, y: 2}))
fy = diff(f, y)
print(fy.evalf(subs={x: 1, y: 2}))

# python实现梯度下降法求解函数的最小值并画出图像 minf(x)=x1-x2+2x1^2+2x1x2+x2^2 X(0)=(0,0)T


def Fun(x, y):
    return x-y+2*x*x+2*x*y+y*y


def PxFun(x, y):
    return 1+4*x+2*y


def PyFun(x, y):
    return -1+2*x+2*y


fig = plt.figure()
ax = Axes3D(fig,auto_add_to_figure=False)
fig.add_axes(ax)
X, Y = np.mgrid[-2:2:40j, -2:2:40j]
Z = Fun(X, Y)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap="rainbow")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
step = 0.0008
x=0
y=0
tag_x=[x]
tag_y=[y]
tag_z=[Fun(x,y)]
new_x=x
new_y=y
Over=False
while Over==False:
    new_x-=step*PxFun(x,y)
    new_y-=step*PyFun(x,y)
    if Fun(x,y)-Fun(new_x,new_y)<7e-9:
        Over=True
    x=new_x
    y=new_y
    tag_x.append(x)
    tag_y.append(y)
    tag_z.append(Fun(x,y))
ax.plot(tag_x,tag_y,tag_z,'r')
plt.title('(x,y)~('+str(x)+","+str(y)+')')
plt.show()