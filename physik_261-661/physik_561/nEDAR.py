# nEDAR - das neue EDAR
# Christoph Schürmann, 2020
# basierend auf EDAR von Martin Quast

# https://datatofish.com/executable-pyinstaller/
# pyinstaller --onefile nEDAR.py

#import numpy as np
#import matplotlib; matplotlib.use('TkAgg')
from numpy import max as np_max
from numpy import sum as np_sum
from matplotlib import use as mpl_use
mpl_use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from astropy.io.fits import open as fits_open
#import pyfits as fits
from scipy.ndimage import rotate as rotate
from tkinter import *

class nEDAR:
	def __init__(self,window):
		global canvas
		global read,write
		read = [0,0,0]
		write = 0
		#self.window = window
		window.bind("<Return>", self.plot2)
		
		self.r1 = Frame(window, bd=5)
		self.r3 = Frame(window, bd=5)
		self.r2a = Frame(self.r1, bd=2)
		self.r2b = Frame(self.r1, bd=2)
		self.r2c = Frame(self.r1, bd=2)
		
		self.e1 = Entry(self.r2a, width=5)
		self.e2 = Entry(self.r2b, width=5)
		self.e3 = Entry(self.r2c, width=5)
		self.l1 = Label(self.r2a, text="Rotation:", width=10, anchor="e")
		self.l2 = Label(self.r2b, text="Oben:", width=10, anchor="e")
		self.l3 = Label(self.r2c, text="Unten:", width=10, anchor="e")
		
		self.b1 = Button(self.r1, text="Lade Spektrum", width=15, command=self.lese_light)
		self.b2 = Button(self.r1, text="Lade Dunkelbild", width=15, command=self.lese_dark)
		self.b3 = Button(self.r1, text="Lade Kalibrierung", width=15, command=self.lese_cali)
		self.b4 = Button(self.r1, text="Zeige Spektrum", width=15, command=self.plot)
		self.b5 = Button(self.r1, text="Exportiere Daten", width=15, command=self.export)
		
		self.r1.pack(side="top")
		self.r3.pack(side="top")
		self.l1.pack(side="left")
		self.l2.pack(side="left")
		self.l3.pack(side="left")
		self.e1.pack(side="left")
		self.e2.pack(side="left")
		self.e3.pack(side="left")
		self.b1.pack(side="left")
		self.b2.pack(side="left")
		self.b3.pack(side="left")
		self.b4.pack(side="left")
		self.b5.pack(side="left")
		self.r2a.pack(side="left")
		self.r2b.pack(side="left")
		self.r2c.pack(side="left")
		
		fig = Figure(figsize=(12,8))
		canvas = FigureCanvasTkAgg(fig, self.r3)
		canvas.get_tk_widget().pack(side="bottom")
		canvas.draw()
	
	def plot(self):
		global canvas
		global read,write,spe,cal
		
		if self.e1.get()=="":
			rot = 0
		else:
			rot = float(self.e1.get())
		
		if self.e2.get()=="":
			oben = 0
		else:
			oben = int(float(self.e2.get()))
		
		if self.e3.get()=="":
			unten = 510
		else:
			unten = int(float(self.e3.get()))
		
		if read == [1,1,1]:
			write = 1
			canvas.get_tk_widget().pack_forget()
			fig = Figure(figsize=(12,8))
			ax = fig.add_subplot(211)
			a2 = fig.add_subplot(212)
			
			bild = light-dark
			bild_r = rotate(bild,rot,reshape=False)
			cali_r = rotate(cali,rot,reshape=False)
			plot = bild_r/np_max(bild_r)+cali_r/np_max(cali_r)
			
			#ax.plot([0,764],[oben,oben],'r')
			#ax.plot([0,764],[unten,unten],'r')
			
			ax.imshow(plot, cmap="gray", clim=(0,1))
			ax.set_ylim(unten,oben)
			ax.set_xlabel("Pixelkoordinate x")
			ax.set_ylabel("Pixelkoordinate y")
			
			spe = np_sum(bild_r[oben:unten],axis=0)
			cal = np_sum(cali_r[oben:unten],axis=0)
			
			a2.plot(range(len(spe)),spe/np_max(spe),'b')
			a2.plot(range(len(cal)),cal/np_max(cal),'r')
			a2.set_xlim(0,len(spe))
			
			canvas = FigureCanvasTkAgg(fig, self.r3)
			canvas.get_tk_widget().pack()
			canvas.draw()
	
	def plot2(self,event):
		self.plot()
	
	def lese_light(self):
		global light,read
		fname = filedialog.askopenfile()
		light = fits_open(fname.name)[0].data *1.
		#light = np.array(fits.getdata(fname.name))*1.
		read[0] = 1
	
	def lese_dark(self):
		global dark,read
		fname = filedialog.askopenfile()
		dark = fits_open(fname.name)[0].data *1.
		read[1] = 1
	
	def lese_cali(self):
		global cali,read
		fname = filedialog.askopenfile()
		cali = fits_open(fname.name)[0].data *1.
		read[2] = 1
	
	def export(self):
		global spe,cal
		global write
		if write==1:
			f = open("output.dat","w")
			for i in range(len(spe)):
				f.write(str(i)+"\t"+str(spe[i])+"\t"+str(cal[i])+"\n")

window = Tk()
window.title("nEDAR")
nEDAR(window)
window.mainloop()