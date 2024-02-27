import numpy as np

def zehn():

    gamma_M = 155000
    Dgamma_M = 2000
    gamma_obj = 1111.11
    Dgamma_obj = 12.35
    s0 = 25e-1
    b = 35e-1
    Db = 0.5e-1

    Dv_oku = ( ((Dgamma_M*s0)/(gamma_obj*b))**2 + ((gamma_M*s0*Dgamma_obj)/(gamma_obj**2*b))**2 + ((gamma_M*s0*Db)/(gamma_obj*b**2))**2 )**0.5

    print(Dv_oku)

def fuenf():

    gamma_M = 136000
    Dgamma_M = 4000
    gamma_obj = 1886.79
    Dgamma_obj = 35.60
    s0 = 25e-1
    b = 35e-1
    Db = 0.5e-1

    v_oku = (gamma_M*s0)/(gamma_obj*b)
    Dv_oku = ( ((Dgamma_M*s0)/(gamma_obj*b))**2 + ((gamma_M*s0*Dgamma_obj)/(gamma_obj**2*b))**2 + ((gamma_M*s0*Db)/(gamma_obj*b**2))**2 )**0.5

    print(v_oku,Dv_oku)

def brennweite_objektiv():

    t1 = 6e-1
    t2 = 12e-1
    Dt = 0.1e-1
    gamma1 = 445000
    Dgamma1 = 5000
    gamma2 = 645000
    Dgamma2 = 5000

    Df_obj = ( (t1/(gamma2-gamma1)*Dt)**2 + (t2/(gamma2-gamma1)*Dt)**2 + ((t2-t1)/(gamma2-gamma1)**2*Dgamma2)**2 + ((t2-t1)/(gamma2-gamma1)**2*Dgamma1)**2 )**0.5

    print(Df_obj)

def alpha():

    E = 6.63
    DE = 0.02
    G = np.array([7.6,6,3,1.8])*1/2*1e-2*2*np.pi*1/36
    DG = 0.4e-2*1/2*2*np.pi*1/36

    alpha = G/E
    Dalpha = ( (DG/E)**2 + (G/E**2*DG)**2 )**0.5

    print(alpha,Dalpha)
    print(G*1e+2,DG*1e+2)

alpha()
