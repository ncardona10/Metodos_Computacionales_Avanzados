import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import norm 

data = np.loadtxt('sample.dat')

#Histograma
plt.hist(data,density = True)

#Gaussiana
mu, sigma = norm.fit(data)
x_min, x_max = plt.xlim()

x = np.linspace(x_min, x_max, 100)
y = norm.pdf(x, mu, sigma)

plt.plot(x,y)
plt.title('Resultados para mu={:.2f} y  sigma = {:.2f}'.format(mu,sigma))

plt.savefig('sample.pdf')
