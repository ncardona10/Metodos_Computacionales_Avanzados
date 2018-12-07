import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

#PARTE2

def e(lamb,y):
    return np.exp(-lamb/y)/(y**2)

lamb = 2
d = 0.7
n = 1000000
y = np.linspace(0.00000001,300,n)

y[0] = 0.5
cont = 0
for i in range(1,n,1):
    #xn = x[i-1]+2*d*(np.random.uniform()-0.5)
    yn = y[i-1] + d*(np.random.uniform()-0.5)
    while(yn<=0):
        yn = y[i-1] + d*(np.random.uniform()-0.5)
    F = e(lamb,yn)/e(lamb,y[i-1])
    #Algoritmo metropolis
    if(F>=1):
        #Aceptamos
        y[i]=yn
        cont+=1
    else:
        if np.random.uniform()<F:
            y[i] = yn
            cont+=1
        else:
            y[i] = y[i-1]

#grafica
histogram = plt.hist(y,bins=100,density = True)
x1 = np.linspace(0.00001,40,1000)
y1 = e(lamb,x1)
# print(y1)
y1/=integrate.simps(y1,x1)
plt.plot(x1,y1)
plt.savefig("distribucion4.png")
plt.close()
