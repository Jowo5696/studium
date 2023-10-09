import numpy as np
import matplotlib.pyplot as plt
import geradenfit as gf

g = 9.81

Fit = gf.nmvnvm()

aAnzahl_Messungen = 8

aDelta_Auslenkung_Messung = np.zeros(aAnzahl_Messungen)+1*0.1

aAlu_Auslenkung0 = 89
aAlu_Gewicht = np.array([0,50, 100, 150, 200, 250, 300, 350])
aAlu_Auslenkung = np.array([89,75, 62, 47, 34, 19, 4, 0])
aAlu_Auslenkung_korrigiert = abs(aAlu_Auslenkung-aAlu_Auslenkung0)
aAlu_Last = aAlu_Gewicht*0.001*g

aKupfer_Auslenkung0 = 96
aKupfer_Gewicht = np.array([0,50, 100, 150, 200, 250, 300, 350])
aKupfer_Auslenkung = np.array([96,90, 81, 74, 66, 58, 51, 42])
aKupfer_Auslenkung_korrigiert = abs(aKupfer_Auslenkung-aKupfer_Auslenkung0)
aKupfer_Last = aKupfer_Gewicht*0.001*g

aStahl_Auslenkung0 = 94
aStahl_Gewicht = np.array([0,50, 100, 150, 200, 250, 300, 350])
aStahl_Auslenkung = np.array([94,85, 76, 67, 57, 48, 39, 29])
aStahl_Auslenkung_korrigiert = abs(aStahl_Auslenkung0-aStahl_Auslenkung)
aStahl_Last = aStahl_Gewicht*0.001*g

aGewicht = np.ndarray(shape=(3,8),dtype=np.double)
aGewicht[0] = aAlu_Gewicht
aGewicht[1] = aKupfer_Gewicht
aGewicht[2] = aStahl_Gewicht
print(aGewicht)

aAuslenkung = np.ndarray(shape=(3,8),dtype=np.double)
aAuslenkung[0] = aAlu_Auslenkung_korrigiert*0.1
aAuslenkung[1] = aKupfer_Auslenkung_korrigiert*0.1
aAuslenkung[2] = aStahl_Auslenkung_korrigiert*0.1
print('aAuslenkung',aAuslenkung)

aDelta_Auslenkung = np.ndarray(shape=(3,8),dtype=np.double)
aDelta_Auslenkung[0] = aDelta_Auslenkung_Messung*0.1
aDelta_Auslenkung[1] = aDelta_Auslenkung_Messung*0.1
aDelta_Auslenkung[2] = aDelta_Auslenkung_Messung*0.1
print('aDelta_Auslenkung',aDelta_Auslenkung)

aLast = np.ndarray(shape=(3,8),dtype=np.double)
aLast[0] = aAlu_Last
aLast[1] = aKupfer_Last
aLast[2] = aStahl_Last
print('aLast',aLast)

results = np.ndarray(shape=(3,4),dtype=np.double)
aGerade = np.ndarray(shape=(3,8),dtype=np.double)
aGerade_vn_p = np.ndarray(shape=(3,8),dtype=np.double)
aGerade_vn_m = np.ndarray(shape=(3,8),dtype=np.double)

for i in range(len(aLast)):
    plt.errorbar(x=aLast[i],y=aAuslenkung[i],yerr=aDelta_Auslenkung[i],fmt='r+')
    results[i] = Fit.n_m_vn_vm(x=aLast[i],y=aAuslenkung[i],yerr=aDelta_Auslenkung[i])
    aGerade[i] = results[i][1]*aLast[i]+results[i][0]
    aGerade_vn_p[i] = aGerade[i]+results[i][2]
    aGerade_vn_m[i] = aGerade[i]-results[i][2]
    plt.plot(aLast[i],aGerade[i],'b')
    plt.plot(aLast[i],aGerade_vn_p[i],'b--')
    plt.plot(aLast[i],aGerade_vn_m[i],'b--')

