#!/usr/bin/gnuplot

set term pngcairo enhanced size 1600,500
set output "min_1leaf_all.png"
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
set ylabel "Pixel value in thousands" rotate by 90

set origin 0.0, 0.0
set size 0.33, 1.0
set title "(a) 4 MV"

plot "v_min_4mv_13.csv" u 1:($2*0.001) with points linecolor "black" pointsize 0.5 pt 7 title "",\
     "1l_min_4mv_1.csv" u ($1):($3*0.001) with lines title "",\
     "2l_min_4mv_1.csv" u ($1):($3*0.001) with lines title "",\
     "v_min_4mv_13.csv" u ($1):($3*0.001) with lines linecolor "red" title ""

set origin 0.33, 0.0
set size 0.33, 1.0
set title "(b) 6 MV"
unset ylabel

plot "v_min_6mv_3.csv" u 1:($2*0.001) with points linecolor "black" pointsize 0.5 pt 7 title "",\
     "1l_min_6mv_1.csv" u ($1):($3*0.001) with lines title "",\
     "2l_min_6mv_1.csv" u ($1):($3*0.001) with lines title "",\
     "v_min_6mv_3.csv" u 1:($3*0.001) with lines linecolor "red"  title ""

set origin 0.66, 0.0
set size 0.33, 1.0
set title "(c) 15 MV"
unset ylabel
set key samplen 1
set key #at graph 1.5,screen 0.5 center center
plot "v_min_15mv_10.csv" u 1:($2*0.001) with points linecolor "black" pointsize 0.5 pt 7 title "EPID",\
     "1l_min_15mv_1.csv" u ($1):($3*0.001) with lines title "1-Gauss",\
     "2l_min_15mv_1.csv" u ($1):($3*0.001) with lines title "2-Gauss",\
     "v_min_15mv_10.csv" u 1:($3*0.001) with lines linecolor "red"  title "Voigt"

unset multiplot
set output
