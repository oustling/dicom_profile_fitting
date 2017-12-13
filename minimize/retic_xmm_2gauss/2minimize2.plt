#!/usr/bin/gnuplot

set term pngcairo enhanced size 1300,400
set output "2min_retic_xmm_2gauss_3.png"
set size 1.0, 1.0
set origin 0.0, 0.0
set multiplot
set datafile separator ","
set xrange [-8:8]
set yrange [0:16]
set arrow from -2,0 to -2,15 nohead dashtype 2 linecolor "red" linewidth 1.5
set arrow from  2,0 to  2,15 nohead dashtype 2 linecolor "red" linewidth 1.5

set xtics 2
set grid
set xlabel "x [mm]"
set ylabel "Pixel value in thousands" rotate by 90

set origin 0.0, 0.0
set size 0.33, 1.0
set title "(a) 4 MV S = 0.74 millions"

plot "2_min1_4mv.csv" u 1:($2*0.001) with lines title "",\
     "2_min1_4mv.csv" u 1:($3*0.001) with lines title ""

set origin 0.33, 0.0
set size 0.33, 1.0
set title "(b) 6 MV S = 0.60 millions"

plot "2_min1_6mv.csv" u 1:($2*0.001) with lines title "",\
     "2_min1_6mv.csv" u 1:($3*0.001) with lines title ""

set origin 0.66, 0.0
set size 0.33, 1.0
set title "(c) 15 MV S = 0.53 millions"

plot "2_min1_15mv.csv" u 1:($2*0.001) with lines title "",\
     "2_min1_15mv.csv" u 1:($3*0.001) with lines title ""

unset multiplot
set output
