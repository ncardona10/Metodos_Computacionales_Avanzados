import matplotlib
matplotlib.use("Agg")
import numpy as np 
import matplotlib.pyplot as plt

dataSerial = np.loadtxt('adveccionSerial.txt')
n = int(4.0/0.05 + 1)
xSerial = np.linspace(0.0, 4.0, n)
ySerial = dataSerial
print("yserial: ", ySerial)
dataParallel = np.loadtxt('adveccionParallel.txt')
xParallel = np.linspace(0.0, 4.0, n)
yParallel = dataParallel
print("ypAr: ", yParallel)

plt.plot(xSerial,ySerial, label = 'Serial')
plt.plot(xParallel, yParallel, label = 'Paralelo')
plt.xlabel("x")
plt.ylabel("u(x)")
plt.legend()
plt.show()
plt.savefig("grafica.png")
plt.close()

