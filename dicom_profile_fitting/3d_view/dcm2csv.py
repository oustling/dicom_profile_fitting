#!\usr\bin\python

'''
This script extracts image from .dcm format and saves it
into .csv file ready to plot with gnuplot with pm3d
run it with the following command: python3.x dcm2csv.py > output_file.csv
'''

import dicom

image = dicom.read_file("1leaf_4mv_simple.dcm")

line = []
line_length = 1024 # this should be even value

array_size = image.pixel_array.shape[0]
start_x = array_size*0.5 - line_length*0.5
start_y = array_size*0.5 - line_length*0.5
for i in range(0,line_length) :
    for j in range(0,line_length) :
        print( i-line_length*0.5,", ", j-line_length*0.5, ", ", image.pixel_array[start_x+i][start_y+j] )
    print("") # empty line needed by splot with pm3d
