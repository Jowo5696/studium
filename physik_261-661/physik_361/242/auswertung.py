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

#    Auswertung = gf.Auswertung(x,xerr,xlabel,y,yerr,ylabel,title,label,color,zusammen)
#    Auswertung.auswertung()

    Gerade = gf.Gerade()
    m,n,vm,vn = Gerade.mnvmvn(x[0],y[0],yerr[0])

    em = m**(-1)*2*(4/5)**(-3)*R**2*n**(-2)*mu0**(-2)
    dem = vm*m**(-2)*2*(4/5)**(-3)*R**2*n**(-2)*mu0**(-2)

    print('em,dem',em,dem)
    
    BE = 0.5*(4/5)**(3/2)*mu0*n*(I-I180)/R
#    print('BEmittel: ',BE.mean())

    return em,dem


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
    dv = np.ndarray(shape=(len(data),3,5),dtype=float)
    for i in range(len(data)):
        for j in range(len(data[i][0])):
            v[i][0][j] = dg/data[i][0][j] # v0
            dv[i][0][j] = ddg/data[i][0][j] # v0
            v[i][1][j] = dg/data[i][1][j] # vu
            dv[i][1][j] = ddg/data[i][1][j] # vu
            v[i][2][j] = dg/data[i][2][j] # vd
            dv[i][2][j] = ddg/data[i][2][j] # vd

    # 2 7 8 9 10

    eta = 18.19e-6
    g = 9.81
    rho_öl = 886.0
    rho_luft = 1.2041

    d_K = 7.67e-3
    U = 500
    E = U/d_K

    tabledata = np.round(np.transpose([v[0][2][:],v[0][1][:],v[6][2][:],v[6][1][:],v[7][2][:],v[7][1][:],v[8][2][:],v[8][1][:],v[9][2][:],v[9][1][:]]),6)
    tableheaders = ['T1 vu','T1 vd','T6 vu','T6 vd','T7 vu','T7 vd','T8 vu','T8 vd','T9 vu','T9 vd']
    #print('Tabelle 242.e: Geschwindigkeiten')
    #print(tabulate(tabledata,tableheaders,tablefmt='fancy_grid'))

    #for i in [1,6,7,8,9]:
    #    print(i,'up',v[i][1][:],'±',dv[i][1][:])
    #    print(i,'down',v[i][2][:],'±',dv[i][2][:])

    for i in [1,6,7,8,9]:
        r = np.sqrt((9*eta*np.abs((v[i][2][:]-v[i][1][:])))/(4*g*(rho_öl-rho_luft)))
        dr = np.sqrt((0.5*r**(-1)*(9*eta/(4*g*(rho_öl-rho_luft)))*dv[i][1][:])**2+(0.5*r**(-1)*(9*eta/(4*g*(rho_öl-rho_luft)))*dv[i][2][:])**2)
        print(i,'r',np.mean(r),'±',np.mean(dr))
        Ne = 3*np.pi*eta*r*(v[i][2][:]+v[i][1][:])/E
        dNe = np.sqrt((3*np.pi*eta*(v[i][1][:]+v[i][2][:])/E*dr)**2+(3*np.pi*eta*r*1/E*dv[i][2][:])**2+(3*np.pi*eta*1/E*dv[i][1][:])**2)
    #    dNe = ((3*np.pi*eta*1/E*dv[i][2][:])**2 + (3*np.pi*eta*1/E*dv[i][1][:])**2 + (3*np.pi*eta*1/E*dr*(v[i][1][:]+v[i][2][:]))**2)**(1/2)
        print(i,'Ne',np.mean(Ne),'±',np.mean(dNe))
        #dq = np.sum((dq_notsumed/dq_notsumed.shape[0])**2, axis=1)**(1/2)
    
    #print(np.transpose([r[0],dr[0],Ne[0],dNe[0]]))
#    r = np.round(r*1e+7,2)
#    dr = np.round(dr*1e+7,2)
#    Ne = np.round(Ne*1e+20,2)
#    dNe = np.round(dNe*1e+14,2)
    tabledata1 = [['T1 (r±dr)*10^7',r[0],dr[0]],['T1 Ne*10^20±dNe*10^14',Ne[0],dNe[0]],['T7 (r±dr)*10^7',r[1],dr[1]],['T7 Ne*10^20±dNe*10^14',Ne[1],dNe[1]],['T8 (r±dr)*10^7',r[2],dr[2]],['T8 Ne*10^20±dNe*10^14',Ne[2],dNe[2]],['T9 (r±dr)*10^7',r[3],dr[3]],['T9 Ne*10^20±dNe*10^14',Ne[3],dNe[3]],['T10 (r±dr)*10^7',r[4],dr[4]],['T10 Ne*10^20±dNe*10^14',Ne[4],dNe[4]],]
    tableheaders1 = ['T1 r','T1 dr','T1 Ne','T1 dNe']
    print('Tabelle 242.g: Radien und Ladungen')
    print(tabulate(tabledata1,tablefmt='fancy_grid'))


    #font = {"fontname":"Computer Modern", "family":"serif"}
    #plt.errorbar([2,7,8,9,10],Ne,ls='',color='r',marker='d',label='Gesamtladung Messwerte',capsize=3,linewidth=0.5)
    #plt.plot([2,7,8,9,10],Ne,ls='',color='r',marker='d',label='Gesamtladung Messwerte')
    #plt.xlabel('Tröpfchen [#]',font)
    #plt.ylabel('Ne [C]',font)
    #plt.legend(loc='best')
    #plt.grid()
    #plt.savefig('242_h_graph.png')
    #plt.show()

    dNe = np.array([5.4,30,2.8,3.1,2.4])*10**(-20)

    #print(np.gcd.reduce([605,565,585,575,505]))
    print('gemeinsamer teiler',Ne/1.602)
    e = np.zeros(len(Ne))
    de = np.zeros(len(Ne))
    e[0] = Ne[0]/4
    e[1] = Ne[1]/3
    e[2] = Ne[2]/3
    e[3] = Ne[3]/2
    e[4] = Ne[4]/3
    de[0] = dNe[0]/3
    de[1] = dNe[1]/3
    de[2] = dNe[2]/3
    de[3] = dNe[3]/3
    de[4] = dNe[4]/3
    print('elementarladung mit gemeinsame teiler',e,de)

    zusammen = ['end'] # Welche Plots zusammengehören. Gleiche Buchstaben werden in einem Plot ausgegeben (Beispiel: ['a','a','b'], die ersten beiden x, y Werte werden in einem Plot ausgegeben, die dritten x, y, Werte werden in einem Plot ausgegeben).
    x = [1/r]
    xerr = [1/r**2*dr]
    xlabel = 'Radius [1/m]'
    y = [e**(2/3)]
    yerr = [(2/3)*e**(2/3-1)*de]
    ylabel = r'e$^{2/3}$ (ohne Korrektur)'
    title = '242.i: Elementarladung'
    label = 'Elementarladung' # label von plt.errorbar und plt.plot
    color = ['r'] # farbe der punkte (geraden sind immer blau)

#    Auswertung = gf.Auswertung(x,xerr,xlabel,y,yerr,ylabel,title,label,color,zusammen)
#    Auswertung.auswertung()

    e0 = (1.087e-12)**(3/2)
    de0 = (3/2)*(1.087e-12)**(3/2-1)*(1.507e-13)

    dem = 1.6e+5
    em = 1.751e+11
    me = e0/em
    dme = np.sqrt((de0/em)**2+(e0/em**(-2)*dem)**2)
    print('masse',me,dme)



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
