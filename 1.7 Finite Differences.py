from time import sleep

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

N=100
meshPoints=2*N+1
deltaT = 1
x_vals = [0]*meshPoints
for i in range(0,meshPoints):
    x_vals[i]= i/(meshPoints-1);
f = [0]+[100]*(meshPoints-2)+[0]

for i in range(50000):
    change = [0]*meshPoints
    change[1]=(-f[0]+2*f[1])/(4*N**2)
    for x in range(2,meshPoints-2):
        change[x] = (-f[x-1]+2*f[x]-f[x+1])/(4*N**2)
    change[meshPoints-2] = (-f[meshPoints-3]+2*f[meshPoints-2])/(4*N**2)

    for x in range(1,meshPoints-1):
        f[x]=f[x]-10000*change[x]

    if(i%1000==0):
        ax.plot(x_vals, f)




plt.show()



