#! /usr/bin/bash


python 362.py > a_table.tex
latex a_table.tex
pdflatex a_table.tex
zathura a_table.pdf
