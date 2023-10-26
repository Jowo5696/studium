import numpy as np
import matplotlib.pyplot as plt
import geradenfit as gf
from tabulate import tabulate

# Konstanten



# Messewrte
#   Messwerte: aufgabeMessung = np.array([]) #Einheit
#   Fehler: d_aufgabeMessung = np.zeros(len(Messwerte))+Fehler / np.array([]) #Einheit

# 232.a
a_U0 = np.array([1.871,2.215,2.634,3.128,3.582,3.934,4.453]) # V
a_U = np.array([18.1,21.5,25.5,30.2,35.0,38.2,43.5])*(5/50) # V
a_delt_U = np.zeros(len(a_U))+0.2*(5/50) # V
a_I = np.array([4,5,6,7,8,9,10])*(500/50) # mA
a_delt_I = np.zeros(len(a_I))+0.2*(500/50) # mA

a_data = np.transpose([a_U0,a_U,a_delt_U,a_I,a_delt_I])
a_head = ['Ausgangsspannung U0 [V]','U [V]','∆U [V]','I [mA]','∆I [mA]']

#print('Tabelle 232.a: U-I-Abhängigkeit')
#print(tabulate(a_data,headers=a_head,tablefmt='fancy_grid'))

# 232.b

# 232.c
c_I = a_I # mA
c_Rx = np.zeros(len(a_I))+59.3
c_U = c_Rx*c_I*1e-3

c_delt_U = np.zeros(len(c_U))
c_delt_I = np.zeros(len(c_U))

#plt.plot(c_I,c_U,color='green',label='232.b')

# 232.d
d_R = np.linspace(13,130,10)
d_U = np.array([12.1,21.9,24.0,25.9,26.9,27.5,28.0,29.0,29.0,29.5])*(5/50) # V
d_delt_U = np.zeros(len(d_U))+0.2*(5/50) # V
d_I = np.array([29.8,13.6,10.9,8.2,7.1,6.1,5.8,4.7,4.1,3.5])*(500/50) # mA
d_delt_I = np.zeros(len(d_I))+0.2*(500/50) # mA
d_R1 = 20 # Ohm
d_Rx = d_R1
d_R2 = 50 # Ohm
d_Ry = d_R2
d_U0 = 4 # V
d_Ri = 50 # Ohm

d_data = np.transpose([d_R,d_U,d_delt_U,d_I,d_delt_I])
d_head = ['R [Ω]','U [V]','∆U [V]','I [mA]','∆I [mA]']
#print('Tabelle 232.d: Messung verschiedener Lastwiderstände')
#print(tabulate(d_data,headers=d_head,tablefmt='fancy_grid'))

# 232.f
f_Ry = np.array([200, 400, 600, 800, 1000])
f_Uinf = np.array([9.0, 12.9, 21.5, 35.5, 44.5])*5/50
f_U20 = np.array([6.0, 11.0, 16.0, 27.5, 41.0])*5/50
f_U50 = np.array([7.0, 12.5, 18.8, 22.2, 42.5])*5/50

f_delt_U = (np.zeros(len(f_Ry))+0.2)*5/50
f_delt_R = np.zeros(len(f_Ry))+2

f_Ry2 = f_Ry*1000**(-1)*100
f_Rges = np.zeros(len(f_Ry2))+100

f_l = np.zeros(len(f_Ry2))+1000 
f_xl = f_Ry/f_l

f_data = np.transpose([f_Ry,f_delt_R,f_Uinf,f_U20,f_U50,f_delt_U])
f_head = ['R_y [Ω]','∆R_y [Ω]','U bei R=∞Ω [V]','U bei R=20Ω [V]','U bei R=50Ω [V]','∆U [V]']
#print('Tabelle 232.f: R-I-Abhängigkeit')
#print(tabulate(f_data,headers=f_head,tablefmt='fancy_grid'))

#plt.plot(f_xl,f_Ry2)

# 232.g
g_I20 = np.array([3.1,5.4,8.5,14.3,31.5])*(500/50) # mA
g_I50 = np.array([2.2,4.0,6.1,9.1,14.9])*(500/50) # Skt
g_delt_I = (np.zeros(len(g_I20))+0.2)*(500/50) # Skt

