import numpy as np 
import matplotlib.pyplot as plt  

data = np.loadtxt('tiempos.txt')


y = [[],[],[],[],[]]
errors = [[],[],[],[],[]]

parts = [1,10,20,50,100]
procesa = [1,2,4,8]
for i in range(len(parts)):
    for j,pross in enumerate(procesa):
        data = np.loadtxt('timePart'+str(parts[i])+'p'+str(pross)+'.txt')
        y[j].append(np.mean(data))  
        errors[j].append(np.std(data))  


for i in range(len(procesa)):

    plt.errorbar(parts,y[i],errors[i],label=str(procesa[i])+" procesadores")
plt.xlabel('Particiones')
plt.ylabel('Tiempo corriendo')
plt.title('Tiempos en c++, dadas n particiones')
plt.legend()
plt.xlim(-1,110)
plt.savefig('tiempos_procesadores.png')
#plt.show()




