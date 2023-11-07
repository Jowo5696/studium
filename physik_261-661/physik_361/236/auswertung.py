import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
import geradenfit as gf

execute = 'h'

#{{{ c
def c():
    U0 = 2.2 # V
    R1 = 100 # Ohm
    R2 = 5 # Ohm
    R = np.array([100,200,300,400,500,1000,2000,3000,4000,5000]) # Ohm
    vph = np.array([180,122,94,76,64,36,20,15,11,9]) # mm
    delt_vph = np.array([10,7,4,2,2,1,1,1,1,1]) # mm
    delt_vph_G = 1/vph**2*delt_vph

    zusammen = ['end'] # Welche Plots zusammengehören. Gleiche Buchstaben werden in einem Plot ausgegeben (Beispiel: ['a','a','b'], die ersten beiden x, y Werte werden in einem Plot ausgegeben, die dritten x, y, Werte werden in einem Plot ausgegeben).
    x = [R]
    xerr = [np.zeros(len(R))]
    xlabel = r'Widerstand $[\Omega]$'
    y = [1/vph]
    yerr = [delt_vph_G]
    ylabel = r'1/$\varphi$ [1/Skt]'
    title = '236.c Stromempfindlichkeit und Spulenwiderstand'
    label = '236.c' # label von plt.errorbar und plt.plot
    color = ['red'] # farbe der punkte (geraden sind immer blau)
    Auswertung = gf.Auswertung(x,xerr,xlabel,y,yerr,ylabel,title,label,color,zusammen)
    Auswertung.auswertung()

    m = gf.Gerade()
    m,n,vm,vn = m.mnvmvn(x[0],y[0],yerr[0])

    cI = 1/m*(R1+R2)/(U0*R2)
    delt_cI = cI*1/m*vm
    print(cI,delt_cI)

    Rg = n*(cI*U0*R2)/(R1+R2)
    delt_Rg = Rg/n*vn
    print(Rg,delt_Rg)
#}}}

#{{{ g
def g():

    vph = np.array([35,33,29,16,13]) # Skt
    delt_vph = np.zeros(len(vph))+1 # Skr
    I = np.zeros(len(vph))+1.91e-3 # A
    delt_I = np.zeros(len(vph))+0.01e-3 # A 
    cI = vph/I # Skt/A
    delt_cI = np.sqrt((delt_vph/I)**2+(vph/I**2*delt_I)**2) # Skt/A

    data = np.round(np.transpose([I,delt_I,vph,delt_vph,cI,delt_cI]),2)
    headers = ['I [A]','ΔI [A]',r'φ [Skt.]',r'Δφ [Skt]',r'cI [Skt./A]','ΔcI [Skt./A]']
    print('Tabelle 236.g: Stromempfindlichkeit verschiedener Trägheitsmomente')
    print(tabulate(data,headers=headers,tablefmt='fancy_grid'))
#}}}

#{{{ h
def h():
    
    vph = np.array([46,40,37,34,30,28,26,20,12,8]) # Skt
    delt_vph = np.zeros(len(vph))+1 # Skt
    t = np.array([0,2.1,3.1,4.1,5.2,6.1,7.1,10.0,15.1,20.1]) # s
    delt_t = np.zeros(len(t))+0.3 # s

    C = 10e-6 # F
    U0 = 2.2 # V
    
    zusammen = ['end'] # Welche Plots zusammengehören. Gleiche Buchstaben werden in einem Plot ausgegeben (Beispiel: ['a','a','b'], die ersten beiden x, y Werte werden in einem Plot ausgegeben, die dritten x, y, Werte werden in einem Plot ausgegeben).
    x = [t]
    xerr = [delt_t]
    xlabel = 'Zeit [s]'
    y = [np.log(vph)]
    yerr = [delt_vph/vph]
    ylabel = 'logarithmische Auslenkung [Skt]'
    title = '263.h: Ballistisches Galvanometer'
    label = '236.h' # label von plt.errorbar und plt.plot
    color = ['red'] # farbe der punkte (geraden sind immer blau)

    Auswertung = gf.Auswertung(x,xerr,xlabel,y,yerr,ylabel,title,label,color,zusammen)
    Auswertung.auswertung()

    m = gf.Gerade()
    m,n,vm,vn = m.mnvmvn(x[0],y[0],yerr[0])
    R = 1/(m*C)
    delt_R = 1/(m**2*C)*vm
    print(R,delt_R)
#}}}

for char in execute:
    locals()[char]()

# Plot

zusammen = ['end'] # Welche Plots zusammengehören. Gleiche Buchstaben werden in einem Plot ausgegeben (Beispiel: ['a','a','b'], die ersten beiden x, y Werte werden in einem Plot ausgegeben, die dritten x, y, Werte werden in einem Plot ausgegeben).
x = []
xerr = []
xlabel = []
y = []
yerr = []
ylabel = []
title = ''
label = [] # label von plt.errorbar und plt.plot
color = [] # farbe der punkte (geraden sind immer blau)

Auswertung = gf.Auswertung(x,xerr,xlabel,y,yerr,ylabel,title,label,color,zusammen)
Auswertung.auswertung()
