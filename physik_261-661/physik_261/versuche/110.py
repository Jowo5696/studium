import numpy as np
import matplotlib.pyplot as plt
import geradenfit as gf


aZeit = np.array([0,30,60,90,120,150,180,210,240,270,300,330,360,390,420,450,480,510,540,570,600,630,660,670,680,690,700,710,720,730,740,750,760,770,780,790,800,830,860,890,920,950,1010]) #[s]
aTemp_Wasser_Aluminium = np.array([19.8,19.8,19.8,19.8,19.9,20.0,20.0,19.9,20.0,20.0,20.0,20.0,20.0,20.1,20.1,20.2,20.3,20.3,20.3,20.4,20.4,20.4,20.5])


Tg = np.array([35.2,38.6,39.1])
delta = 0.5
T1 = 99.6
Tk = 20.5
Ck = 619.7
dCk = ((4184*0.001)**2+(377*0.001)**2)**0.5
lcs = np.array([897,382,477])
m = np.array([0.155, 0.505, 0.446])
u = np.array([26.9,63.5,0.09*58.7+0.18*52+0.73*55.8])*1.661*10**(-27)
mole = 6.022*10**23
n = u*mole
M = m/n
R = 8.314
#print('M',M)

#print('dCk',dCk)

C = np.array([0,0,0])
delta_C = np.array([0,0,0])

C = Ck*((Tg-Tk)/(T1-Tg))
delta_C = ((Ck*(T1-Tk)*(T1-Tg)**(-2)*delta)**2+(Ck*(Tg-T1)**(-1)*delta)**2+(Ck*(Tg*(-1)+Tk)*(Tg*(-1)+T1)**(-2)*delta)**2+((Tk-Tg)*(T1-Tg)**(-1)*dCk)**2)**0.5

cs = C/m
delta_cs = delta_C/m

cm = C/M
delta_cm = delta_C/M

#print('C',C)
#print('delta_C',delta_C)
#print('cs',cs)
#print('delta_cs',delta_cs)
#print('Abweichung',(cs/lcs-1))
#print('cm',cm)
#print('delta_cm',delta_cm)
#print('Abweichung',(3*R),(cm/(3*R)-1))

m = np.array([0.0045,0.0071,0.0094])
d_m = np.zeros(len(m))+0.001
T = np.array([0.34,0.43,0.48])
d_T = np.zeros(len(T))+0.01
r = np.zeros(len(m))+0.00595
d_r = np.zeros(len(r))+0.00005
p0 = np.array([102196.9,102426.2,102629.1])
d_p0 = np.array([11.1,13.7,16.5])
d_pL = 50
V0 = 0.001141
g = 9.81

dp0 = (((g*d_m)/(np.pi*r**2))**2+((2*m*g*d_r)/(np.pi*r**3))**2+d_pL**2)**0.5
print('dp0',dp0)

kappa = (4*V0*m)/(T**2*r**4*p0)
d_kappa = (((4*V0)/(T**2*r**4*p0)*d_m)**2+((2*4*V0*m)/(T**3*r**4*p0)*d_T)**2+((5*4*V0*m)/(T**2*r**5*p0)*d_r)**2+((4*V0*m)/(T**2*r**4*p0**2)*dp0)**2)**0.5

print('kappa',kappa)
print('d_kappa',d_kappa)
print('m_kappa',(kappa.sum()/3))
print('m_d_kappa',(d_kappa.sum()/3))
