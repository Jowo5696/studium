#! /usr/bin/bash

gnuplot 'e.gnuplot'
printf "\n--- done gnuplot ---\n\n"
latex e.tex
printf "\n--- done latex ---\n\n"
pdflatex e.tex
printf "\n--- done ---\n\n"
