set terminal epslatex color 
set output "output_b.tex"
set title '372.b: Lesliewürfel'
set xlabel '$T^4-T_0^4$ [K]'
set ylabel '$\frac{\Phi}{F}$ [W/m²]'
set grid
set key box top left width -5

m = .0001
n = -1e-8
f(x) = m*x+n
fit f(x) 'b.dat' every ::1::10 using 1:2 via m,n
chi2=(FIT_STDFIT*FIT_STDFIT)
set label sprintf("x² = %.3f", chi2) at 4.85e+9,25 

o = .0001
p = -1e-8
g(x) = o*x+p
fit g(x) 'b.dat' every ::11::20 using 1:2 via o,p 
chi2=(FIT_STDFIT*FIT_STDFIT)
set label sprintf("x² = %.3f", chi2) at 5.5e+9,20

q = .0001
r = -1e-8
h(x) = q*x+r
fit h(x) 'b.dat' every ::21::30 using 1:2 via q,r
chi2=(FIT_STDFIT*FIT_STDFIT)
set label sprintf("x² = %.3f", chi2) at 5e+9,6.5

s = .0001
t = -1e-8
i(x) = s*x+t
fit i(x) 'b.dat' every ::31::40 using 1:2 via s,t
chi2=(FIT_STDFIT*FIT_STDFIT)
set label sprintf("x² = %.3f", chi2) at 5e+9,0

#j(x) = (5.670e-8)*x

plot 'b.dat' every ::1::10 u 1:2:3:4 with xyerrorbars title 'schwarze Lackierung' pt 13 pointsize 1,\
        'b.dat' every ::11::20 u 1:2:3:4 with xyerrorbars title 'weiße Lackierung' pt 13 pointsize 1,\
        'b.dat' every ::21::30 u 1:2:3:4 with xyerrorbars title 'mattes Metall' pt 13 pointsize 1,\
        'b.dat' every ::31::40 u 1:2:3:4 with xyerrorbars title 'poliertes Metall' pt 13 pointsize 1,\
        f(x) notitle linecolor rgb '#9400D4' lw 2,\
        g(x) notitle linecolor rgb '#009E73' lw 2,\
        h(x) notitle linecolor rgb '#57B5E8' lw 2,\
        i(x) notitle linecolor rgb '#E69E00' lw 2
#        j(x) title 'Schwarzer Körper' linecolor rgb '#000000' lw 2

# pt 0 pixel
# pt 1 plus
# pt 13 dot
# lw linewidth
# ps pointsize
# yerrorbars uses last column
