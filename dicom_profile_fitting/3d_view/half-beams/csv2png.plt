#!/usr/bin/gnuplot

# This script generates output file from input defined in .csv file
# edit file_names in here and run the script with : gnuplot csv2png

set term pngcairo enhanced size 800,600
set output "whole_half_beam_4mv.png"
set datafile separator ","
set xrange [-512:512]
set yrange [-512:512]
set zrange [-5:55]
set xtics 128
set ytics 128
set ticslevel 0
set grid
set border 4095
set grid mxtics mytics mztics
set xlabel "x [px]"
set ylabel "y [px]"
set zlabel "Pixel value in thousands" rotate by 90
set hidden3d  

set grid front
set view 65,45 

splot "half_4mv_with_bkg.csv" u 1:2:((65536-$3)*0.001) with pm3d title ""

set output
