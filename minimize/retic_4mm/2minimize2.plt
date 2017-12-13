#!/usr/bin/gnuplot

set term pngcairo enhanced size 1600,600
set output "2min_retic_4mm.png"
set size 1.0, 1.0
set origin 0.0, 0.0
set multiplot
set datafile separator ","
set xrange [-8:8]
set yrange [0:16]
set arrow from -2,0 to -2,16 nohead dashtype 2 linecolor "red" linewidth 1.5
set arrow from  2,0 to  2,16 nohead dashtype 2 linecolor "red" linewidth 1.5

set xtics 2
set grid
set xlabel "x [mm]"
set ylabel "Pixel value in thousands" rotate by 90

set origin 0.0, 0.0
set size 0.33, 1.0
set title "(a) 4 MV S = 75.0 millions"

plot "2min_4mv.csv" u 1:($2*0.001) with lines title "",\
     "2min_4mv.csv" u 1:($3*0.001) with lines title ""

set origin 0.33, 0.0
set size 0.33, 1.0
set title "(b) 6 MV S = 87.9 millions"

plot "2min_6mv.csv" u 1:($2*0.001) with lines title "",\
     "2min_6mv.csv" u 1:($3*0.001) with lines title ""

set origin 0.66, 0.0
set size 0.33, 1.0
set title "(c) 15 MV S = 91.9 millions"

plot "2min_15mv.csv" u 1:($2*0.001) with lines title "",\
     "2min_15mv.csv" u 1:($3*0.001) with lines title ""

unset multiplot
set output
