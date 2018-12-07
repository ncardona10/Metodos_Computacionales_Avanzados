#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[3]:


data = np.loadtxt('datos_observacionales.dat')
t = data[:,0]
x = data[:,1]
y = data[:,2]
z = data[:,3]


# In[15]:


#Modelo fisico
def model(x,y,z,t,params):
    return 0

def hamiltonian(x, y, z,t, params, momentum):
    K = 0.5 * np.sum(momentum**2)
    V = -loglikelihood(x, y, z, params)
    return K + V

def loglikelihood(x, y, z,t, params):
    d = y_obs -  model(x, y,z,params)
    d = d
    d = -0.5 * np.sum(d**2)
    return d

def logprior(params):
    p = 0.0
    n_param = len(params)
    for i in range(n_params):
        if params[i] < 30 and params[i]>0 :
            p += 0.0
        else:
            p += np.inf
    return p

def leapfrog(x, y, z,t, params, momentum):
    N_steps = 5
    dt = 1E-2
    m = 1
    new_params = params.copy()
    new_momentum = momentum.copy()
    for i in range(N_steps):
        new_momentum = new_momentum + div_loglikelihood(x, y, z,t, params) * 0.5 * dt
        new_params = new_params + (new_momentum/m) * dt
        new_momentum = new_momentum + div_loglikelihood(x, y, z, t,params) * 0.5 * dt
    new_momentum = -new_momentum
    return new_params, new_momentum

def div_loglikelihood(x, y, z,t, params):
    div = np.ones(len(params))
    delta = 1E-5
    for i in range(len(params)):
        d_param = np.zeros(len(params))
        d_param[i] = delta
        div[i] = loglikelihood(x, y, z, params + d_param)
        div[i] = div[i] - loglikelihood(x, y, z, params - d_param)
        div[i] = div[i]/(2.0 * delta)
    return div



# In[18]:


N=5000
def MCMC(x, y, z,t):
    params = [np.random.random(3)]
    momentum = [np.random.normal(size=3)]
    for i in range(1,N):
        propuesta_params, propuesta_momentum = leapfrog(x, y,z, t,params[i-1], momentum[i-1])
        e_new = hamiltonian(x, y, z,propuesta_params, propuesta_momentum)
        e_old = hamiltonian(x, y, z,params[i-1],momentum[i-1])

        r = min(1,np.exp(-(e_new - e_old)))
        alpha = np.random.random()
        if(alpha<r):
            param.append(propuesta_params)
        else:
            param.append(params[i-1])
        momentum.append(np.random.normal(size=3))

    params= np.array(params)
    return params


# In[ ]:


markov = MCMC(x,y,z,t)


# In[10]:


plt.plot(t,x)
plt.title('x en funcion de t')
plt.xlabel('t')
plt.ylabel('x')
plt.savefig('xvst.png')
plt.close()


# In[12]:


plt.plot(t,y)
plt.title('y en funcion de t')
plt.xlabel('t')
plt.ylabel('y')
plt.savefig('yvst.png')
plt.close()


# In[13]:


plt.plot(t,z)
plt.title('z en funcion de t')
plt.xlabel('t')
plt.ylabel('z')
plt.savefig('zvst.png')
plt.close()


# In[ ]:
