#Comparacion de los modelos:
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = pd.read_csv("years-lived-with-disability-vs-health-expenditure-per-capita.csv", delimiter = ",")
data = data[data.Year==2011]

data = data.dropna()
x = np.array(data.Health_expenditure_per_capita_PPP)
y = np.array(data.Years_Lived_With_Disability)
#M1
N = 1000
gm = np.random.uniform(0,1E-2,N)
gb = np.random.uniform(0,20,N)

def model(x, m, b):
    return x*m + b

def lk(x,y,m,b):
    y_model = model(x, m, b)
    p = y_model * np.exp(-(y_model/y))
    p = p/(y**2)
    return np.sum(p)

def montecarlo(N,gm,gb):
    lks = np.ones(N)
    for i in range(N):
        lks[i] = lk(x,y,gm[i],gb[i])
    return np.sum(lks)/N

pm1d = montecarlo(N,gm,gb)

#M2
N2 = 1000
ga2 = np.random.uniform(0,2,N2)
gb2 = np.random.uniform(0,3,N2)

def model2(x, a, b):
    return a*np.log(x*b)

def lk2(x,y,a,b):
    y_model = model2(x, a, b)
    p = y_model * np.exp(-(y_model/y))
    p = p/(y**2)
    return np.sum(p)

def montecarlo2(N2,ga2,gb2):
    lks = np.ones(N2)
    for i in range(N2):
        lks[i] = lk2(x,y,ga2[i],gb2[i])
    return np.sum(lks)/N2

pm2d = montecarlo2(N2,ga2,gb2)

#M3
N3 = 1000
ga3 = np.random.uniform(0,10,N3)
gb3 = np.random.uniform(-10,10,N3)
gm3 = np.random.uniform(0,0.5,N3)

def model3(x, a, b, m):
    return a*np.log(m*x)+b

def lk3(x,y,a,b,m):
    y_model = model3(x, a, b, m)
    p = y_model * np.exp(-(y_model/y))
    p = p/(y**2)
    return np.sum(p)

def montecarlo3(N3,ga3,gb3,gm3):
    lks = np.ones(N3)
    for i in range(N3):
        lks[i] = lk3(x,y,ga3[i],gb3[i],gm3[i])
    return np.sum(lks)/N3

pm3d = montecarlo3(N3,ga3,gb3,gm3)

#Comparacion:
F12 = pm1d/pm2d
F23 = pm2d/pm3d
F13 = pm1d/pm3d
print (F12,F23,F13)

