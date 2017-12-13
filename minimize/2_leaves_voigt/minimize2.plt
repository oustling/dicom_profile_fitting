#!/usr/bin/gnuplot

set term pngcairo enhanced size 1600,600
set output "min_2leaves_voigt.png"
set size 1.0, 1.0
set origin 0.0, 0.0
set multiplot
set datafile separator ","
set xrange [-45:45]
set yrange [0:35]
set arrow from  -10,0 to  -10,35 nohead dashtype 2 linecolor "red" linewidth 1.5
set arrow from  10,0 to  10,35 nohead dashtype 2 linecolor "red" linewidth 1.5

set xtics 5
set grid
set xlabel "x [mm]"
set ylabel "Pixel value in thousands" rotate by 90

set origin 0.0, 0.0
set size 0.33, 1.0
set title "(a) 4 MV; S = 34.64 (24.4) millions"

plot "min_4mv_11.csv" u 1:($2*0.001) with lines title "",\
     "min_4mv_11.csv" u 1:($3*0.001) with lines title ""

set origin 0.33, 0.0
set size 0.33, 1.0
set title "(b) 6 MV; S = 37.99 (16.54) millions"

plot "min_6mv_1.csv" u 1:($2*0.001) with lines title "",\
     "min_6mv_1.csv" u 1:($3*0.001) with lines title ""

set origin 0.66, 0.0
set size 0.33, 1.0
set title "(c) 15 MV; S = 38.28 (35.18) millions"

plot "min_15mv_3.csv" u 1:($2*0.001) with lines title "",\
     "min_15mv_3.csv" u 1:($3*0.001) with lines title ""

unset multiplot
set output
