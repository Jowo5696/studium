import numpy as np
import matplotlib.pyplot as plt
import geradenfit as gf

# Konstanten



# Messewrte
#   Messwerte: aufgabeMessung = np.array([]) #Einheit
#   Fehler: d_aufgabeMessung = np.zeros(len(Messwerte))+Fehler / np.array([]) #Einheit



# Rechnung
#   Messwerte: aufgabeGröße = Rechnung #Einheit
#   Fehler: d_aufgabeGröße = Rechnung #Einheit



# Achsen
#   x =
#   y =
#   yerr =

zusammen = ['end'] #<--- Welche Plots zusammengehören. Gleiche Buchstaben werden in einem Plot ausgegeben (Beispiel: ['a','a','b'], die ersten beiden x, y und yerr Werte werden in einem Plot ausgegeben, die dritten x, y, yerr Werte werden in einem Plot ausgegeben).
x = [] #<--- x Werte
xlabel = []
y = [] #<--- y Werte
ylabel = []
yerr = [] #<--- y Fehler (ein Fehler pro x Wert)
xerr = [] #<--- x Fehler (ein Fehler pro x Wert)
color = 'blue' #<--- Farbe der Punkte/Geraden

Auswertung = gf.Auswertung(x,y,yerr,zusammen,color)
Auswertung.auswertung()
