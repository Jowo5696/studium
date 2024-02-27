set terminal epslatex color
set output "output.tex"
set title 'title'
set xlabel '$x$ [\#]'
set ylabel '$y$ [\#]'
set grid
set key box top left
f(x) = m*x+n
fit f(x) 'test.dat' via m,n
plot 'test.dat' title with yerrorbars 'test data' pt 13 pointsize 2,\
        x**2 title '$x^2$',\
        f(x) title 'linear regression'

# pt 0 pixel
# pt 1 plus
# pt 13 dot
# lw linewidth
# ps pointsize
# yerrorbars uses last column
