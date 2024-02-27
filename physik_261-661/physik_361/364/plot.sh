#! /usr/bin/bash

gnuplot 'plot.gnuplot'
printf "\n--- done gnuplot ---\n\n"
latex plot.tex
printf "\n--- done latex ---\n\n"
pdflatex plot.tex
printf "\n--- done ---\n\n"
