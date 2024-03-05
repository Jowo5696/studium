set terminal epslatex color
set output "output_e.tex"
set title '362.3: Bildausleuchtung'
set xlabel 'Feld'
set ylabel 'Bildfeldausleuchtung [Lux]'
set grid
set key box width -5 top right
plot 'e.dat' u 1:2:5 with yerrorbars title '362.e: $f=100$mm' pt 13 pointsize 1,\
        'e.dat' u 1:3:5 with yerrorbars title '362.f: $f=100$mm, rotiert' pt 13 pointsize 1,\
        'e.dat' u 1:4:5 with yerrorbars title '362.g: $f=53$mm' pt 13 pointsize 1

# pt 0 pixel
# pt 1 plus
# pt 13 dot
# lw linewidth
# ps pointsize
# yerrorbars uses last column
