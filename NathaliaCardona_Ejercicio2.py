import numpy as np
import matplotlib.pyplot as plt


#Punto 1.1
a = np.random.random((4,8))
a[:,0] = -1
a[1,:] = 2
print (a)

#Punto 1.2
b=np.random.normal(size=1000)
cont = 0
for i in range(len(b)):
    if(b[i]>2.0):
        cont+=1
print (cont)

#Punto 1.3
c = b
#Genera indices false y true cuando se cumple con la condicion o no, solo se cambia en los indices que cumplen
c[b<0]=-1
c[b>=0]=2

#Punto 4.1
a=5
b=4
delta = np.pi/2
t = np.linspace(0, 100, 1000)
x = np.sin(a*t + delta)
y = np.sin(b*t)
plt.plot(x,y)
plt.savefig("grafica1.png")
plt.close()

#Punto 4.2.1
def puntos2D(N):
    #coordenadas polares
    r = np.sqrt(np.random.random(N))
    tetha = np.random.random(N)*np.pi*2
    #regresar a cartesianas
    x = r*np.cos(tetha)
    y = r*np.sin(tetha)
    return x,y

x,y = puntos2D(1000)
plt.scatter(x,y)
plt.savefig("grafica2.png")
plt.close()

#Punto 4.2.2
def puntos3D(N):
    #coordenadas polares
    r = 1
    tetha = np.random.random(N)*np.pi*2
    phi = np.arccos(2*np.random.random(N)-1)
    #regresar a cartesianas
    x = r*np.sin(phi)*np.cos(tetha)
    y = r*np.sin(tetha)*np.sin(phi)
    z = r*np.cos(phi)
    return x,y,z

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x,y,z = puntos3D(2000)
ax.scatter(x, y, z, c='r', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.savefig("grafica3.png")
