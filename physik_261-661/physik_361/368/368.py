import numpy as np


def b():

    m = np.arange(1,10)
    x = 28.86e-3-np.array([26.80,24.90,23.39,21.58,19.84,18.07,16.52,14.73,13.06])*1e-3
    Dx = 0.1e-3

    D = 0.1e-3
    DD = 0.001e-3
    
    f = 29.2e-2
    Df = 0.5e-3

    mg = 0.0017
    Dmg = 1.004e-5

    Dlam = ((DD/f*mg)**2 + (D/f**2*mg*Df)**2 + (D/f*Dmg)**2)**0.5

#    for i in range(len(m)):
#        print(m[i],x[i],)Dx)
#        print(m[i],'&',np.round(x[i],4),'$\pm$',Dx,r'\\')

def c():

    B = 1.0e-2
    DB = 0.2e-3

    b = 61.0e-2
    Db = 1.0e-2

    g = 10.5e-2
    Dg = 0.2e-2
    
    Dd = ((DB/b*g)**2 + (B/b**2*g*Db)**2 + (B/b*Dg)**2)**0.5

    print(Dd)

def d():

    m = np.arange(1,9)
    lam = 546.07e-9

    a = np.array([55.55,61.15,66.7,72.35,78.0,83.6,89.3,95.0,44.40,38.85,33.30,27.70,22.15,16.55,10.90,5.30])*1e-2
    Da = 0.05e-2

    phi = (a[0:8]-a[8:])/2
    Dphi = ((Da/2)**2 + (Da/2)**2)**0.5

    g = m*lam/2/np.sin(phi/2)
    Dg = m*lam/(2*np.sin(phi/2)**2)*np.cos(phi/2)*1/2*Dphi

    g_mittel = g.sum()/len(g)
    Dg_mittel = Dg.sum()/len(Dg)

#    for i in range(len(phi)):
#        print(m[i],'&',g[i],'\pm',Dg[i])

#    print(g_mittel,Dg_mittel)

def e():

    m = np.arange(1,9)
    
    g = 9.81e-6
    Dg = 0.02e-6

    a = np.array([45.55,41.1,36.65,32.2,27.8,23.3,18.8,14.4,54.4,58.9,63.30,67.8,72.3,76.8,81.3,85.85])*1e-2
    Da = 0.05e-2

    phi = (a[0:8]-a[8:])/2
    Dphi = ((Da/2)**2 + (Da/2)**2)**0.5

    lam = 2*g*np.sin(phi/2)/m
    Dlam = ((2*g*np.cos(phi/2)*1/2*Dphi)**2 + (2*Dg*np.sin(phi/2))**2)**0.5

    lam_mittel = lam.sum()/len(lam)
    Dlam_mittel = Dlam.sum()/len(Dlam)

    for i in range(len(lam)):
        print(m[i],'&',-1*lam[i],'\pm',Dlam[i])

def f():

    G = np.array([.2,.2,.2])*1e-2
    DG = np.array([.05,.05,.05])*1e-2

    dTW = 1.635
    DdTW = 0.005

    b_strich = np.array([114,111.3,108.9])*1e-2
    Db_strich = np.array([.3,.3,.3])*1e-2

    b = dTW + b_strich
    Db = ((DdTW)**2 + (Db_strich)**2)**0.5

    g = np.array([6,6,6])*1e-2
    Dg = np.array([.1,.1,.1])*1e-2

    d = G/b*g
    Dd = ((DG/b*g)**2 + (G/b**2*g*Db)**2 + (G/b*Dg)**2)**0.5

    print(d)

    N = d/9.81e-6
    DN = ((Dd)**2 + (d/(9.81e-6)**2*0.02e-6)**2)**0.5

    print(N,DN)

e()
