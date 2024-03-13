#! /usr/bin/bash

gnuplot 'c2.gnuplot'
printf "\n--- done gnuplot ---\n\n"
latex c2.tex
printf "\n--- done latex ---\n\n"
pdflatex c2.tex
printf "\n--- done ---\n\n"