g_Pinf = np.zeros(len(f_Uinf))
g_P20 = np.round(f_U20*g_I20,1)
g_delt_P20 = np.round(np.sqrt((f_delt_U*g_I20)**2+(f_U20*g_delt_I)**2),1)
g_P50 = np.round(f_U50*g_I50,1)
g_delt_P50 = np.round(np.sqrt((f_delt_U*g_I50)**2+(f_U50*g_delt_I)**2),1)

g_data = np.transpose([g_I20,g_I50,g_delt_I,g_Pinf,g_P20,g_delt_P20,g_P50,g_delt_P50])
g_head = ['I 20Ω [mA]','I 50Ω [mA]','∆I [mA]','P(∞Ω)','P(20Ω)','∆P(20Ω)','P(50Ω)','∆P(50Ω)']
print('Tabelle 232.g: Leistung')
print(tabulate(g_data,headers=g_head,tablefmt='fancy_grid'))

# 232.m
m_Widerstand_1 = np.array([1.1,0.9,0.7,0.65,0.57,0.49,0.43,0.38,0.35,0.30,0.27,0.24,0.21,0.18,0.16,0.14,0.13,0.12,0.095,0.085])
m_delt_Widerstand_1 = np.zeros(len(m_Widerstand_1))+0.02
m_T_1 = np.array([19.8, 24.1, 28.2, 32.6, 37.0, 40.7, 44.1, 47.2, 50.4, 53.6, 57.1, 61.4, 64.8, 68.2, 73.6, 78.4, 81.6, 85.4, 90.5, 95.2])
m_delt_T_1 = np.zeros(len(m_T_1))+0.2

m_Widerstand_2 = np.array([4.2,4.1,4.1,4.0,4.1,4.2,4.0,4.2,4.1,4.1,4.1,4.2,4.1,4.6,4.4,4.2,4.2,4.1,4.2,4.2])
m_T_2 = np.array([20.5, 25.1, 28.7, 33.5, 37.5, 41.6, 45.0, 48.2, 50.9, 54.7, 57.8, 61.9, 65.4, 70.3, 74.3, 79.1, 82.3, 87.8, 91.2, 96.1])
m_delt_Widerstand_2 = np.zeros(len(m_Widerstand_2))+0.1
m_delt_T_2 = np.zeros(len(m_T_2))+0.2

m_Widerstand_3 = np.array([112,127,138,170,203,209,330,460,640,1350,4600,15000,55000,'8.8 M',230000,280000,300000,320000,350000,360000])
m_T_3 = np.array([21.2, 25.8, 29.34, 24.1, 38.6, 42.4, 45.4, 48.8, 51.9, 55.0, 58.8, 62.5, 66.1, 70.9, 75.9, 79.7, 82.9, 88.8, 92.4, 97.3])
m_delt_Widerstand_3 = np.array([10,10,10,10,10,30,30,30,30,200,200,200,2e+4,2e+4,2e+4,2e+4,2e+4,2e+4,2e+4,2e+4])
m_delt_T_3 = np.zeros(len(m_T_3))+0.2

m_Widerstand_4 = np.array([1.1,1.1,1.12,1.14,1.15,1.17,1.18,1.20,1.20,1.21,1.22,1.23,1.25,1.27,1.28,1.30,1.31,1.33,1.35,1.35])
m_T_4 = np.array([22.3, 26.5, 30.7, 34.9, 39.4, 43.1, 46.3, 49.4, 52.6, 56.1, 59.9, 63.6, 67.1, 72.0, 76.9, 80.4, 83.6, 89.5, 93.4, 98.4])
m_delt_Widerstand_4 = np.zeros(len(m_Widerstand_4))+0.02
m_delt_T_4 = np.zeros(len(m_T_4))+0.2

m_Widerstand_5 = np.array([100,100.2,100,100,100,100,100.1,100,100.2,100,100,100.1,100,100,100.3,100.2,100.1,100.3,100.2,100.2])
m_T_5 = np.array([23.5, 26.9, 31.5, 35.7, 39.9, 44.1, 47.2, 50.2, 53.4, 57.0, 60.5, 63.9, 67.7, 73.0, 77.8, 81.3, 84.9, 90.0, 94.2, 98.6])
m_delt_Widerstand_5 = np.zeros(len(m_Widerstand_5))+0.1
m_delt_T_5 = np.zeros(len(m_T_5))+0.2

