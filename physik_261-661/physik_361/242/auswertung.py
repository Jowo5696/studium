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
    r = (178-np.fromiter(data['d'],dtype=float))*1e-3
    dr = 1e-3

    n = 130
    R = 0.15
    mu0 = 4*np.pi*1e-7

    BS_I = (4/5)**(3/2)*1.256e-6*n*1/R*I
    BS_I180 = (4/5)**(3/2)*1.256e-6*n*1/R*I180

    tabledata = np.round(np.transpose([BS_I,BS_I180]),5)
    tableheaders = ['BS von I [T]','BS von I180 [T]']
    #print('Tabelle 242.b.2.: BS')
    #print(tabulate(tabledata,tableheaders,tablefmt='fancy_grid'))

    tabledata = np.round(np.transpose([U,r**2*I**2,r**2*I180**2]),4)
    tableheaders = ['U [V]','I [A]','I180 [A]']
#    print('Tabelle 242.b.3: Datenpunkte zum Plot')
#    print(tabulate(tabledata,tableheaders,tablefmt='fancy_grid'))

    zusammen = ['end'] # Welche Plots zusammengehören. Gleiche Buchstaben werden in einem Plot ausgegeben (Beispiel: ['a','a','b'], die ersten beiden x, y Werte werden in einem Plot ausgegeben, die dritten x, y, Werte werden in einem Plot ausgegeben).
    x = [np.concatenate((U,U))]
    xerr = [np.concatenate((np.zeros(len(U)),np.zeros(len(U))))]
    xlabel = 'U [V]'
    y = [np.concatenate((r**2*I**2,r**2*I180**2))]
    yerr = [np.concatenate((2*r*dr*I**2,2*r*dr*I**2))]
    ylabel = '(rI)² [m²A²]'
    title = '242.b.3: Bestimmung spezifische Ladung'
    label = '242.a' # label von plt.errorbar und plt.plot
    color = ['r'] # farbe der punkte (geraden sind immer blau)

    Auswertung = gf.Auswertung(x,xerr,xlabel,y,yerr,ylabel,title,label,color,zusammen)
    Auswertung.auswertung()

    Gerade = gf.Gerade()
    m,n,vm,vn = Gerade.mnvmvn(x[0],y[0],yerr[0])

    em = m**(-1)*2*(4/5)**(-3)*R**2*n**(-2)*mu0**(-2)
    dem = vm*m**(-2)*2*(4/5)**(-3)*R**2*n**(-2)*mu0**(-2)

    print(em,dem)
    
    BE = 0.5*(4/5)**(3/2)*mu0*n*(I-I180)/R
    print('BEmittel: ',BE.mean())



# }}}

#fadenstrahlrohr()

# {{{ 242 Millikan

def millikan():

    data = [np.transpose(pd.read_csv('t01.csv',sep=',').to_numpy()),
            np.transpose(pd.read_csv('t02.csv',sep=',').to_numpy()),
            np.transpose(pd.read_csv('t03.csv',sep=',').to_numpy()),
            np.transpose(pd.read_csv('t04.csv',sep=',').to_numpy()),
            np.transpose(pd.read_csv('t05.csv',sep=',').to_numpy()),
            np.transpose(pd.read_csv('t06.csv',sep=',').to_numpy()),
            np.transpose(pd.read_csv('t07.csv',sep=',').to_numpy()),
            np.transpose(pd.read_csv('t08.csv',sep=',').to_numpy()),
            np.transpose(pd.read_csv('t09.csv',sep=',').to_numpy()),
            np.transpose(pd.read_csv('t10.csv',sep=',').to_numpy())]

    #print(data)
    ddata = data

    d = 1e-4
    dg = 5*d
    dd = 0.000025
    ddg = 5*dd

    abweichung = np.ndarray(shape=(len(data),5),dtype=float)
    dabweichung = np.ndarray(shape=(len(data),5),dtype=float)
    for i in range(len(data)):
        for j in range(len(data[i][0])):
            abweichung[i][j] = ((2*dg/data[i][0][j])/(dg/data[i][2][j]-dg/data[i][1][j])-1)*100
            dabweichung[i][j] = ((2*ddg/ddata[i][0][j])/(ddg/ddata[i][2][j]-ddg/ddata[i][1][j])-1)*100
        #print('Tröpfchen',i,abweichung[i])
        #print('delta',i,dabweichung[i])

    v = np.ndarray(shape=(len(data),3,5),dtype=float)
    for i in range(len(data)):
        for j in range(len(data[i][0])):
            v[i][0][j] = dg/data[i][0][j] # v0
            v[i][1][j] = dg/data[i][1][j] # vu
            v[i][2][j] = dg/data[i][2][j] # vd

    # 2 7 8 9 10

    eta = 18.19e-6
    g = 9.81
    rho_öl = 886.0
    rho_luft = 1.225

    d_K = 7.67e-3
    U = 500
    E = U/d_K

    for i in [1,6,7,8,9]:
        r = np.sqrt((9*eta*np.abs((v[i][2][:]-v[i][1][:])))/(4*g*(rho_öl-rho_luft)))
        print(i,'r',r)
        Ne = 3*np.pi*eta*r*(v[i][2][:]+v[i][1][:])/E
        print(i,'Ne',Ne)

    plt.plot([2,7,8,9,10],Ne,ls='',color='r',marker='d')
    plt.grid()
    plt.show()

# }}}

millikan()

# Plot

#zusammen = ['end'] # Welche Plots zusammengehören. Gleiche Buchstaben werden in einem Plot ausgegeben (Beispiel: ['a','a','b'], die ersten beiden x, y Werte werden in einem Plot ausgegeben, die dritten x, y, Werte werden in einem Plot ausgegeben).
#x = []
#xerr = []
#xlabel = ''
#y = []
#yerr = []
#ylabel = ''
#title = ''
#label = '' # label von plt.errorbar und plt.plot
#color = [] # farbe der punkte (geraden sind immer blau)

#Auswertung = gf.Auswertung(x,xerr,xlabel,y,yerr,ylabel,title,label,color,zusammen)
#Auswertung.auswertung()
