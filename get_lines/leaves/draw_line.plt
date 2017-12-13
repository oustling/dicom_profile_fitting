#!/usr/bin/gnuplot

# two diagonal profiles for 4,6,15 MV
# x-shifted to have maximum in x=0

set term pngcairo enhanced size 800,600
#set term postscript eps enhanced color
# set output '|ps2pdf - bkg.pdf'
set output "2leaf_lines.png"
#set size 1.0, 1.0
#set origin 0.0, 0.0
#set multiplot
set datafile separator ","
set xrange [-80.6:80.6]
set yrange [0:40]

#set yrange [-20:20]
set xtics 40.3
#set ytics 10
#set ticslevel 0
#set mxtics 2
#set mytics 2
set grid
#set grid mxtics mytics
set xlabel "x [cm]"
#set ylabel "Wartość piksela w tysiącach" rotate by 90
#set pm3d hidden3d  

#set origin 0.0, 0.0
#set size 0.33, 1
#set title "4"

plot "all_lines_2leaves_4mv.csv" u ($1):($2*0.001) with lines title "",\
     "all_lines_2leaves_4mv.csv" u ($1):($3*0.001) with lines title "",\
     "all_lines_2leaves_4mv.csv" u ($1):($4*0.001) with lines title "",\
     "all_lines_2leaves_4mv.csv" u ($1):($5*0.001) with lines title "",\
     "all_lines_2leaves_4mv.csv" u ($1):($6*0.001) with lines title ""

#set origin 0.33, 0.0
#set size 0.33, 1
#set title "6"

#plot "all_lines.csv" u 1:($3*0.001) with lines title ""

#set origin 0.66, 0.0
#set size 0.33, 1
#set title "15"

#plot "all_lines.csv" u 1:($4*0.001) with lines title ""


#unset multiplot

set output
