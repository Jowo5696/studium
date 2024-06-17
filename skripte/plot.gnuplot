set terminal epslatex color
set output "output.tex"
set title 'title'
set xlabel '$x$ [\#]'
set ylabel '$y$ [\#]'
set grid
set key box top left width -4 # 'samplen x' sets how much space the symbol takes

set style line 1 lt rgb "#1f78b4" pt 13 ps .5 # blue
set style line 2 lt rgb "#33a02c" pt 13 ps .5 # green
set style line 3 lt rgb "#e31a1c" pt 13 ps .5 # red
set style line 4 lt rgb "#fdbf6f" pt 13 ps .5 # yellow
set style line 5 lt rgb "#ff7f00" pt 13 ps .5 # orange
set style line 6 lt rgb "#6a3d9a" pt 13 ps .5 # purple
set style line 7 lt rgb "#a6cee3" pt 13 ps .5 # pastel blue
set style line 8 lt rgb "#b2df8a" pt 13 ps .5 # pastel green
set style line 9 lt rgb "#fb9a99" pt 13 ps .5 # pastel red
set style line 10 lt rgb "#cab2d6" pt 13 ps .5 # pastel purple

f(x) = m*x+n
fit f(x) 'test.dat' via m,n
chi2 = (FIT_STDFIT*FIT_STDFIT)
set label sprintf("x² = %.5f", chi2) at 2,10
plot 'test.dat' with yerrorbars title 'test data' ls 1,\
        x**2 title '$x^2$',\
        f(x) title 'straight fit'
# NaN with points / lines title '' ls 1 # fake legend

# pt 0 pixel
# pt 1 plus
# pt 13 dot
# lw linewidth
# ps pointsize
# yerrorbars uses last column
# lc rgb #d95f02 (orange) #1b9e77 (green) #7570b3 (blue)
