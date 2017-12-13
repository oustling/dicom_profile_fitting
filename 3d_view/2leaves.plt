#!/usr/bin/gnuplot

# This script generates output file from input defined in .csv file
# edit file_names in here and run the script with : gnuplot csv2png

set term pngcairo enhanced size 1300,500
set output "2leaves.png"
set datafile separator ","
set xrange [-290:100]
set yrange [-100:100]
set zrange [-5:60]
set xtics 40
set ytics 40
set ticslevel 0
set grid
set border 4095
set grid mxtics mytics mztics
set xlabel "x [px]"
set ylabel "y [px]"
set zlabel "Pixel value in thousands" rotate by 90
set hidden3d 
 
set size 1.0, 1.0
set origin 0.0, 0.0
set multiplot

set size 0.5, 1.0
set origin 0.0, 0.0

set grid front
set view 65,320 

set title "(a)"
splot "2.csv" u 1:2:($3*0.001) with pm3d title ""

set size 0.5, 1.0
set origin 0.5, 0.0

set title "(b)"
splot "4mv_leaves_bkg_substracted_simple.csv" u 1:2:($3*0.001) with pm3d title ""

unset multiplot
set output
