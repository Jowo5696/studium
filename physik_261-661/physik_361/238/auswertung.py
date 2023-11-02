import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
import geradenfit as gf

#{{{ 238.a

a_data = pd.read_csv('238_a_messungen.csv')

a_I1 = np.fromiter(a_data['I_A1'],dtype=float)
a_delt_I1 = np.zeros(len(a_I1))+0.01

a_U1 = np.fromiter(a_data['U_B1'],dtype=float)
a_delt_U1 = np.zeros(len(a_U1))+0.1

a_UR = np.fromiter(a_data['U_B2'],dtype=float)
a_delt_UR = np.zeros(len(a_UR))+0.1

a_R = a_UR/a_I1
a_delt_R = np.sqrt((a_delt_UR/a_I1)**2+(a_UR/a_I1**2*a_delt_I1)**2)

a_cos = a_UR/a_U1
a_delt_cos = np.sqrt((a_delt_UR/a_U1)**2+(a_UR/a_U1**2*a_delt_U1)**2)

a_Ps = a_U1*a_I1
a_delt_Ps = np.sqrt((a_delt_U1*a_I1)**2+(a_U1*a_delt_I1)**2)

a_Pscos = a_U1*a_I1*a_cos
a_delt_Pscos = np.sqrt((a_delt_U1*a_I1*a_cos)**2+(a_U1*a_delt_I1*a_cos)**2+(a_U1*a_I1*a_delt_cos)**2)

a_Pw = np.fromiter(a_data['P_1'],dtype=float)
a_delt_Pw = np.zeros(len(a_Pw))+0.01

a_data1 = np.transpose([np.round(a_U1,2),np.round(a_UR,2),np.round(a_delt_UR,2),np.round(a_I1,2),np.round(a_delt_I1,2),np.round(a_R,2),np.round(a_delt_R,2)])
a_head1 = ['U_B1 [V]','U_R [V]','ΔU [V]','I [A]','ΔI [A]','R [Ω]','ΔR [Ω]']
a_data2 = np.round(np.transpose([a_Pw,a_delt_Pw,a_Ps,a_delt_Ps,a_Pscos,a_delt_Pscos]),2)
a_head2 = ['Pw [W]','ΔPw [W]','Ps [W]','ΔPs [W]','Ps*cos [W]','ΔP*cos [W]']
#print('Tabelle 238.b: Leistung')
#print(tabulate(a_data2,headers=a_head2,tablefmt='fancy_grid'))

zusammen = ['a','a','a','end'] # Welche Plots zusammengehören. Gleiche Buchstaben werden in einem Plot ausgegeben (Beispiel: ['a','a','b'], die ersten beiden x, y Werte werden in einem Plot ausgegeben, die dritten x, y, Werte werden in einem Plot ausgegeben).
x = [a_R,a_R,a_R,a_R]
xerr = [a_delt_R,a_delt_R,a_delt_R,np.zeros(len(a_R))+0.01]
xlabel = ['Widerstand [Ω]','Widerstand [Ω]','Widerstand [Ω]','Widerstand [Ω]']
y = [a_Pw,a_Ps,a_Pscos,np.zeros(len(a_R))+27]
yerr = [a_delt_Pw,a_delt_Ps,a_delt_Pscos,np.zeros(len(a_R))+0.01]
ylabel = ['Leistung [W]','Leistung [W]','Leistung [W]','Leistung [W]']
title = '238.b: RC-Kreis'
label = ['Wirkleistung','Scheinleistung','Scheinleistung cos','Maximale Wirkleistung'] # label von plt.errorbar und plt.plot
color = ['red','green','blue','pink'] # farbe der punkte (geraden sind immer blau)

#Auswertung = gf.Auswertung(x,xerr,xlabel,y,yerr,ylabel,title,label,color,zusammen)
#Auswertung.auswertung()

#}}}

# {{{ 238.c.d

c_data = pd.read_csv('238_c_messungen.csv')

c_U1 = np.fromiter(c_data['U_B1'],dtype=float)
c_U2 = np.fromiter(c_data['U_B2'],dtype=float)
c_delt_U = np.zeros(len(c_U1))+0.1

c_I1 = np.fromiter(c_data['I_A1'],dtype=float)
c_I2 = np.fromiter(c_data['I_A2'],dtype=float)
c_delt_I = np.zeros(len(c_I1))+0.01

c_Pw1 = np.fromiter(c_data['P_1'],dtype=float)
c_Pw2 = np.fromiter(c_data['P_2'],dtype=float)
c_delt_Pw = np.zeros(len(c_Pw1))+0.01

