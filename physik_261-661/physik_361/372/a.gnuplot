set terminal epslatex color
set output "output_a.tex"
set title '372.a: Offsetspannung'
set ylabel '$U_0$ [mV]'
set xlabel '$t$ [s]'
set grid
set key box top left width -3
plot 'a.dat' u 1:2:3 with yerrorbars title 'gemessene Daten' pt 13 pointsize 1

# pt 0 pixel
# pt 1 plus
# pt 13 dot
# lw linewidth
# ps pointsize
# yerrorbars uses last column
