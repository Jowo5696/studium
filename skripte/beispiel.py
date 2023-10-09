import numpy as np
import matplotlib.pyplot as plt
import geradenfit as gf

# Konstanten

g = 9.81 #m/s**2

# Messewrte
#   Messwerte: aufgabeMessung = np.array([]) #Einheit
#   Fehler: d_aufgabeMessung = np.zeros(len(Messwerte))+Fehler / np.array([]) #Einheit

aGewicht = np.array([10.0,20.0,30.0,40.0,50.0]) #kg
d_aGewicht = np.zeros(len(aGewicht))+1.5 #kg

bGewicht = np.array([10,20,30,40,50,60,70,80,90,100]) #kg
bGeschw = np.array([12,14,15,18,29,33,34,35,36,37]) #m/s
d_bGeschw = np.zeros(len(bGeschw))+4 #m/s

# Rechnung
#   Messwerte: aufgabeGröße = Rechnung #Einheit
#   Fehler: d_aufgabeGröße = Rechnung #Einheit

aKraft = aGewicht*g
d_aKraft = d_aGewicht*g

# Achsen
#   x =
#   y =
#   yerr =

zusammen = ['a','a','b','end'] #<--- Welchee Plots zusammengehören. Gleiche Buchstaben werden in einem Plot ausgegeben (Beispiel: ['a','a','b'], die ersten beiden x, y und yerr Werte werden in einem Plot ausgegeben, die dritten x, y, yerr Werte werden in einem Plot ausgegeben).
x = [aGewicht,bGewicht,aGewicht] #<--- x Werte
y = [aKraft,bGeschw,aKraft] #<--- y Werte
yerr = [d_aKraft,d_bGeschw,d_aKraft] #<--- y Fehler (ein Fehler pro x Wert)
color = 'blue' #<--- Farbe der Punkte/Geraden

Auswertung = gf.Auswertung(x,y,yerr,zusammen,color)
Auswertung.auswertung()
