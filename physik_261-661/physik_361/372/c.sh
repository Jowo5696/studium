#! /usr/bin/bash

gnuplot 'c.gnuplot'
printf "\n--- done gnuplot ---\n\n"
latex c.tex
printf "\n--- done latex ---\n\n"
pdflatex c.tex
printf "\n--- done ---\n\n"
