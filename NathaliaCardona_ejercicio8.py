import numpy as np
import matplotlib.pyplot as plt

g = 9.8
n = 1000
x_obs = np.array([880, 795, 782, 976, 178])
sigma = 5.0
sigma_v = 1
def x(v, theta):
    return v**2 * np.sin(2*theta)/g

def lkh(v):
    theta = np.random.uniform(0,2*np.pi,n)
    ii = np.zeros(n)
    for i in range(n):
        d = x(v,theta[i])
        for j in range(5):
            ii = (d > x_obs[j]-sigma) & (d < x_obs[j]+sigma)
    p = len(theta[ii])/n
    return p

def prior(v):    
    p=0
    if v>=10 and v<=100:
        p=1
    return p/90

lista_v = [np.random.uniform(10,50)]
posterior = []
posterior.append(lkh(lista_v[0])*prior(lista_v[0]))
N = 500

for i in range(1,N):
    propuesta_v  = lista_v[i-1] + np.random.normal(loc=0.0, scale=sigma_v)
    
    posterior_old = lkh(lista_v[i-1])*prior(lista_v[i-1])    
    posterior_new = lkh(propuesta_v)*prior(propuesta_v)    

    r = min(1,posterior_new/posterior_old)
    alpha = np.random.random()
    if(alpha<r):
        lista_v.append(propuesta_v)
        posterior.append(posterior_new)
    else:
        lista_v.append(lista_v[i-1])
        posterior.append(posterior_old)           

lista_v = np.array(lista_v)
posterior = np.array(posterior)
ds = np.std(lista_v)
media = np.mean(lista_v)
hist, edges = np.histogram(lista_v,bins=50,density=True)
maxv = edges[1:][hist==max(hist)] 
plt.hist(lista_v)
plt.title("Desviacion estandar " + "{:2f}".format() "Promedio" + "Maximo" + )
plt.savefig("histograma.pdf")
