import matplotlib
matplotlib.use("Agg")
import numpy as np 
import matplotlib.pyplot as plt

data = np.loadtxt('adveccion.txt')
n = int(4.0/0.05 + 1)
x = np.linspace(0.0, 4.0, n)
y1 = data[0,:]
y2 = data[1,:]
y3 = data[2,:]
y4 = data[3,:]

plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.plot(x,y4)
plt.xlabel("x")
plt.ylabel("u(x)")
plt.savefig("grafica.png")
plt.close()

