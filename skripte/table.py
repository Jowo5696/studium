import numpy as np


print('\\documentclass[a4paper,12pt]{article}\n\\usepackage{amsmath,amsfonts,amssymb}\n\\begin{document}')

y = np.array([1,2,3,4,5])
x_sq = np.array([1,4,9,16,25])

counter = 2

def main(f,x):

    print('\t$y$ & $x^2$\\\\')
    print('\t\\hline')
    for i in range(len(f)-1):
        print('\t',f[i],'&',x[i],r'\\')
    print('\t',f[-1],'&',x[-1])


print('\\noindent Tabelle 1: $f\\left(x\\right) = x^2$\\\\\\\\')
print('\\begin{tabular}{',len(y)*'l','}')
main(y,x_sq)
print('\\end{tabular}\n\\end{document}')
