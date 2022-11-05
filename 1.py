import numpy as np 
import math
from scipy import optimize
import matplotlib.pyplot as plt 
def coeff(x1,x2,a,b,c):
    return a*np.exp(x1+3*x2-0.1)+b*np.exp(x1-3*x2-0.1)+c*np.exp(-x1-0.1)
def f(x):
    return coeff(x[0],x[1],1,1,1)
def df(x):
    a = coeff(x[0],x[1],1,1,-1)
    b = coeff(x[0],x[1],3,-3,0)
    return [a,b]
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

def armijo_goldstein(xk,dk):
    alpha = 0.5
    r=0.7
    beta=0.1
    dk=np.array(dk)
    xk=np.array(xk)
    c1 = 0.3
    while not (f(xk+alpha*dk) <= f(xk)+alpha*c1*np.dot(df(xk),dk)) and (f(xk+alpha*dk) >= f(xk)+alpha*(1-c1)*np.dot(df(xk),dk)) :
        alpha=r*alpha
    return alpha
def backtrack_armijo(xk,dk):
    alpha = 0.5
    r=0.7
    beta=0.1
    dk=np.array(dk)
    xk=np.array(xk)
    while not f(xk+alpha*dk) <= f(xk)+alpha*beta*np.dot(df(xk),dk):
        alpha=r*alpha
    return alpha

epsilon = 0.000001
x=[]
fx=[]
xk = [1,0.2]
iter = 1
print('armijo goldstein')
while(np.linalg.norm(df(xk))>=0.000001):
    dk = df(xk)
    dk = [-1*p for p in dk]
    #alpha = backtrack_armijo(xk,dk)
    alpha=armijo_goldstein(xk,dk)
    dk = [alpha*p for p in dk]
    xk= [sum(value) for value in zip(xk,dk)]
    x.append(xk)
    # print(xk)
    # print(f(xk))
    fx.append(f(xk))
    iter=iter+1
print('No of iterations =',iter)
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
print('backtrack armijo')
while(np.linalg.norm(df(xk))>=0.000001):
    dk = df(xk)
    dk = [-1*p for p in dk]
    alpha = backtrack_armijo(xk,dk)
    #alpha=armijo_goldstein(xk,dk)
    dk = [alpha*p for p in dk]
    xk= [sum(value) for value in zip(xk,dk)]
    x.append(xk)
    # print(xk)
    # print(f(xk))
    fx.append(f(xk))
    iter=iter+1
print('No of iterations =',iter)
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