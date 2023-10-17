import numpy as np
import matplotlib.pyplot as plt
import geradenfit as gf
import uncertainties

# Konstanten



# Messewrte
#   Messwerte: aufgabeMessung = np.array([]) #Einheit
#   Fehler: d_aufgabeMessung = np.zeros(len(Messwerte))+Fehler / np.array([]) #Einheit

# a NOCHMAL MACHEN
Hertz=2e3
Spannung = 10
Widerstand = 934 
deltaWiderstand = 2
C1 = 20e-6
R1 = 1000-Widerstand
R2 = Widerstand
PotentiometerSpannung = 200

# b NOCHMAL MACHEN
Potentiometer1_max = 200
Potentiometer2_max = 200
Potentiometer1 = 490 # skalar für R2
deltaPotentiometer1 = 2
Potentiometer2 = 500 # skalar für R2?
deltaPotentiometerr2 = 2
Frequenz = 20
Spannung = 20
Inudktivität1 = 226e-6

# c
Widerstand = 1101
deltaWiderstnad = 1
Strom = 0.06
deltaStrom = 0.001
Frequnz = 20
U0 = 10
Us = 0.108
deltaUs = 0.001

# d
Widerstand = np.linspace(0, 200, 10)
#Skt = np.linspace(0, 1000, 10)
#Skt  = [0, 100, 200, 300, 400, 500,  600, 700, 800, 900, 920, 940, 960, 980, 1000]
Skt = np.array([0, 20, 40, 60, 60,  80, 100, 200, 300, 400, 500, 600, 700, 800,  900, 1000])
Spannung_Widerstand = np.array([42, 113, 142, 156, 165, 169, 179, 182, 183, 184, 184, 184, 185, 185, 185])*1e-3
#Spannung_Widerstand = [0.186, 0.186, 0.185, 0.185, 0.185, 0.184, 0.183, 0.182, 0.179, 0.175, 0.167, 0.160, 0.149, 0.126, 0.070, 0.020]
Spannung_Kondensator = np.array([173, 126, 74, 59, 49, 25, 17, 12, 9,  7, 5, 4, 3, 2])*1e-3
Spannung_Widerstand_inf = 187
Spannung_Kondensator_inf = 0

# e
Ue = 10

Frequenz = np.array([200, 300, 400, 600, 800, 1200, 1700, 2400, 3500, 5000])
Ua_Tiefpass = np.array([3.363, 3.223, 3.054, 2.686, 2.340, 1.793, 1.347, 0.972, 0.652, 0.426])
Ua_Hochpass = np.array([0.161, 0.886, 1.119, 1.474, 1.710, 1.964, 2.087, 2.125, 2080, 1.942])
Ua_Sperrfilterr = np.array([3.325, 3.072, 2.629, 1.000, 0.942, 2.574, 3.031, 3.166, 3.117, 2.911])

# i
Widerstand = 5.9
C=1.5e-6 
Frequenz =  np.array([200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750])
U = np.array([0.206, 0.283, 0.718, 0.580, 0.177, 0.93, 0.59, 0.40, 0.028, 0.020, 1.311, 1.553, 1.871, 2.255, 2.585, 2.616, 2.304, 1.895, 1.547, 1.281, 1.081])

# Rechnung
#   Messwerte: aufgabeGröße = Rechnung #Einheit
#   Fehler: d_aufgabeGröße = Rechnung #Einheit

print((x).derivatives[x])

# Achsen
#   x =
#   y =
#   yerr =

zusammen = ['end'] #<--- Welche Plots zusammengehören. Gleiche Buchstaben werden in einem Plot ausgegeben (Beispiel: ['a','a','b'], die ersten beiden x, y und yerr Werte werden in einem Plot ausgegeben, die dritten x, y, yerr Werte werden in einem Plot ausgegeben).
x = [] #<--- x Werte
y = [] #<--- y Werte
yerr = [] #<--- y Fehler (ein Fehler pro x Wert)
color = 'blue' #<--- Farbe der Punkte/Geraden

Auswertung = gf.Auswertung(x,y,yerr,zusammen,color)
Auswertung.auswertung()
