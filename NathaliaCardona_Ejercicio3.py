import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

#a,b son las caras de una moneda
def posterior(s):
    #prior p(a)
    n = 1000
    pa = np.linspace(0,1,n)
    prior = np.ones(n)
    #numero de a en s
    n_a = s.count("a")
    n_b = len(s)-n_a
    lh = (pa**n_a)*(1-pa)**n_b
    posterior = lh*prior
    norm = integrate.simps(posterior,pa)

    posterior = posterior/norm
    #mas probable
    i = posterior==max(posterior)
    p_max = pa[i]
    #valor medio
    E = integrate.simps(pa*posterior,pa)
    #desviacion
    E2 = integrate.simps(posterior*(pa**2),pa)
    sigma = (E2-E**2)**0.5
    #grafica
    plt.plot(pa,posterior)
    plt.title("Mas probable = " + "{:.4f}".format(p_max[0]) + " Valor medio = " + "{:.4f}".format(E) + " Sigma = " + "{:.4f}".format(sigma))
    plt.xlabel("Pa")
    plt.ylabel("P(Pa|S)")
    plt.savefig("posterior.pdf")
    plt.close()
















#pruebas
s = "aba"
s = "bbb"
