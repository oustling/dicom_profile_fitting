#!/usr/bin/gnuplot

# This script generates output file from input defined in .csv file
# edit file_names in here and run the script with : gnuplot csv2png

set term pngcairo enhanced size 800,600
set output "1_bkg_substracted.png"
set datafile separator ","
set xrange [-500:500]
set yrange [-500:500]
set zrange [0:60]
set xtics 100
set ytics 100
set ticslevel 0
set grid
set grid mxtics mytics
set xlabel "x [px]"
set ylabel "y [px]"
set zlabel "Pixel value in thousands" rotate by 90
set pm3d #hidden3d  

set grid front
set view 65,35 

splot "1_bkg_substracted.csv" u 1:2:($3*0.001) with pm3d title ""

set output
