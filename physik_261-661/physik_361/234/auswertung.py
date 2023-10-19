import numpy as np
from sympy import *
import matplotlib.pyplot as plt
import geradenfit as gf

# Konstanten



# Messewrte
#   Messwerte: aufgabeMessung = np.array([]) #Einheit
#   Fehler: d_aufgabeMessung = np.zeros(len(Messwerte))+Fehler / np.array([]) #Einheit

# a NOCHMAL MACHEN
a_Hertz = 400
a_Spannung = 10
a_Widerstand = 934 
a_deltaWiderstand = 2
a_C1 = 20e-6
a_Rx = a_Widerstand
a_Ry = 1000-a_Widerstand
delt_a_R = 2
a_PotentiometerSpannung = 200

a_Rx_Ohm = (a_Rx*200)/1000
a_Ry_Ohm = (a_Ry*200)/1000
delt_a_R_Ohm = (delt_a_R*200)/1000
#print(a_Rx_Ohm,a_Ry_Ohm,delt_a_R_Ohm)

#a_Cx = a_C1*(a_Rx_Ohm/a_Ry_Ohm)
a_Cx = a_C1*(a_Rx_Ohm/a_Ry_Ohm)
delt_a_Cx = np.sqrt((a_C1*(delt_a_R_Ohm/a_Ry_Ohm))**2+(a_C1*(a_Rx_Ohm/a_Ry_Ohm**2)*delt_a_R_Ohm)**2)

#print(a_Cx,delt_a_Cx)


# b NOCHMAL MACHEN
b_Potentiometer1_max = 200
b_Potentiometer2_max = 200
b_Potentiometer1 = 490 # skalar für R2
b_deltaPotentiometer1 = 2
b_Potentiometer2 = 500 # skalar für R2?
b_deltaPotentiometer2 = 2
b_Frequenz = 20
b_Spannung = 20
b_Induktivität1= 226e-6

b_Pmetery = 1000-b_Potentiometer1

b_Pmetery_Ohm = (b_Pmetery/1000)*200
b_Pmeterx_Ohm = (b_Potentiometer1/1000)*200
delt_b_Pmeter_Ohm = (b_deltaPotentiometer1/1000)*200

b_Induktivität2 = (b_Pmetery_Ohm/b_Pmeterx_Ohm)*b_Induktivität1
delt_b_Induktivität2 = np.sqrt(((delt_b_Pmeter_Ohm/b_Pmeterx_Ohm)*b_Induktivität1)**2+((b_Pmetery_Ohm/b_Pmeterx_Ohm**2)*b_Induktivität1*delt_b_Pmeter_Ohm)**2)

#print(b_Pmeterx_Ohm,b_Pmetery_Ohm,delt_b_Pmeter_Ohm)
#print(b_Induktivität2,delt_b_Induktivität2)

# c
c_Widerstand = 1.100
c_deltaWiderstand = 0.001
c_Strom = 0.060
c_deltaStrom = 0.001
c_Frequenz = 400
c_U0 = 10
c_Us = 0.108
c_deltaUs = 0.001

c_Induktivität = np.sqrt((c_Us/c_Strom)**2-c_Widerstand**2)*(1/(2*np.pi*c_Frequenz))
delt_c_Induktivität = np.sqrt((0.5*((c_Us/c_Strom)**2-c_Widerstand**2)**(-1/2)*(-2*c_Widerstand)*c_deltaWiderstand*(1/(2*np.pi*c_Frequenz)))**2+(0.5*((c_Us/c_Strom)**2-c_Widerstand**2)**(-1/2)*(-2*c_Strom**(-3))*c_deltaStrom*(1/(2*np.pi*c_Frequenz)))**2+(0.5*((c_Us/c_Strom)**2-c_Widerstand**2)**(-1/2)*(2*c_Us)*c_deltaUs*(1/(2*np.pi*c_Frequenz)))**2)
delt_c_Induktivität = 0.000017

c_abweichung = c_Induktivität/b_Induktivität2-1

vphi = np.arctan((2*np.pi*c_Frequenz*c_Induktivität)/c_Widerstand)*360/(2*np.pi)
delt_vphi = np.sqrt((1/(((2*np.pi*c_Frequenz*c_Induktivität)/c_Widerstand)**2+1)*2*np.pi*c_Frequenz/c_Widerstand*delt_c_Induktivität)**2+(1/(((2*np.pi*c_Frequenz*c_Induktivität)/c_Widerstand)**2+1)*2*np.pi*c_Frequenz/c_Widerstand**2*c_deltaWiderstand)**2)

#print(c_Induktivität,delt_c_Induktivität,c_abweichung)
#print(vphi,delt_vphi)

