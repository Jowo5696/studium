#! /usr/bin/bash


python table.py > table.tex
latex table.tex
pdflatex table.tex
zathura table.pdf
