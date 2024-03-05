import numpy as np


def table(x_1,y_1,xerr_1,yerr_1,x_2,y_2,xerr_2,yerr_2):
    print('\\documentclass[a4paper,12pt]{article}\n\\usepackage{amsmath,amsfonts,amssymb}\n\\begin{document}')
    print('\\noindent Tabelle 362.a: Abbe--Verfahren\\\\\\\\')
    print('\\begin{tabular}{',len(x_1)*'l','}')
    print('\t',r"$x$ [m] & $1+\frac{1}{\gamma}$ [1] & $\Delta x$ [m] & $\Delta \left(1+\frac{1}{\gamma}\right)$ [1] & $x'$ [m] & $1+\gamma$ [m] & $\Delta x'$ [m] & $\Delta \left(1+\gamma\right)$ [1]",r'\\')                                                                                               
    print('\t\\hline')
    for i in range(len(x_1)-1):
        print('\t',np.round(x_1[i],3),'&',np.round(y_1[i],3),'&',np.round(xerr_1[i],3),'&',np.round(yerr_1,3),'&',np.round(x_2[i],3),'&',np.round(y_2[i],3),'&',np.round(xerr_2[i],3),'&',np.round(yerr_2,3),r'\\')
    print('\t',np.round(x_1[-1],3),'&',np.round(y_1[-1],3),'&',np.round(xerr_1[-1],3),'&',np.round(yerr_1,3),'&',np.round(x_2[-1],3),'&',np.round(y_2[-1],3),'&',np.round(xerr_2[-1],3),'&',np.round(yerr_2,3),r'\\')
    print('\\end{tabular}\n\\end{document}')


def a():

    G = 2.2*1e-2 #m
    DG = 0.1*1e-2 #m
    X = 30.0*1e-2 #m
    DX = 0.1*1e-2 #m

    x_tilde = np.array([15.7,15.6,15.5,15.4,15.1,14.9,14.7,14.6,13.7,12.8])*1e-2 #m
    x_strich_tilde = np.array([76.0,72.0,68.0,64.0,60.0,56.0,52.0,48.0,44.0,40.0])*1e-2 #m

    B = np.array([18.7,16.9,15.0,13.3,11.5,9.7,8.0,6.5,4.7,3.1])*1e-2 #m
    DB = 0.2*1e-2

    Delta_tilde = 0.2*1e-2 #m

    x = X - x_tilde
    Dx = ( (DX)**2 + (Delta_tilde)**2 )**0.5

    x_strich = X - x_strich_tilde
    Dx_strich = Dx 

    gamma = B/G
    Dgamma = ( (DB/G)**2 + (B/G**2*DG)**2 )**0.5

    y_1 = x
    x_1 = 1+1/gamma
    yerr_1 = Dx
    xerr_1 = 1/gamma**2*Dgamma

    y_2 = x_strich
    x_2 = 1+gamma
    yerr_2 = Dx_strich
    xerr_2 = Dgamma

#    print('y_1','x_1','yerr_1','xerr_1','y_2','x_2','yerr_2','xerr_2')
#    for i in range(len(x)):
#        print(np.round(y_1[i],3),np.round(x_1[i],3),np.round(yerr_1,3),np.round(xerr_1[i],3),np.round(y_2[i],3),np.round(x_2[i],3),np.round(yerr_2,3),np.round(xerr_2,3))

    table(x_1,y_1,xerr_1,yerr_1,x_2,y_2,xerr_2,yerr_2)

def d():

    x = np.array([1,3,5,7,9,1,3,5,7,9,4,4,4,4,4,6,6,6,6,6])
    y = np.array([2,2,2,2,2,4,4,4,4,4,1,2,3,4,5,1,2,3,4,5])

    hintergrund = 0.8

    helligkeit_e = np.array([18.30,11.22,11.24,10.52,15.10,15.19,12.05,13.05,13.20,22.62,10.44,11.75,12.40,13.81,13.37,10.68,11.30,12.40,13.92,14.02])-hintergrund
    helligkeit_f = np.array([1204, 1206, 1210, 1152, 795, 1105, 1367, 1470, 1315, 1245, 1235, 1355, 1500, 1607, 1447, 1000, 1050, 1398, 1399, 1392])*1e-2-hintergrund
    helligkeit_g = np.array([805, 905, 995, 920, 700, 530, 735, 1002, 807, 684, 950, 1032, 1036, 942, 734, 1092, 1162, 1172, 1030, 820])*1e-2-hintergrund

    delta = 0.2

#    print('#','x','y','helligkeit_e','helligkeit_f','helligkeit_g','delta')
#    print('')
#    for i in range(len(x)):
#        print(x[i],y[i],np.round(helligkeit_e[i],2),np.round(helligkeit_f[i],2),np.round(helligkeit_g[i],2),delta)

    matrix_e = np.zeros((9,5))
    matrix_f = np.zeros((9,5))
    matrix_g = np.zeros((9,5))
    matrix_e[x-1,y-1] = helligkeit_e
    matrix_f[x-1,y-1] = helligkeit_f
    matrix_g[x-1,y-1] = helligkeit_g

#    for i in range(9):
#        for j in range(5):
#            print(matrix_e[i][j],'',end='')
#    for i in range(9):
#        for j in range(5):
#            print(matrix_f[i][j],'',end='')
#    for i in range(9):
#        for j in range(5):
#            print(matrix_g[i][j],'',end='')


    for i in range(20):
        print(i,np.round(helligkeit_e[i],2),np.round(helligkeit_f[i],2),np.round(helligkeit_g[i],2),delta)

#a()
d()
