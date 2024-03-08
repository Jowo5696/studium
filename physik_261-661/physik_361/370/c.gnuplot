set terminal epslatex color
set output "output_c.tex"
set title '370.c: Spezifisches Drehvermögen'
set xlabel 'Konzentration [cm$\cdot$mol/Liter]'
set ylabel '$\phi - \phi_0$ [°]'
set grid
set key box top left width -3
f(x) = m*x+n
fit f(x) 'c.dat' u 1:2 via m,n
plot 'c.dat' u 1:2:3 with yerrorbars title 'gemessene Daten' pt 13 pointsize 1,\
        f(x) title 'straight fit'

# pt 0 pixel
# pt 1 plus
# pt 13 dot
# lw linewidth
# ps pointsize
# yerrorbars uses last column
