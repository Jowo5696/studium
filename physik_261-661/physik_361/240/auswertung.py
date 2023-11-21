import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
import geradenfit as gf

data = np.transpose(pd.read_csv('240_b_messung_1.csv',sep='\t').to_numpy())
data = data[0:2,:]
data = np.transpose(data)
data[:,1] = data[:,1]*1e-3 # B [T]
data[:,0] = data[:,0]*(-1) # I [A]

N = 500
lFe = 477e-3
dlFe = 4e-3
d = 2e-3
dd = 0.05e-3
mu_0 = 4*np.pi*1e-7

H = np.ndarray(shape=np.shape(data))
H[:,0] = (-1)*(N*data[:,0]/lFe-d/(mu_0*lFe)*data[:,1])
H[:,1] = data[:,1]
print(H[110:120,:])

H = pd.DataFrame(H,columns=['H','B'])
H.to_csv(path_or_buf='240_b_messung_1_H_und_B.dat',sep=' ')

# Plot

zusammen = ['end'] # Welche Plots zusammengehören. Gleiche Buchstaben werden in einem Plot ausgegeben (Beispiel: ['a','a','b'], die ersten beiden x, y Werte werden in einem Plot ausgegeben, die dritten x, y, Werte werden in einem Plot ausgegeben).
x = []
xerr = []
xlabel = ''
y = []
yerr = []
ylabel = ''
title = ''
label = '' # label von plt.errorbar und plt.plot
color = [] # farbe der punkte (geraden sind immer blau)

Auswertung = gf.Auswertung(x,xerr,xlabel,y,yerr,ylabel,title,label,color,zusammen)
Auswertung.auswertung()
