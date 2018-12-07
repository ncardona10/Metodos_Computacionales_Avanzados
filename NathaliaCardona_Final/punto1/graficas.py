import numpy as np 
import matplotlib.pyplot as plt 

from os import listdir
from os.path import isfile, join
from scipy.stats import norm 
#Funcion gaussiana
def gauss(x):
    g = np.exp(-(x**2)/2.0)/(2.0*np.pi)**0.5
    return g
#Histogramas
leerArch = [f for f in listdir("./") if (isfile(join("./", f)) and f.endswith('.dat'))]
arch = np.array([])
x = np.linspace(-5,5,100)
y = gauss(x)
#print(y)
for a in leerArch:
    temp = np.loadtxt(a)
    plt.hist(temp,alpha=0.5,density=True)
    
plt.plot(x,y)
plt.title('Histogramas de la distribucion gaussiana con mu=0, sigma=1')
plt.savefig('histogramas.png')
plt.close()

#Estadistica de Gelman-Rubin
ns = np.linspace(1,10,10)*100
m = 8
v = np.zeros(len(ns))
media = 0
varianza = 0
medias = []
for i in range(len(ns)):
    n = int(ns[i])
    for a in leerArch:
        temp = np.loadtxt(a)
        media += np.mean(temp[:n])
        medias.append(np.mean(temp[:n]))
        varianza += np.std(temp[:n])
    b = n/(m-1)*np.sum((np.array(medias)-media)**2)
    theta = media/m
    w = varianza/m
    v[i] = ((n-1)/n) * w + ((m+1)/n*m) * b

plt.plot(ns,v)
plt.title('Estadistica de Gelman Rubin')
plt.xlabel('numero de iteraciones')
plt.ylabel('Estadistica de Gelman')
plt.savefig('GelmanRubin.png')
plt.close()



