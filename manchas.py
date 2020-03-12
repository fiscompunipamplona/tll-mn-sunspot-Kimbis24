from numpy import loadtxt
from pylab import plot,show, xlabel,ylabel,xlim

#Parte a) Lea los datos y grafique.
a=loadtxt("sunspots.txt", float)
plot(a[:,0],a[:,1])
xlabel("Mes")
ylabel("Numero de manchas")
show()

#Parte b) Grafique solo los primeros 1000 datos
plot(a[:,0],a[:,1],"g")
xlim(0,1001)
xlabel("Mes")
ylabel("Numero de manchas")
show()