c_datatable = np.round(np.transpose([c_U1,c_U2,c_delt_U,c_I1,c_I2,c_delt_I,c_Pw1,c_Pw1,c_delt_Pw]),2)
c_headers = ['U1 [V]','U2 [V]','ΔU [V]','I1 [A]','I2 [A]','ΔI [A]','Pw1 [W]','Pw2 [W]','ΔPw [W]']
#print('Tabelle 238.c: Wirkleistung')
#print(tabulate(c_datatable,headers=c_headers,tablefmt='fancy_grid'))

d_PS2 = c_U2*c_I2
d_delt_PS2 = np.sqrt((c_delt_U*c_I2)**2+(c_U2*c_delt_I)**2)

d_PCu = c_U1*c_I1+c_U2*c_I2
d_delt_PCu = np.sqrt((c_delt_U*c_I1)**2+(c_U1*c_delt_I)**2+(c_delt_U*c_I2)**2+(c_U2*c_delt_I)**2)

d_eta = c_Pw2/c_Pw1
d_delt_eta = np.sqrt((c_delt_Pw/c_Pw1)**2+(c_Pw2/c_Pw1**2*c_delt_Pw)**2)

d_PV = c_Pw1-c_Pw2
d_delt_PV = np.sqrt((c_delt_Pw)**2+(c_delt_Pw)**2)

d_PFe = d_PV-d_PCu
d_delt_PFe = np.sqrt((d_delt_PV)**2+(d_delt_PCu)**2)

d_PS1 = c_U1*c_I1
d_delt_PS1 = np.sqrt((c_delt_U*c_I1)**2+(c_U1/c_I1**2*c_delt_I)**2)

d_data = np.round(np.transpose([d_PS2,d_delt_PS2,d_PCu,d_delt_PCu,np.zeros(len(d_eta)),np.zeros(len(d_delt_eta)),d_PV,d_delt_PV,d_PFe,d_delt_PFe,d_PS1,d_delt_PS1]),2)
d_data[:,4] = np.round(d_eta,4)
d_data[:,5] = np.round(d_delt_eta,4)
d_headers = ['PS2 [W]','ΔPS2 [W]','PCu [W]','ΔPCu [W]','η','Δη','PV [W]','ΔPV [W]','PFe [W]','ΔPFe [W]','PS1 [W]','ΔPS1 [W]']
#print('Tabelle 238.c: Leistungen und Wirkungsquerschnitt')
#print(tabulate(d_data,headers=d_headers,tablefmt='fancy_grid'))

zusammen = ['a','a','a','a','a','b','end'] # Welche Plots zusammengehören. Gleiche Buchstaben werden in einem Plot ausgegeben (Beispiel: ['a','a','b'], die ersten beiden x, y Werte werden in einem Plot ausgegeben, die dritten x, y, Werte werden in einem Plot ausgegeben).
x = [c_I2,c_I2,c_I2,c_I2,c_I2,c_I2]
xerr = [c_delt_I,c_delt_I,c_delt_I,c_delt_I,c_delt_I,c_delt_I]
xlabel = ['Stromstärke I2 [A]','Stromstärke I2 [A]','Stromstärke I2 [A]','Stromstärke I2 [A]','Stromstärke I2 [A]','Stromstärke I2 [A]']
y = [c_Pw1,c_Pw2,d_PV,d_PCu,d_PFe,d_eta]
yerr = [c_delt_Pw,c_delt_Pw,d_delt_PV,d_delt_PCu,d_delt_PFe,d_delt_eta]
ylabel = ['Leistung [W]','Leistung [W]','Leistung [W]','Leistung [W]','Leistung [W]','Wirkungsgrad [Verhältnis]']
title = '238.d: Leistungen'
label = ['Pw1','Pw2','PV','PCu','PFe','η'] # label von plt.errorbar und plt.plot
color = ['red','blue','green','violet','pink','red'] # farbe der punkte (geraden sind immer blau)

Auswertung = gf.Auswertung(x,xerr,xlabel,y,yerr,ylabel,title,label,color,zusammen)
#Auswertung.auswertung()

#}}}

# 238.e

e_omegaL = c_U1[0]/c_I1[0]
e_delt_omegaL = np.sqrt((c_delt_U[0]/c_I1[0])**2+(c_U1[0]/c_I1[0]**2*c_delt_I[0])**2)
#print(c_U1[0],c_delt_U[0],c_I1[0],c_delt_I[0])
#print(np.round(e_omegaL,2),np.round(e_delt_omegaL,2))

# 238.f

f_sigma1 = 1-c_I2[-1]**2/c_I1[-1]**2
f_delt_sigma1 = np.sqrt((2*c_I2[-1]/c_I1[-1]**2*c_delt_I[-1])**2+(2*c_I2[-1]**2/c_I1[-1]**3*c_delt_I[-1])**2)

f_sigma2 = 1-c_U2[0]**2/c_U1[0]**2
f_delt_sigma2 = np.sqrt((2*c_U2[0]/c_U1[0]**2*c_delt_U[0])**2+(2*c_U2[0]**2/c_U1[0]**3*c_delt_U[0])**2)

