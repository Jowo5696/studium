set terminal epslatex color
set output "output.tex"
set title '364.h: Wellenlänge des Lichts'
set xlabel '$\frac{1}{D}$ $[\frac{1}{m}]$'
set ylabel '$\alpha$ [rad]'
set grid
set key box top left
f(x) = m*x+n
fit f(x) 'alpha.dat' using 2:1 via m,n
plot 'alpha.dat' using 2:1:3 with yerrorbars title 'berechnete Daten' pt 13 pointsize 2,\
        f(x) title 'straight fit'

# pt 0 pixel
# pt 1 plus
# pt 13 dot
# lw linewidth
# ps pointsize
