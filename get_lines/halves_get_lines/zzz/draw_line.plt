#!/usr/bin/gnuplot

# two diagonal profiles for 4,6,15 MV
# x-shifted to have maximum in x=0

set term pngcairo enhanced size 1300,400
#set term postscript eps enhanced color
# set output '|ps2pdf - bkg.pdf'
set output "halves.png"
set size 1.0, 1.0
set origin 0.0, 0.0
set multiplot
set datafile separator ","
set xrange [-300:300]
set yrange [24:67]
#set arrow from -2,24 to -2,42 nohead dashtype 2 linecolor "red" linewidth 1.5
#set arrow from  2,24 to  2,42 nohead dashtype 2 linecolor "red" linewidth 1.5

#set yrange [-20:20]
set xtics 100
#set ytics 10
#set ticslevel 0
#set mxtics 2
#set mytics 2
set grid
#set grid mxtics mytics
set xlabel "x [px]"
set ylabel "Wartość piksela w tysiącach" rotate by 90
#set pm3d hidden3d  

set origin 0.0, 0.0
set size 0.33, 1
set title "polwiazka 1"

plot "1.csv" u 1:($2*0.001) with lines title ""

set origin 0.33, 0.0
set size 0.33, 1
set title "-3 do 3"

plot "3.csv" u 1:($2*0.001) with lines title ""

set origin 0.66, 0.0
set size 0.33, 1
set title "polwiazka 4"

plot "4.csv" u 1:($2*0.001) with lines title ""





unset multiplot

set output
