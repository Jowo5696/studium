set terminal epslatex color
set output "output_c.tex"
set title '372.c: Abhängigkeit Abstand -- Fluss'
set xlabel '$\frac{1}{r^2}$ [1/m²]'
set ylabel '$\frac{\Phi}{A}$ [W/m²]'
set grid
set key box top left
f(x) = m*x+n
fit f(x) 'c.dat' via m,n
plot 'c.dat' u 1:2:3:4 with xyerrorbars title 'gemessene Daten' pt 13 pointsize 1,\
        f(x) title 'straight fit'

# pt 0 pixel
# pt 1 plus
# pt 13 dot
# lw linewidth
# ps pointsize
# yerrorbars uses last column
