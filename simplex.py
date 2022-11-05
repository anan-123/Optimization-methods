import numpy as np
y1=[]
y2 = []
def find_ele(t):
    ans=max(t)
    for r in t:
        if r>0 and r<ans:
            ans=r
    return ans
def locate_r(table):
        if min(table[:-1,len(table[0,:])-1])<=0:
            r= np.where(table[:-1,len(table[0,:])-1] == min(table[:-1,len(table[0,:])-1]))[0][0]

        for i, b in zip(table[:-1, np.where(table[r,:-1] == min(table[r,:-1]))[0][0]],table[:-1,-1]):
            if i**2<=0 and b/i<=0:
               y1.append(0)
            else:
                y1.append(b/i)
        e=find_ele(y1)
        return [y1.index(e), np.where(table[r,:-1] == min(table[r,:-1]))[0][0]]
def locate(table):
    if min(table[len(table[:,0])-1,:-1])<0:
        if min(m[len(m[:,0])-1,:-1])<=0:
            n= np.where(m[len(m[:,0])-1,:-1] == min(m[len(m[:,0])-1,:-1]))[0][0]
    
        for i,b in zip(table[:-1,n],table[:-1,-1]):
            if i**2<=0 and b/i<=0:
               y2.append(0)
            else:
                y2.append(b/i)
        e=find_ele(total)
        return [y2.index(element),n]

def pivot(r,c,m):
    t = np.zeros((len(m[:,0]),len(m[0,:])))
    if m[r,c]!=0:  
        ratio = m[r,:]*1/m[r,c]
        for i in range(len(m[:,c])):
            if list(m[i,:]) == list(m[r,:]) and (1==1):
                t[i,:] = list(m[i,:]-ratio*m[i,c])
        t[r,:] = list(ratio)
        return t
    
   

#----------------------------------------------------------------MAIN----------------------------------------------------------------
import sys
filename = sys.argv[1]
f = open(filename, "r")
k = f.read()
y = k.split('\n')
flag = 0
A= []

for i in range(0,len(y)):
    if y[i][0]=='s':
        flag+=1
        continue
    if y[i][0]=='e':
        continue
    if flag == 1:
        A.append(list(y[i].split()))
    if flag==2:
        B= list(y[i].split())
    if flag==3:
        C =list(y[i].split())

C = list(map(float,C))
a=A.copy()
for i in range(len(a)):
    a[i]=list(map(float,a[i]))
b = list(map(float,B))
c = list(map(float,C))
n1 =len(A)
n2 = len(C)
m = np.zeros((n1+1,n2+n1+2))
for i in range(len(A)):
    l1 = a[i]
    l1.append(b[i])
    l1=np.negative(l1)
    
    val=0
    for i in range(len(m[:,0])):
        flag=1
        for j in m[i,:]:
            if j!=0:
                flag=0
        if flag==1:
            val=1
            break
    if val==1:
        for j in range(len(m[0,:])):
            flag=1
            for i in m[j,:]:
                if i!=0:
                    flag=0
            if flag==1:
                r = m[j,:]
                break
        r[0:len(l1)-1]=l1[0:len(l1)-1]
        r[-1 ] = l1[-1]
        r[len(m[:,0])- len(m[:,0])-1+j] = 1
   
count=0
flag=0
for i in range(len(m[:,0])):
    flag=0
    for j in m[i,:]:
            if j!=0:
                flag=1
    if flag == 0:
            count+=1
  
if count==1:
        r = m[len(m[:,0])-1,:]
        r[-1]=C[-1]
        r[0:len(C)-1]=np.negative(C[0:len(C)-1])
        r[-2]=1
        

   
m[-1,-1] = np.negative(m[-1,-1])
m[-1,:-2] = np.negative(m[-1,:-2])


if min(m[:-1,-1])<0:
        m= pivot(locate_r(m)[0],locate_r(m)[1],m)
while min(m[len(m[:,0])-1,:-1]):
        m = pivot(locate(m)[0],locate(m)[1],m)
if m[-1,-1]*-1==0:
    print(0)
else:
    print(m[-1,-1]*-1)
ans=[]
for i in range(len(m[0,:]) -len(m[:,0])-1):
        if float(sum(m[:,i])) == float(max(m[:,i])):
            print(m[np.where(m[:,i] == max(m[:,i]))[0][0],-1], end =" ")
        else:
            print(0,end=" ")
print()