print('aGerade',aGerade)
print('results',results)

plt.show()

print('----------b----------')

bDelta_Auslenkung_Messung = 0.1

bStahl_Auslenkung0 = 923.5
bStahl_Gewicht = np.array([0,2000, 3000, 4000, 4100, 4200, 4250, 4300])
bStahl_Auslenkung = np.array([923.5,923.3, 923.1, 925.3, 927.9, 931.5, 947.1, 966.5])
bStahl_Auslenkung_korrigiert = abs(bStahl_Auslenkung-bStahl_Auslenkung0)
bStahl_Last = bStahl_Gewicht*0.001*g

bPVC_Auslenkung0 = 922.8
bPVC_Gewicht = np.array([0,1000, 2000, 2100, 2200, 2300, 2400, 2450])
bPVC_Auslenkung = np.array([922.8,922.9, 924.2, 925.1, 926.7, 930.5, 942.0, 951.0])
bPVC_Auslenkung_korrigiert = abs(bPVC_Auslenkung-bPVC_Auslenkung0)
bPVC_Last = bPVC_Gewicht*0.001*g

bGFK_Auslenkung0 = 923.3
bGFK_Gewicht = np.array([0,4000, 6500, 7000, 7500, 7600, 7700, 7750])
bGFK_Auslenkung = np.array([923.3,924.1, 927.5, 930.9, 944.5, 950.4, 958.2, 959.6])
bGFK_Auslenkung_korrigiert = abs(bGFK_Auslenkung-bGFK_Auslenkung0)
bGFK_Last = bGFK_Gewicht*0.001*g

bGewicht = np.ndarray(shape=(3,8),dtype=np.double)
bGewicht[0] = bStahl_Gewicht
bGewicht[1] = bPVC_Gewicht
bGewicht[2] = bGFK_Gewicht
print('bGewicht',bGewicht)

bAuslenkung = np.ndarray(shape=(3,8),dtype=np.double)
bAuslenkung[0] = bStahl_Auslenkung_korrigiert
bAuslenkung[1] = bPVC_Auslenkung_korrigiert
bAuslenkung[2] = bGFK_Auslenkung_korrigiert
print('bAuslenkung',bAuslenkung)

bDelta_Auslenkung = np.ndarray(shape=(3,8),dtype=np.double)
bDelta_Auslenkung[0] = bDelta_Auslenkung_Messung
bDelta_Auslenkung[1] = bDelta_Auslenkung_Messung
bDelta_Auslenkung[2] = bDelta_Auslenkung_Messung
print('bDelta_Auslenkung',bDelta_Auslenkung)

bLast = np.ndarray(shape=(3,8),dtype=np.double)
bLast[0] = bStahl_Last
bLast[1] = bPVC_Last
bLast[2] = bGFK_Last
print('bLast',bLast)

results = np.ndarray(shape=(3,4),dtype=np.double)
bGerade = np.ndarray(shape=(3,8),dtype=np.double)
bGerade_vn_p = np.ndarray(shape=(3,8),dtype=np.double)
bGerade_vn_m = np.ndarray(shape=(3,8),dtype=np.double)

for i in range(len(bLast)):
    plt.errorbar(x=bLast[i],y=bAuslenkung[i],yerr=bDelta_Auslenkung[i],fmt='r+')
    results[i] = Fit.n_m_vn_vm(x=bLast[i],y=bAuslenkung[i],yerr=bDelta_Auslenkung[i])
    bGerade[i] = results[i][1]*bLast[i]+results[i][0]
    bGerade_vn_p[i] = bGerade[i]+results[i][2]
    bGerade_vn_m[i] = bGerade[i]-results[i][2]
    plt.plot(bLast[i],bGerade[i],'b')
    plt.plot(bLast[i],bGerade_vn_p[i],'b--')
    plt.plot(bLast[i],bGerade_vn_m[i],'b--')

print('bGerade',bGerade)
print('results',results)

plt.show()

print('----------d----------')


