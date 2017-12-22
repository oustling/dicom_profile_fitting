#!/usr/bin/gnuplot

set term pngcairo enhanced size 1300,400
set output "min_1leaf_1gauss.png"
set size 1.0, 1.0
set origin 0.0, 0.0
set multiplot
set datafile separator ","
set xrange [-20:20]
set yrange [0:35]
set arrow from 0,0 to 0,35 nohead dashtype 2 linecolor "red" linewidth 1.5
set arrow from  10,0 to  10,35 nohead dashtype 2 linecolor "red" linewidth 1.5
set xtics 5
set grid
set xlabel "x [mm]"
set ylabel "Wartość piksela w tysiącach" rotate by 90

set origin 0.0, 0.0
set size 0.33, 1.0
set title "(a) 4 MV S = 96.4 mln"

plot "min_4mv_1.csv" u 1:($2*0.001) with lines title "",\
     "min_4mv_1.csv" u 1:($3*0.001) with lines title ""

set origin 0.33, 0.0
set size 0.33, 1.0
set title "(b) 6 MV S = 59.6 mln"

plot "min_6mv_1.csv" u 1:($2*0.001) with lines title "",\
     "min_6mv_1.csv" u 1:($3*0.001) with lines title ""

set origin 0.66, 0.0
set size 0.33, 1.0
set title "(c) 15 MV S = 41.8 mln"

plot "min_15mv_1.csv" u 1:($2*0.001) with lines title "",\
     "min_15mv_1.csv" u 1:($3*0.001) with lines title ""

unset multiplot

set output