# d
d_Widerstand = np.linspace(0, 200, 10)
#Skt = np.linspace(0, 1000, 10)
#Skt  = [0, 100, 200, 300, 400, 500,  600, 700, 800, 900, 920, 940, 960, 980, 1000]
d_Skt = np.array([0, 20, 40, 60, 80, 100, 200, 300, 400, 500, 600, 700, 800,  900, 1000])
d_Spannung_Widerstand = np.array([42, 113, 142, 156, 165, 169, 179, 182, 183, 184, 184, 184, 185, 185, 185])*1e-3
#Spannung_Widerstand = [0.186, 0.186, 0.185, 0.185, 0.185, 0.184, 0.183, 0.182, 0.179, 0.175, 0.167, 0.160, 0.149, 0.126, 0.070, 0.020]
d_Spannung_Kondensator = np.array([173, 126, 95, 74, 59, 49, 25, 17, 12, 9,  7, 5, 4, 3, 2])*1e-3
d_Spannung_Widerstand_inf = 187
d_Spannung_Kondensator_inf = 0

for i in range(0,15):
    d_x = np.array([0,d_Spannung_Widerstand[i]*np.cos(np.arctan(d_Spannung_Kondensator[i]/d_Spannung_Widerstand[i])),187*1e-3])
    d_y = np.array([0,d_Spannung_Widerstand[i]*np.sin(np.arctan(d_Spannung_Kondensator[i]/d_Spannung_Widerstand[i])),0])
    d_delt_Spannung = np.array([0,1e-3,0])
#    plt.errorbar(d_x,d_y,d_delt_Spannung)

angle = np.linspace(0,2*np.pi,150)
radius = 0.187/2
x = 0.187/2+radius*np.cos(angle)
y = radius*np.sin(angle)
#plt.plot(x,y)

#plt.axis([0,0.187,0,0.187/np.sqrt(2)])
#plt.savefig('234_d.png')
#plt.show()

# e
e_Ue = 10

e_Frequenz = np.array([200, 300, 400, 600, 800, 1200, 1700, 2400, 3500, 5000])
e_Ua_Tiefpass = np.array([3.363, 3.223, 3.054, 2.686, 2.340, 1.793, 1.347, 0.972, 0.652, 0.426])
e_Ua_Hochpass = np.array([0.161, 0.886, 1.119, 1.474, 1.710, 1.964, 2.087, 2.125, 2.080, 1.942])
e_Ua_Sperrfilter = np.array([3.325, 3.072, 2.629, 1.000, 0.942, 2.574, 3.031, 3.166, 3.117, 2.911])

delt_e_Ua = np.zeros(len(e_Ua_Tiefpass))+1e-3

e_R = 100
e_C = 1.5*1e-6
e_RL = 10

# x achse: Omega = nu/nu_g
# y achse: A = U_A/U_E

nu_g_Hoch_Tief = 1/(e_R*e_C*2*np.pi)
nu_g_Sperrfilter = 700

Omega_Hoch_Tief = e_Frequenz/nu_g_Hoch_Tief
Omega_Sperrfilter = e_Frequenz/nu_g_Sperrfilter

A_Tiefpass = e_Ua_Tiefpass/e_Ue
delt_A_Tiefpass = delt_e_Ua/e_Ue

A_Hochpass = e_Ua_Hochpass/e_Ue
delt_A_Hochpass = delt_e_Ua/e_Ue

A_Sperrfilter = e_Ua_Sperrfilter/e_Ue
delt_A_Sperrfilter = delt_e_Ua/e_Ue

#plt.errorbar(Omega_Hoch_Tief,A_Tiefpass,delt_A_Tiefpass,ls="",marker="d")
#plt.errorbar(Omega_Hoch_Tief,A_Hochpass,delt_A_Hochpass,ls="",marker="d")
#plt.errorbar(Omega_Sperrfilter,A_Sperrfilter,delt_A_Sperrfilter,ls="",marker="d")
#plt.savefig('234_e.png')
#plt.show()

# i
i_Widerstand = 5.9
i_C=1.5e-6 
i_Frequenz = np.array([200, 400, 600, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 800, 1000, 1200, 1400, 1600, 1800, 2000])
i_U = np.array([0.206, 0.283, 0.718, 1.311, 1.553, 1.871, 2.255, 2.585, 2.616, 2.304, 1.895, 1.547, 1.281, 1.081, 0.580, 0.177, 0.093, 0.059, 0.040, 0.028, 0.020])
delt_i_U = np.zeros(len(i_U))+1e-3

plt.errorbar(i_Frequenz,i_U,delt_i_U,ls="",marker="d")
#plt.savefig('234_i.png')
plt.show()

# Rechnung
#   Messwerte: aufgabeGröße = Rechnung #Einheit
#   Fehler: d_aufgabeGröße = Rechnung #Einheit



# Achsen
#   x =
#   y =
#   yerr =

zusammen = ['end'] #<--- Welche Plots zusammengehören. Gleiche Buchstaben werden in einem Plot ausgegeben (Beispiel: ['a','a','b'], die ersten beiden x, y und yerr Werte werden in einem Plot ausgegeben, die dritten x, y, yerr Werte werden in einem Plot ausgegeben).
x = [] #<--- x Werte
y = [] #<--- y Werte
yerr = [] #<--- y Fehler (ein Fehler pro x Wert)
color = 'blue' #<--- Farbe der Punkte/Gerade

Auswertung = gf.Auswertung(x,y,yerr,zusammen,color)
Auswertung.auswertung()
