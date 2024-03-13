#! /usr/bin/bash

gnuplot 'a2.gnuplot'
printf "\n--- done gnuplot ---\n\n"
latex a2.tex
printf "\n--- done latex ---\n\n"
pdflatex a2.tex
printf "\n--- done ---\n\n"
