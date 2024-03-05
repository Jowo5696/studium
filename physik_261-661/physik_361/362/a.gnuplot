set terminal epslatex color
set output "output_a.tex"
set title '362.a: Abbe-Verfahren'
set xlabel '$1+\frac{1}{\gamma}$ [1]'
set ylabel '$x$ [m]'
set grid
set key box top left
f(x) = m*x+n
fit f(x) 'a.dat' using 2:1 via m,n
plot 'a.dat' using 2:1:4:3 with xyerrorbars title 'gemessene Daten' pt 13 pointsize 2,\
        f(x) title 'straight fit'

# pt 0 pixel
# pt 1 plus
# pt 13 dot
# lw linewidth
# ps pointsize
# yerrorbars uses last column
