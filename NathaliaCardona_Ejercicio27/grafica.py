import matplotlib  
matplotlib.use('Agg')
import numpy as np 
import matplotlib.pyplot as plt 
from os import listdir
from os.path import isfile, join
from scipy.stats import norm 


leerArch = [f for f in listdir("./") if (isfile(join("./", f)) and f.endswith('.dat'))]
arch = np.array([])

for a in leerArch:
    temp = np.loadtxt(a)
    arch = np.concatenate([temp,arch])

#Histograma
plt.hist(arch,normed = True)

#Gaussiana
mu, sigma = norm.fit(arch)
x_min, x_max = plt.xlim()

x = np.linspace(x_min, x_max, 100)
y = norm.pdf(x, mu, sigma)

plt.plot(x,y)
plt.title('Resultados para mu={:.2f} y  sigma = {:.2f}'.format(mu,sigma))

plt.savefig('sample.pdf')


    
