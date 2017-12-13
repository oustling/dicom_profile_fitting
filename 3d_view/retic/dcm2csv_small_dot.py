#!\usr\bin\python

'''
This script extracts image from .dcm format and saves it
into .csv file ready to plot with gnuplot with pm3d
run it with the following command: python3.x dcm2csv.py > output_file.csv
'''

import dicom

image = dicom.read_file("15_bkg_substracted2.dcm")

line = []
line_length = 1024 # this should be even value
half_line = int(line_length*0.5)


array_size = image.pixel_array.shape[0]
start_x = array_size*0.5 - line_length*0.5
start_y = array_size*0.5 - line_length*0.5
for i in range(half_line - 60, half_line - 20 ) :
    for j in range(half_line - 20, half_line + 20 ) :
        print( i-line_length*0.5,", ", j-line_length*0.5, ", ", image.pixel_array[start_x+i][start_y+j] )
    print("") # empty line needed by splot with pm3d
