import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = pd.read_csv("years-lived-with-disability-vs-health-expenditure-per-capita.csv", delimiter = ",")
data = data[data.Year==2011]

data = data.dropna()
x = np.array(data.Health_expenditure_per_capita_PPP)
y = np.array(data.Years_Lived_With_Disability)
#plt.scatter(x,y)

#Modelo1
def model(x,m,b):
    return x*m + b

def loglikelihood(x,y,m,b):
    y_model = model(x, m, b)
    p = y_model * np.exp(-(y_model/y))
    p = p/(y**2)
    p = np.log(p)
    return np.sum(p)

def logprior(m,b):
    if  np.abs(m < 1E-2) and b >0 and b<20:
        area = 2.0*1E-2*20.0
        p = np.log(1.0/area)
    else:
        p = -np.inf
    return p

N = 50000
lista_m = [1/8000.0]
lista_b = [10.0]

logposterior = [loglikelihood(x, y, lista_m[0], lista_b[0]) + logprior(lista_m[0], lista_b[0])]

sigma_delta_m = 1E-4
sigma_delta_b = 0.5

for i in range(1,N):
    propuesta_m  = lista_m[i-1] + np.random.normal(loc=0.0, scale=sigma_delta_m)
    propuesta_b  = lista_b[i-1] + np.random.normal(loc=0.0, scale=sigma_delta_b)
 
    logposterior_viejo = loglikelihood(x, y, lista_m[i-1], lista_b[i-1]) + logprior(lista_m[i-1], lista_b[i-1])
    logposterior_nuevo = loglikelihood(x, y, propuesta_m, propuesta_b) + logprior(propuesta_m, propuesta_b)

    r = min(1,np.exp(logposterior_nuevo-logposterior_viejo))
    alpha = np.random.random()
    if(alpha<r):
        lista_m.append(propuesta_m)
        lista_b.append(propuesta_b)
        logposterior.append(logposterior_nuevo)
    else:
        lista_m.append(lista_m[i-1])
        lista_b.append(lista_b[i-1])
        logposterior.append(logposterior_viejo)
lista_m = np.array(lista_m)
lista_b = np.array(lista_b)
logposterior = np.array(logposterior)

x_model = np.linspace(0,10000,10000)
y_model = model(x_model,np.mean(lista_m),np.mean(lista_b))
plt.plot(x_model, y_model,color="red",label="Modelo")
plt.scatter(x,y,label="Datos")
plt.legend()
plt.savefig("Modelo1.png")
plt.close()