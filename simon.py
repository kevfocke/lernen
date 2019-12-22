import numpy as np
#bla = np.random.rand()
#print(bla)
a=[]
b=[]
c=[]
t=100000000
for i in range(t):
	x=np.random.rand()
	y=np.random.rand()
	a.append(x)
	b.append(y)


for i in range(t):	
	if a[i]**2+b[i]**2<1:
		c.append(1)
	
u=4*float(len(c))/len(a)
print(u)


