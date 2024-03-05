set terminal epslatex color
set output "output.tex"
set title '366.c: Kalibrationskurve'
set xlabel 'Ablenkwinkel [°]'
set ylabel 'Wellenlänge [nm]'
# set xtics rotate by 45 offset -0.8,-2.2
set grid
set key box top right
#f(x) = m*x+b
#fit f(x) '366_e.dat' using 1:2 via m,b
plot '366_c.dat' with xerrorbars title 'gemessene Daten' pt 13 pointsize 1
#        f(x) title 'straight fit'

# pt 0 pixel
# pt 1 plus
# pt 13 dot
# lw linewidth
# ps pointsize
# yerrorbars uses last column
