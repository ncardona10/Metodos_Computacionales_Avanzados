import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
def lh():
    edades_maximas = []
    #edades
    for i in range(0,100):
        #intentos
        for j in range(10000):
            poblacion = np.random.randint(0,i+1,1000)
            muestra = np.random.choice(poblacion,2)
            if(max(muestra) == 40):
                edades_maximas.append(i)
    return edades_maximas
temp = lh()
edades = plt.hist(temp, bins = 100,density=True)
x=edades[1][:-1]
y=edades[0]/sum(edades[0])
valor_max=x[y==max(y)]
valor_medio =sum(x*y)
sigma = np.sqrt(sum((x**2)*y)-sum(x*y)**2)

plt.hist(temp, bins = 100,density=True)
plt.title("E. max.= "+ "{:.4f}".format(valor_max[0]) + "Valor medio= " + "{:.4f}".format(valor_medio) + "Desviacion estandar= " "{:.4f}".format(sigma))
plt.savefig("histograma.pdf")
plt.close()
