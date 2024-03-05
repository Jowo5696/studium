set terminal epslatex color
set output "output_a_strich.tex"
set title '362.a: Abbe-Verfahren'
set xlabel '$1+\gamma$ [1]'
set ylabel "$x'$ [m]"
set grid
set key box top right
f(x) = m*x+n
fit f(x) 'a.dat' using 6:5 via m,n
plot 'a.dat' using 6:5:8:7 with xyerrorbars title 'gemessene Daten, gestrichen' pt 13 pointsize 2,\
        f(x) title 'straight fit, gestrichen'

# pt 0 pixel
# pt 1 plus
# pt 13 dot
# lw linewidth
# ps pointsize
# yerrorbars uses last column