m_data = np.transpose([m_Widerstand_1,m_delt_Widerstand_1,m_T_1,m_delt_T_1,m_Widerstand_2,m_delt_Widerstand_2,m_T_2,m_delt_T_2,m_Widerstand_3,m_delt_Widerstand_3,m_T_3,m_delt_T_3])
m_data2 = np.transpose([m_Widerstand_4,m_delt_Widerstand_4,m_T_4,m_delt_T_4,m_Widerstand_5,m_delt_Widerstand_5,m_T_5,m_delt_T_5])
m_head = ['R1 [Ω]','∆R1 [Ω]','T1 [C]','∆T1 [C]','R2 [Ω]','∆R2 [Ω]','T2 [C]','∆T2 [C]','R3 [Ω]','∆R3 [Ω]','T3 [C]','∆T3 [C]']
m_head2 = ['R4 [Ω]','∆R4 [Ω]','T4 [C]','∆T4 [C]','R5 [Ω]','∆R5 [Ω]','T5 [C]','∆T5 [C]']

#print('Tabelle 1 232.m: Widerstand in Abhängigkeit der Temperatur')
#print(tabulate(m_data,headers=m_head,tablefmt='fancy_grid'))
#print('Tabelle 2 232.m: Widerstand in Abhängigkeit der Temperatur')
#print(tabulate(m_data2,headers=m_head2,tablefmt='fancy_grid'))

# Rechnung
#   Messwerte: aufgabeGröße = Rechnung #Einheit
#   Fehler: d_aufgabeGröße = Rechnung #Einheit



# Achsen
#   x =
#   y =
#   yerr =

zusammen = ['a','a','a','end'] #<--- Welche Plots zusammengehören. Gleiche Buchstaben werden in einem Plot ausgegeben (Beispiel: ['a','a','b'], die ersten beiden x, y und yerr Werte werden in einem Plot ausgegeben, die dritten x, y, yerr Werte werden in einem Plot ausgegeben).
#x = [f_Uinf,f_U20,f_U50] #<--- x Werte
x = [f_xl,f_xl,f_xl] #<--- x Werte
xlabel = ['x/l [Skt]','x/l [Skt]','x/l [Skt]']
xerr = [np.zeros(len(f_xl)),np.zeros(len(f_xl)),np.zeros(len(f_xl))]
y = [f_Uinf,f_U20,f_U50] #<--- x Werte
#y = [f_Ry,f_Ry,f_Ry] #<--- y Werte
ylabel = ['U [V]','U [V]','U [V]'] 
yerr = [f_delt_U,f_delt_U,f_delt_U] #<--- y Fehler (ein Fehler pro x Wert)
title = ['232.f lineare Relation zwischen U und x/l']
label = ['232.f R=inf','232.f R=20','232.f R=50']
color = ['blue','red','green'] #<--- Farbe der Punkte/Geraden

#zusammen = ['a','end'] #<--- Welche Plots zusammengehören. Gleiche Buchstaben werden in einem Plot ausgegeben (Beispiel: ['a','a','b'], die ersten beiden x, y und yerr Werte werden in einem Plot ausgegeben, die dritten x, y, yerr Werte werden in einem Plot ausgegeben).
#x = [a_I] #<--- x Werte
#xlabel = ['I [mA]']
#xerr = [a_delt_I] #<--- x Fehler (ein Fehler pro x Wert)
#y = [a_U] #<--- y Werte
#ylabel = ['U [V]'] 
#yerr = [a_delt_U] #<--- y Fehler (ein Fehler pro x Wert)
#title = ['232.a U-I-Abhängigkeit']
#label = ['232.a']
#color = ['blue'] #<--- Farbe der Punkte/Geraden

Auswertung = gf.Auswertung(x,xlabel,y,ylabel,yerr,xerr,title,label,color,zusammen)
#Auswertung.auswertung()
