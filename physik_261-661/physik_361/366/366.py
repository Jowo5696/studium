import numpy as np

def e():

    gamma = 60*np.pi/180
    Dgamma = 0.012*np.pi/180
    delta = np.array([47.300,48.317,48.349,48.667,49.099,49.550,49.783,50.533,51.467])*np.pi/180
    Ddelta = 0.017*np.pi/180

    n = np.sin((delta+gamma)/2)/np.sin(gamma/2)
    Dn = ( (0.5*np.cos((gamma+delta)/2)*Ddelta*1/np.sin(gamma/2))**2 + ( (0.5*np.cos((gamma+delta)/2)*1/np.sin(gamma/2)-np.sin((gamma+delta)/2)*0.5*1/np.cos(gamma/2))*Dgamma )**2 )**0.5
    n_mittel = n.sum()/9
    Dn_mittel = Dn.sum()/9

    wellenlänge = (np.array([643.85,579.06,576.96,546.08,508.58,479.99,467.81,435.83,404.66])*1e-9)**(-2)*1e-10

    for i in range(len(n)):
        print(np.round(wellenlänge[i],2),'&',np.round(n[i],5),'&',np.round(Dn[i],5),'&','\\\\')

def e2():

    lam = np.array([400,500,600])*1e-9
    k1 = 0.0106*1e-12
    Dk1 = 0.0004*1e-12
    b = 32.5*1e-3
    Db = 0.5*1e-3

    A = 2*k1*1/(lam**3)*b
    DA = ( (2*1/lam**3*b*Dk1)**2 + (2*k1*1/lam**3*Db)**2 )**0.5

    dlam = lam/A
    Ddlam = lam/A**2*DA

    print('A: ',A)
    print('DA: ',DA)
    print('dlam: ',dlam)
    print('Ddlam: ',Ddlam)

    

e2()
