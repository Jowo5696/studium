import numpy as np
import matplotlib.pyplot as plt

class Gerade:

    def __init__(self):
        pass

    def mnvmvn(self,x,y,yerr):

        print('----------')

        x_bar = ((x/yerr**2)).sum()/(1/yerr**2).sum()
        print('x_bar',x_bar)

        x_bar_sq = x_bar**2
        print('x_bar_sq',x_bar_sq)

        x_sq_bar = ((x**2)/(yerr**2)).sum()/(1/yerr**2).sum()
        print('x_sq_bar',x_sq_bar)

        y_bar = (y/yerr**2).sum()/(1/yerr**2).sum()
        print('y_bar',y_bar)

        xy_bar = ((x*y)/(yerr)**2).sum()/(1/(yerr)**2).sum()
        print('xy_bar',xy_bar)

        sigma_sq = x.size/(1/yerr**2).sum()
        print('sigma_sq',sigma_sq)

        m = (xy_bar-x_bar*y_bar)/(x_sq_bar-x_bar_sq)
        print('m',m)

        n = (x_sq_bar*y_bar-x_bar*xy_bar)/(x_sq_bar-x_bar_sq)
        print('n',n)

        v_m = (sigma_sq/(x.size*(x_sq_bar-x_bar_sq)))**0.5
        print('sigma_m',v_m)

        v_n = ((sigma_sq*x_sq_bar)/(x.size*(x_sq_bar-x_bar_sq)))**0.5
        print('sigma_n',v_n)

        print('----------')

        return m,n,v_m,v_n


class Auswertung:

    def __init__(self,x,xlabel,y,ylabel,yerr,xerr,title,label,color,zusammen):
        self.Gerade = Gerade()
        self.x = x
        self.xlabel = xlabel
        self.y = y
        self.ylabel = ylabel
        self.yerr = yerr
        self.xerr = xerr
        self.title = title
        self.label = label
        self.color = color
        self.zusammen = zusammen

    def auswertung(self):
        font = {"fontname":"Computer Modern", "family":"serif"}
        mnvmvn = np.ndarray(shape=(len(self.x),4),dtype=float)

        for i in range(len(self.x)):
            mnvmvn[i] = self.Gerade.mnvmvn(self.x[i],self.y[i],self.yerr[i])
            steigung = mnvmvn[i][0]
            steigung_plus = mnvmvn[i][0]-mnvmvn[i][2]
            steigung_minus = mnvmvn[i][0]-mnvmvn[i][2]
            b = mnvmvn[i][1]
            fit = steigung*self.x[i]+b
            fit_plus = steigung*self.x[i]+b+mnvmvn[i][3]
            fit_minus = steigung*self.x[i]+b-mnvmvn[i][3]

            plt.errorbar(self.x[i],self.y[i],self.yerr[i],self.xerr[i],fmt=self.color[i],ls="",marker=".",label=self.label[i]+' Messwerte',capsize=3,linewidth=0.5)
            plt.plot(self.x[i],fit,self.color[i],label=self.label[i]+' Geradenfit',linewidth=0.8)
            plt.plot(self.x[i],fit_plus,'b--',label='error +/-',linewidth=0.5)
            plt.plot(self.x[i],fit_minus,'b--',linewidth=0.5)

            plt.xlabel(self.xlabel[0],font)
            plt.ylabel(self.ylabel[0],font)
            plt.title(self.title[0],font)
            plt.legend(loc='best')
            plt.grid()

            if len(self.zusammen) == 1:
                plt.show()
                break
            elif self.zusammen[i] == 'end':
                break
            elif self.zusammen[i] == self.zusammen[i+1]:
                continue
            else:
                plt.show()
