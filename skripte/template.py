import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
import geradenfit as gf



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
