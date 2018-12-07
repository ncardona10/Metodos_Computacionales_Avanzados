import numpy as np   
import matplotlib.pyplot as plt      

x_obs = np.array([-2.0,1.3,0.4,5.0,0.1, -4.7, 3.0, -3.5,-1.1])
y_obs = np.array([ -1.931,   2.38,   1.88,  -24.22,   3.31, -21.9,  -5.18, -12.23,   0.822])
sigma_obs = np.array([ 2.63,  6.23, -1.461, 1.376, -4.72,  1.313, -4.886, -1.091,  0.8054])

mu_a = -1
mu_b = 0
mu_c = 2

sigma_a = 5
sigma_b = 5
sigma_c = 5

def model(x,a,b,c):
    return a*x**2 + b*x + c

def log_likelihood(a, b, c):
    d = np.sum(-(y_obs-model(x_obs,a,b,c))**2/(2*sigma_obs**2))
    return d

def log_prior(a, b, c):
    p = -np.inf
    if a <=5 and a>-100 and c > -10 and c < 10 and b >-20 and b<20:
        p = 0.0
    return p

def gradient_log_a(a, b, c, sigma_a, x_obs, y_obs, sigma_z, mu_a):
    parte1 = (np.log(1/(sigma_a*np.sqrt(2*np.pi)))*(a-mu_a))/sigma_a**2
    parte2 = (y_obs-model(x_obs,a,b,c))*(x_obs**2)
    return parte1 + np.sum(parte2)  

def gradient_log_b(a, b, c, sigma_b, x_obs, y_obs, sigma_z, mu_b):
    parte1 = (np.log(1/(sigma_b*np.sqrt(2*np.pi)))*(b-mu_b))/sigma_b**2
    parte2 = (y_obs-model(x_obs,a,b,c))*(x_obs)
    return parte1 + np.sum(parte2)

def gradient_log_c(a, b, c, sigma_c, x_obs, y_obs, sigma_z, mu_c):
    parte1 = (np.log(1/(sigma_c*np.sqrt(2*np.pi)))*(c-mu_c))/sigma_c**2
    parte2 = y_obs-model(x_obs,a,b,c)
    return parte1 + np.sum(parte2)

def leapfrog_a(a, b, c,pa, sigma_a, mu_a, x_obs, y_obs, sigma_z, d_t = 1E-1, iteraciones = 5):
    a_new = a
    p_new = pa
    for i in range(iteraciones):
        p_new = p_new + 0.5 * d_t * gradient_log_a(a_new, b, c,sigma_a, x_obs, y_obs, sigma_z, mu_a) #kick
        a_new = a_new + d_t * p_new 
        p_new = p_new + 0.5 * d_t * gradient_log_a(a_new, b, c, sigma_a, x_obs, y_obs, sigma_z, mu_a) #kick
    return a_new, p_new

def leapfrog_b(a, b, c,pb, sigma_b, mu_b, x_obs, y_obs, sigma_z, d_t = 1E-1, iteraciones = 5):
    b_new = b
    p_new = pb
    for i in range(iteraciones):
        p_new = p_new + 0.5 * d_t * gradient_log_b(a,b_new, c, sigma_b, x_obs, y_obs, sigma_z, mu_b) #kick
        b_new = b_new + d_t * p_new 
        p_new = p_new + 0.5 * d_t * gradient_log_b(a,b_new, c, sigma_b, x_obs, y_obs, sigma_z, mu_b) #kick
    return b_new, p_new

def leapfrog_c(a, b, c, pc,sigma_c, mu_c, x_obs, y_obs, sigma_z, d_t = 1E-1, iteraciones = 5):
    c_new = c
    p_new = pc
    for i in range(iteraciones):
        p_new = p_new + 0.5 * d_t * gradient_log_c(a, b, c_new, sigma_c, x_obs, y_obs, sigma_z, mu_c) #kick
        c_new = c_new + d_t * p_new 
        p_new = p_new + 0.5 * d_t * gradient_log_c(a, b, c_new, sigma_c, x_obs, y_obs, sigma_z, mu_c) #kick
    return c_new, p_new

def H(a,b,c,p_a, p_b, p_c):
    l1 = (p_a**2 + p_b**2 + p_c**2)/2
    l2=  -log_likelihood( a, b, c)-(np.log(1/sigma_a*2*np.pi)*(a-mu_a)**2/(2*sigma_a)+np.log(1/sigma_b*2*np.pi)*(b-mu_b)**2/(2*sigma_b)+np.log(1/sigma_a*2*np.pi)*(c-mu_c)**2/(2*sigma_c))
    return l1 + l2

def MCMC(nsteps):
    a = np.zeros(nsteps)
    pa = np.zeros(nsteps)
    b = np.zeros(nsteps)
    pb = np.zeros(nsteps)
    c = np.zeros(nsteps)
    pc = np.zeros(nsteps)
    
    pa[0] = np.random.normal(0,1)
    a[0] = np.random.normal(0,1)
    pb[0] = np.random.normal(0,1)
    b[0] = np.random.normal(0,1)
    pc[0] = np.random.normal(0,1)
    c[0] = np.random.normal(0,1)
       
    for i in range(1,nsteps):
        pa[i] = np.random.normal(0,1)
        a_new, pa_new = leapfrog_a(a[i-1],b[i-1],c[i-1],pa[i-1],sigma_a, mu_a,x_obs, y_obs, sigma_obs) 
        pa_new = -pa_new 
        
        pb[i] = np.random.normal(0,1)
        b_new, pb_new = leapfrog_b(a[i-1],b[i-1],c[i-1],pb[i-1], sigma_b, mu_b, x_obs, y_obs, sigma_obs) 
        pb_new = -pb_new 
        
        pc[i] = np.random.normal(0,1)
        c_new, pc_new = leapfrog_c(a[i-1],b[i-1],c[i-1],pc[i-1], sigma_c, mu_c,x_obs, y_obs, sigma_obs) 
        pc_new = -pc_new 
        
        E_new = H(a[i-1],b[i-1],c[i-1],pa_new, pb_new, pc_new) 
        E_old = H(a[i-1],b[i-1],c[i-1], pa[i-1],pb[i-1],pc[i-1])
        alpha = min(1.0,np.exp(-(E_new - E_old))) 
        beta = np.random.random()
        if beta < alpha:
            a[i] = a_new
            b[i] = b_new
            c[i] = c_new
        else:
            a[i] = a[i-1]
            b[i] = b[i-1]
            c[i] = c[i-1]
    return a,b,c

a,b,c = MCMC(10000)
#GRAFICA
xd = np.linspace(-5,5,100)
z_model = model(xd,np.mean(a),np.mean(b), np.mean(c))
plt.errorbar(x_obs, y_obs, yerr=sigma_obs, fmt='o')
plt.plot(xd, z_model,c="red")
plt.savefig("montecarlo.png")
plt.close()