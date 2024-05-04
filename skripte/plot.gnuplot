set terminal epslatex color
set output "output.tex"
set title 'title'
set xlabel '$x$ [\#]'
set ylabel '$y$ [\#]'
set grid
set key box top left width -4
f(x) = m*x+n
fit f(x) 'test.dat' via m,n
chi2 = (FIT_STDFIT*FIT_STDFIT)
set label sprintf("x² = %.5f", chi2) at 2,10
plot 'test.dat' with yerrorbars title 'test data' pt 13 pointsize 1,\
        x**2 title '$x^2$',\
        f(x) title 'straight fit'

# pt 0 pixel
# pt 1 plus
# pt 13 dot
# lw linewidth
# ps pointsize
# yerrorbars uses last column
