#! /usr/bin/bash

gnuplot 'a_strich.gnuplot'
printf "\n--- done gnuplot ---\n\n"
latex a_strich.tex
printf "\n--- done latex ---\n\n"
pdflatex a_strich.tex
printf "\n--- done ---\n\n"
