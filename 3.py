import numpy as np 
import math
from scipy import optimize
import matplotlib.pyplot as plt 
def f(x):
    x1 = x[0]
    x2 = x[1]
    f = 5*(x1**2)+5*(x2**2)-x1*x2-11*x1+11*x2
    return f+11
def df(x):
    x1 = x[0]
    x2 = x[1]
    a = 10*x1 -x2 -11
    b = 10*x2 - x1+11
    return [a,b]
    
def H(l):
    return [[10, -1], [-1, 10]]
def plot_f(a,b,fx):
    ax = plt.axes(projection='3d')
    ax.plot3D(a,b,fx, 'gray')
    plt.show()
def contour_plot(x,a,b,c,d,l):
    [p, q] = np.meshgrid(np.linspace(a,b, 100),np.linspace(c,d, 100))
    plt.ylabel('x2')
    r = f([p,q])
    plt.contourf(p,q,r)
    plt.xlabel('x1')
    for i in range(1,len(x)):
        a1=x[i-1][0]
        a2= x[i-1][1]
        a3=x[i][0]-a1
        a4=x[i][1]-a2
        plt.arrow(a1,a2,a3,a4,head_width= l,length_includes_head=True)
    plt.show()
starting_points= [[10,-9],[1,1],[-1,4],[3,5],[-1,0]]
for xk in starting_points:
    print('starting point is : ',xk)
    eg,ev=np.linalg.eigh(H(0))
    # print(eg)
    #print('lambda max : ',max(eg[0],eg[1]))
    alpha1 = 2/6
    alpha2 = 2/13
    iter = 1
    x=[]
    fx=[]

    while(np.linalg.norm(df(xk))>=0.000001):
        dk = df(xk)
        dk = [-(2/15)*p for p in dk]
        xk= [sum(value) for value in zip(xk,dk)]
        x.append(xk)
        fx.append(f(xk))
        iter=iter+1
    print(iter)
    a=[]
    b=[]
    for i in x:
        a.append(i[0])
        b.append(i[1])
    plot_f(a,b,fx)
    min_x = min([i[0] for i in x])
    max_x = max([i[0] for i in x])
    min_y = min([i[1] for i in x])
    max_y = max([i[1] for i in x])
    l = max(max_x-min_x,max_y-min_y)
    contour_plot(x,min_x,max_x,min_y,max_y,l/135)

