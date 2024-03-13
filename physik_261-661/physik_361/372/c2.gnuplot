set terminal epslatex color 
set output "output_c2.tex"
set title '372.c: Stefan--Boltzmann--Gesetz, logarithmisch'
set xlabel '$\log (T)$ [K]'
set ylabel '$\log(\frac{\Phi}{A})$ [W/m²]'
set grid
set key box top left
f(x) = m*x+n
fit f(x) 'c2.dat' u 1:2 via m,n
chi2 = (FIT_STDFIT*FIT_STDFIT)
set label sprintf("x² = %.3f", chi2) at 3.05,5.2
plot 'c2.dat' u 1:2:3:4 with xyerrorbars title 'gemessene Daten' pt 13 pointsize 1,\
        f(x) title 'straight fit'

# pt 0 pixel
# pt 1 plus
# pt 13 dot
# lw linewidth
# ps pointsize
# yerrorbars uses last column
