import matplotlib  
matplotlib.use('Agg')
import numpy as np 
import matplotlib.pyplot as plt 
from os import listdir
from os.path import isfile, join
from scipy.stats import norm 

real = 155.0/6.0
data = np.loadtxt('data.dat')
n = data[:,0]
error = abs(real - data[:,1]) / real *100

plt.semilogy(n,error)
plt.xlabel('numero de procesadores')
plt.ylabel('Error porcentual')

plt.savefig('grafica.png')


plt.close()





