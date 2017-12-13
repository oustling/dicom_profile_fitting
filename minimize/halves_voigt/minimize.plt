#!/usr/bin/gnuplot

set term pngcairo enhanced size 1300,400
set output "min_halves_voigt.png"
set size 1.0, 1.0
set origin 0.0, 0.0
set multiplot
set datafile separator ","
set xrange [-40:40]
set yrange [0:45]

set xtics 10
set grid
set xlabel "x [mm]"
set ylabel "Pixel value in thousands" rotate by 90

set origin 0.0, 0.0
set size 0.33, 1
set title "(a) 4 MV S = 87.6 millions"

plot "min_4mv_5.csv" u 1:($2*0.001) with linespoints ps 0.2 title "",\
     "min_4mv_5.csv" u 1:($3*0.001) with linespoints ps 0.2 title ""

set origin 0.33, 0.0
set size 0.33, 1
set title "(b) 6 MV S = 55.0 millions"
unset ylabel

plot "min_6mv_6.csv" u 1:($2*0.001) with linespoints ps 0.2 title "",\
     "min_6mv_6.csv" u 1:($3*0.001) with linespoints ps 0.2 title ""

set origin 0.66, 0.0
set size 0.33, 1
set title "(c) 15 MV S = 82.0 millions"
unset ylabel

plot "min_15mv_6.csv" u 1:($2*0.001) with linespoints ps 0.2 title "",\
     "min_15mv_6.csv" u 1:($3*0.001) with linespoints ps 0.2 title ""





unset multiplot

set output
