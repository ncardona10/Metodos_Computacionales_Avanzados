import matplotlib
matplotlib.use("Agg")
import numpy as np 
import matplotlib.pyplot as plt

dataSerial = np.loadtxt('walkSerial.txt')
dataParallel = np.loadtxt('walkParallel.txt')

plt.hist(dataSerial, label = 'Serial', density = True, alpha = 0.5)
plt.hist(dataParallel, label = 'Paralelo', density = True, alpha = 0.5 )
plt.legend()
plt.savefig('histograma.png')
plt.close()