a = np.array([0,25,50,75,100])

dPerioden = np.array([3, 5, 7, 9, 10])


a_25_50_75_100 = np.ndarray(shape=(4,5),dtype=float)
a_25_50_75_100[0] = np.array([4.2, 7.0, 10.0, 12.2, 14.2])
a_25_50_75_100[1] = np.array([5.5, 9.2, 12.8, 16.4, 18.3])
a_25_50_75_100[2] = np.array([7.0, 11.8, 16.5, 21.2, 23.6])
a_25_50_75_100[3] = np.array([8.6, 14.5, 20.3, 26.3, 29.3])

dPerioden0 = np.array([5, 6, 7, 8, 9, 11, 12, 13, 14, 15])
a0 = np.array([6.0, 7.2, 8.5, 9.7, 11.0, 13.4, 14.7, 16.0, 17.2, 18.4])

dDelta_t = np.zeros(len(dPerioden))+0.5
dDelta_t0 = np.zeros(len(dPerioden0))+0.5

T = np.ndarray(shape=(4,5),dtype=float)
for i in range(4):
    T[i] = a_25_50_75_100[i]/dPerioden
print('T',T)
delta_T = np.ndarray(shape=(4,5),dtype=float)
for i in range(4):
    delta_T[i] = 1/dPerioden*dDelta_t[i]
print('delta_T',delta_T)

T0 = np.ndarray(shape=(len(dPerioden0),1),dtype=float)
for i in range(len(dPerioden0)):
    T0[i] = a0[i]/dPerioden0[i]
print('T0',T0)
delta_T0 = np.ndarray(shape=(len(dPerioden0),1),dtype=float)
for i in range(len(dPerioden0)):
    delta_T0[i] = 1/dPerioden0[i]*dDelta_t0[i]
print('delta_T0',delta_T0)

T0_mittel = T0.sum()/len(T0)
print('T0_mittel',T0_mittel)
delta_T0_mittel = delta_T0.sum()/len(T0)
print('delta_T0_mittel',delta_T0_mittel)

T_ges = np.ndarray(shape=(5,5),dtype=float)
T_ges[0][:] = T0_mittel
T_ges[1] = T[0]
T_ges[2] = T[1]
T_ges[3] = T[2]
T_ges[4] = T[3]
print('T_ges',T_ges)
delta_T_ges = np.ndarray(shape=(5,5),dtype=float)
delta_T_ges[0] = delta_T0_mittel
delta_T_ges[1] = delta_T[0]
delta_T_ges[2] = delta_T[0]
delta_T_ges[3] = delta_T[0]
delta_T_ges[4] = delta_T[0]

T_ges_mittel = np.zeros(5)
for i in range(5):
    T_ges_mittel[i] = T_ges[i].sum()/len(T_ges[i])
print('T_ges_mittel',T_ges_mittel)
delta_T_ges_mittel = np.zeros(5)
for i in range(5):
    delta_T_ges_mittel[i] = delta_T_ges[i].sum()/len(delta_T_ges[i])
print('delta_T_ges_mittel',delta_T_ges_mittel)

T_ges_mittel_sq = T_ges_mittel**2
print('T_ges_mittel_sq',T_ges_mittel_sq)
delta_T_ges_mittel_sq = 2*T_ges_mittel*delta_T_ges_mittel
print('delta_T_ges_mittel_sq',delta_T_ges_mittel_sq)
a_sq = a**2
print('a_sq',a_sq)

results = np.ndarray(shape=(4),dtype=float)
dGerade = np.ndarray(shape=(5),dtype=float)

results = Fit.n_m_vn_vm(x=a_sq,y=T_ges_mittel_sq,yerr=delta_T_ges_mittel_sq)
dGerade = results[1]*a_sq+results[0]
plt.errorbar(x=a_sq,y=T_ges_mittel_sq,yerr=delta_T_ges_mittel_sq)
plt.plot(a_sq,dGerade,'b')

plt.show()
