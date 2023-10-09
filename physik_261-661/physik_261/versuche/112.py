import numpy as np
import matplotlib.pyplot as plt
import geradenfit as gf

dT = 1
dl = np.ndarray(shape=(3,20),dtype=float)
dl[0] = np.zeros(20)+0.01
dl[1] = np.zeros(20)+0.01
dl[2] = np.zeros(20)+0.01

T0 = 21
l0 = 49.0

l_Alu = np.array([0.05,0.08,0.11,0.13,0.14,0.19,0.23,0.26,0.3,0.34,0.37,0.41,0.44,0.47,0.5,0.53,0.57,0.6,0.64,0.66])
l_Karbon = np.array([0,0,0,0,0,0,0,0,0,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05])
l_Stahl = np.array([0.02,0.05,0.07,0.09,0.12,0.14,0.16,0.19,0.21,0.24,0.26,0.29,0.31,0.33,0.36,0.38,0.42,0.44,0.47,0.5])

DT = np.ndarray(shape=(3,20),dtype=float)
DT[0] = np.array([3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60])
DT[1] = np.array([3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60])
DT[2] = np.array([3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60])

Dl = np.ndarray(shape=(3,20),dtype=float)
Dl[0] = l_Alu
Dl[1] = l_Karbon
Dl[2] = l_Stahl

x = np.ndarray(shape=(3,20),dtype=float)
y = np.ndarray(shape=(3,20),dtype=float)
yerr = np.ndarray(shape=(3,20),dtype=float)
nmvnvm = np.ndarray(shape=(3,4),dtype=float)
gerade = np.ndarray(shape=(3,20),dtype=float)
Fit = gf.gerade()

x = DT*l0
print('x',x)
y = Dl
print('y',y)
yerr = dl
print('yerr',yerr)

for i in range(3):
    nmvnvm[i] = Fit.nmvnvm(x=x[i],y=y[i],yerr=yerr[i])
    gerade[i] = nmvnvm[i][1]*x[i]+nmvnvm[i][0]
    plt.plot(x[i],gerade[i],'r')
    plt.errorbar(x=x[i],y=y[i],yerr=yerr[i],ls="",marker="d")

plt.show()
print('nmvnvm',nmvnvm)
