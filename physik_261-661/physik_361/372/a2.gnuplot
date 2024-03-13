set terminal epslatex color
set output "output_a2.tex"
set title '372.a: Ansprechzeit'
set ylabel '$U$ [mV]'
set xlabel '$t$ [s]'
set grid
set key box bottom right width -3
f(x) = 0.9
set arrow from 68, graph 0 to 68, graph 1 nohead linecolor rgb '#10A769' lw 2
plot 'a2.dat' u 1:2:4:3 with xyerrorbars title 'gemessene Daten' pt 13 pointsize 1,\
        f(x) title '$90\%$' lw 2


# pt 0 pixel
# pt 1 plus
# pt 13 dot
# lw linewidth
# ps pointsize
# yerrorbars uses last column
