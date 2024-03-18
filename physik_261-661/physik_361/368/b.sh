#! /usr/bin/bash

gnuplot 'b.gnuplot'
printf "\n--- done gnuplot ---\n\n"
latex b.tex
printf "\n--- done latex ---\n\n"
pdflatex b.tex
printf "\n--- done ---\n\n"
