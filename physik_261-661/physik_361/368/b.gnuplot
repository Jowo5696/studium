set terminal epslatex color
set output "output_b.tex"
set title '368.b: Wellenlänge Na--Lampe'
set xlabel '$m$ [\#]'
set ylabel '$x_m$ [m]'
set grid
set key box top left
f(x) = m*x+n
fit f(x) 'b.dat' u 1:2 via m,n
chi2 = (FIT_STDFIT*FIT_STDFIT)
set label sprintf("x² = %.8f", chi2) at 6.5,0.01
plot 'b.dat' u 1:2:3 with yerrorbars title 'gemessene Daten' pt 13 pointsize 1,\
        f(x) title 'straight fit'

# pt 0 pixel
# pt 1 plus
# pt 13 dot
# lw linewidth
# ps pointsize
# yerrorbars uses last column
