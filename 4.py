import numpy as np 
import math
import matplotlib.pyplot as plt 


def f(x,l):
    x1 = x[0]
    x2 = x[1]
    if l==0:
        f = 10*(x1**2)+10*x1*x2+x2**2+4*x1-10*x2
    if l==1:
        f = 16*(x1**2)+8*x1*x2+10*(x2**2)+12*x1-6*x2
    return f+2 
def df(x,l):
    x1 = x[0]
    x2 = x[1]
    if l==0:
        a= 20*x1 + 10*x2 + 4
        b= 10*x1 + 2*x2 - 10
        
    if l==1:
        a= 32*x1 + 8*x2 + 12
        b = 8*x1 + 20*x2 - 6
    return [a, b]

def H(l):
    if l==0:
        return [[20, 10], [10, 2]]
    if l==1:
        return [[32, 8], [8, 20]]
for l in range(0,2):
    if l==0:
        x0=[1.8,-4]
    else: 
        x0=[-0.5,0.5]
    f_val=[]
    fx0 = f(x0,0)
    alpha = 0.01
    flagp=0
    flagn=0
    for i in range(200):
        p = alpha*(np.cos(i*math.pi/100))
        q = alpha*(np.sin(i*math.pi/100))
        x=[x0[0]+p, x0[1]+q]
        fx = f(x,l)
        f_val.append(fx-fx0)
        if(fx-fx0<0):flagn=1
        if(fx-fx0>0):flagp=1
    print(' 1. the gradient of f is : ',df(x0,l))
    eg,ev=np.linalg.eigh(H(l))
    print('2. the eigen values of H(f) : ',eg)
    if(flagp==1 and flagn==1):
        print('3. the point : ',x0,' is a saddle point')
    elif(flagp==1 and flagn==0):
        print('3. the point : ',x0,' is a local minima')
    else:
        print('3. the point : ',x0,' is a local maxima')
    plt.plot([i*math.pi/100 for i in range(200)],f_val)
    plt.show()