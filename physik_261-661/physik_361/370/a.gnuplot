set terminal epslatex color
set output "output_a.tex"
set title "370.a: Malus'sches Gesetz"
set xlabel '$\phi-\phi_0$ [°]'
set ylabel '$I$ [V]'
set grid
set key box top left
set samples 1000
A = 8
B = 0.01 
C = 1
D = 2
f(x) = A*cos(B*x+C)**2+D
fit f(x) 'a.dat' u 1:2 via A,B,C,D
plot 'a.dat' u 1:2:6:5 with xyerrorbars title 'gemessene Daten' pt 13 pointsize 1,\
        'a.dat' u 3:4:6:5 with xyerrorbars title 'gemessene Daten' pt 13 pointsize 1,\
        f(x) title "Malus'sches Gesetz"

# pt 0 pixel
# pt 1 plus
# pt 13 dot
# lw linewidth
# ps pointsize
# yerrorbars uses last column
