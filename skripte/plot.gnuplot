set terminal epslatex color
set output "output.tex"
set title 'title'
set xlabel '$x$ [\#]'
set ylabel '$y$ [\#]'
set grid
set key box top left
plot 'test.dat' title 'test data' with linespoint pt 13,\
        x**2 title '$x^2$'

# pt 0 pixel
# pt 1 plus
# pt 13 dot
# lw linewidth
# ps pointsize
