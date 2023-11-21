set terminal epslatex color
set output "240_c_graph.tex"
set title '240.c: Hysteresekurve'
set xlabel "$H$ [T]"
set ylabel "$B$ [T]" 
set grid
set key box b 
plot '240_b_messung_1_straight.dat' with lines title '$\mu _A$',\
        '240_b_messung_1_H_und_B.dat' using 2:3 title 'Messdaten' pointtype 13 pointsize 0.2,\
        '240_b_messung_1_straight_2.dat' with lines title '$\mu _0$'