f_sigma3 = (c_U1[-1]/c_I1[-1])/(c_U1[0]/c_I1[0])
# (c_U1[-1]*c_I1[0])/(c_I1[-1]*c_U1[0])
f_delt_sigma3 = np.sqrt(((c_delt_U[-1]*c_I1[0])/(c_I1[-1]*c_U1[0]))**2+((c_U1[-1]*c_delt_I[0])/(c_I1[-1]*c_U1[0]))**2+((c_U1[-1]*c_I1[0])/(c_I1[-1]**2*c_U1[0])*c_delt_I[-1])**2+((c_U1[-1]*c_I1[0])/(c_I1[-1]*c_delt_U[0]**2)*c_delt_U[0])**2)

f_sigma4 = c_U1[-1]/(e_omegaL*c_I2[-1])
f_delt_sigma4 = np.sqrt((c_delt_U[0]/(e_omegaL*c_I2[0]))**2+(c_U1[0]/(e_omegaL**2*c_I2[0])*e_delt_omegaL)**2+(c_U1[0]/(e_omegaL*c_I2[0]**2)*c_delt_I[0])**2)

#print(c_I1[-1],c_I2[-1],c_delt_I[-1])
#print('1: ',f_sigma1,f_delt_sigma1)
#print(c_U1[0],c_U2[0],c_delt_U[0])
#print('2: ',f_sigma2,f_delt_sigma2)
#print(c_U1[-1],c_U1[0],c_I1[-1],c_I1[0])
#print('3: ',f_sigma3,f_delt_sigma3)
#print(c_U1[0],e_omegaL,c_I2[0])
#print('4: ',f_sigma4,f_delt_sigma4)

f_sigma_mittel = 1/4*(f_sigma1+f_sigma2+f_sigma3+f_sigma4)
f_delt_sigma_mittel = np.sqrt((1/4*f_delt_sigma1)**2+(1/4*f_delt_sigma2)**2+(1/4*0.002)**2+(1/4*0.002)**2)
#print(f_sigma_mittel,f_delt_sigma_mittel)

# 238.g

zusammen = ['end'] # Welche Plots zusammengehören. Gleiche Buchstaben werden in einem Plot ausgegeben (Beispiel: ['a','a','b'], die ersten beiden x, y Werte werden in einem Plot ausgegeben, die dritten x, y, Werte werden in einem Plot ausgegeben).
x = [c_I2]
xerr = [c_delt_I]
xlabel = ['Stromstärke [A]']
y = [c_U2/c_U1]
yerr = [np.sqrt((c_delt_U/c_U1)**2+(c_U2/c_U1**2*c_delt_U)**2)]
ylabel = ['Verhältnis der Spannungen']
title = '238.g: Spannungsübertragung'
label = ['Spannungsverhältnis'] # label von plt.errorbar und plt.plot
color = 'red' # farbe der punkte (geraden sind immer blau)

#Auswertung = gf.Auswertung(x,xerr,xlabel,y,yerr,ylabel,title,label,color,zusammen)
#Auswertung.auswertung()

# 238.g

g_R2 = (c_U2/c_I2)
g_R22RV = g_R2+2*0.6
yy = g_R2/g_R22RV*f_sigma_mittel*(1+(f_sigma_mittel*e_omegaL/g_R22RV)**2)**(-0.5)

a = 1-(f_sigma_mittel/2)
yy = a*g_R2/g_R22RV*(1+(f_sigma_mittel*e_omegaL/g_R22RV)**2)**(-1/2)

zusammen = ['end'] # Welche Plots zusammengehören. Gleiche Buchstaben werden in einem Plot ausgegeben (Beispiel: ['a','a','b'], die ersten beiden x, y Werte werden in einem Plot ausgegeben, die dritten x, y, Werte werden in einem Plot ausgegeben).
x = [c_I2]
xerr = [c_delt_I]
xlabel = ['Stromstärke [A]']
y = [yy]
yerr = [np.sqrt((c_delt_U/c_U1)**2+(c_U2/c_U1**2*c_delt_U)**2)]
ylabel = ['Verhältnis der Spannungen']
title = '238.g: Spannungsübertragung'
label = ['Spannungsverhältnis'] # label von plt.errorbar und plt.plot
color = 'red' # farbe der punkte (geraden sind immer blau)

#Auswertung = gf.Auswertung(x,xerr,xlabel,y,yerr,ylabel,title,label,color,zusammen)
#Auswertung.auswertung()

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
color = '' # farbe der punkte (geraden sind immer blau)

#Auswertung = gf.Auswertung(x,xerr,xlabel,y,yerr,ylabel,title,label,color,zusammen)
#Auswertung.auswertung()
