import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
import geradenfit as gf

# {{{ Fadenstrahlrohr

def fadenstrahlrohr():

    data = pd.read_csv("fadenstrahlrohr.csv",sep=',')
    U = np.fromiter(data['U'],dtype=float)
    I = np.fromiter(data['I'],dtype=float)
    I180 = np.fromiter(data['I180'],dtype=float)
    d = 178-np.fromiter(data['d'],dtype=float)

    return U,I,I180,d

# }}}

print(fadenstrahlrohr())

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
