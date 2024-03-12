set terminal epslatex color
set output "output_b.tex"
set title '370.b: Drehvermögen von Quarz'
set xlabel '$\lambda^{-2}$ [1/nm²]'
set ylabel '$\phi - \phi_0$ [°]'
set grid
set xtics rotate by -30 offset .5
set key box top left width -11
m = 3.8e-11
f(x) = m*x+n
fit f(x) 'b.dat' u 1:2 via m,n
plot 'b.dat' u 1:2:3 with yerrorbars title 'gemessene Daten' pt 13 pointsize 1,\
        f(x) title "straight fit, Biot'sches Gesetz"

# pt 0 pixel
# pt 1 plus
# pt 13 dot
# lw linewidth
# ps pointsize
# yerrorbars uses last column
