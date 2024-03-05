#! /usr/bin/bash

gnuplot 'a.gnuplot'
printf "\n--- done gnuplot ---\n\n"
latex a.tex
printf "\n--- done latex ---\n\n"
pdflatex a.tex
printf "\n--- done ---\n\n"
