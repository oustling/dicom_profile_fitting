#!/usr/bin/gnuplot

set term pngcairo enhanced size 1300,400
set output "testD2.png"
set size 1.0, 1.0
set origin 0.0, 0.0
set multiplot
set datafile separator ","
set xrange [-20:20]
set yrange [-20:20]
set zrange [0:16] #25:42
set xtics 10
set ytics 10
set ticslevel 0
set grid
set grid mxtics mytics
set xlabel "x [px]"
set ylabel "y [px]"
set zlabel "Wartość piksela w tysiącach" rotate by 90
set pm3d hidden3d  

set grid front
set view 55,45 

set size 0.33, 1.0
set origin 0.0, 0.0
set label 1 "(x=2; y=-5; z=14.3)" at 2.0, -5.0 ,17  front
set title "(a) 4 MV"
unset colorbox
splot "4_bkg_substracted2.csv" u 1:2:($3*0.001) with pm3d title "",\
      '-' u 1:2:3 with points lc "red" lt 7 title ""
2.0, -5.0, 14.3
e

set origin 0.33, 0.0
set size 0.33, 1.0
unset label 1
set label 2 "(x=1; y=-5; z=14.9)" at 1.0, -5.0 ,17  front
unset colorbox
set title "(b) 6 MV"
splot "6_bkg_substracted2.csv" u 1:2:($3*0.001) with pm3d title "",\
      '-' u 1:2:3 with points lc "red" lt 7 title ""
1.0, -5.0, 15.19
e

set origin 0.66, 0.0
set size 0.33, 1.0
unset label 2
set label 3 "(x=2; y=-4 z=14.6)" at 2.0, -4.0 ,17  front
unset colorbox
set title "(c) 15 MV"
splot "15_bkg_substracted2.csv" u 1:2:($3*0.001) with pm3d title "",\
      '-' u 1:2:3 with points lc "red" lt 7 title ""
2.0, -4.0, 14.6
e

unset multiplot
set output
