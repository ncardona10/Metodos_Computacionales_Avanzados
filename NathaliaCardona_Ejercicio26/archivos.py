import matplotlib
matplotlib.use("Agg")
import os
#abre el archivo y guarda el contenido en una variable
inFile = open('Pi_2500000.txt','r')
cont = inFile.read()
inFile.close()

# funcion que divide el archivo en n partes y las guarda en carpetas
def partir(n):
    lenPart = (int)(len(cont)/n)
    carpeta = 'part'+str(n)
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    for i in range(n):
        direccion = carpeta + '/pi' + str(i+1) + '.txt'
        escribir = open(direccion,'w')
        escribir.write(cont[i*lenPart:(i+1)*lenPart])
        escribir.close()
#llama la funcion para todas las particiones que se quieren
part = [1,10,20,50,100]

for i in part:
    partir(i) 


