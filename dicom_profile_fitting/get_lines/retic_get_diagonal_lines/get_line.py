#!\usr\bin\python
'''
Script extracts diagonal line of given length from .dcm file
To identify offsets, unfortunately, there is need to export .dcm to .csv first, using dcm2csv.py script,
and check csv 'manually' for the biggest pixel value 
First edit the file with desired line length and file names,
Then execute this script by typing in the concole : python3.x get_line.py > file_with_line.csv
'''

import dicom


def get_line( file_name, offset_x, offset_y, diagonal ):
    image = dicom.read_file( file_name )

    line = []
    line_length = 200 # remember this should be even value

    array_size = image.pixel_array.shape[0]

    if( diagonal ):
        start_x = array_size*0.5 - line_length*0.5 + offset_x # diagonal
    else:
        start_x = -( array_size*0.5 - line_length*0.5 ) + offset_x # anti - diagonal

    start_y = array_size*0.5 - line_length*0.5 + offset_y

    # now about to extract a line and shift it 
    # each point here is one pixel; one pixel is 0.2481 mm;
    for i in range( line_length ) :
        if( diagonal ):
            line.append( [i - line_length*0.5 , image.pixel_array[int(start_x)+i][int(start_y)+i] ] ) # diagonal
        else:
            line.append( [-(i - line_length*0.5) , image.pixel_array[int(start_x)-i][int(start_y)+i] ] ) # anti - diagonal

    return line


line1 = get_line( "15_bkg_substracted1.dcm", 1, -5, False ) ## global line
line2 = get_line( "15_bkg_substracted1.dcm", 1, -5, True ) ## global line
line3 = get_line( "15_bkg_substracted2.dcm", 2, -4, False ) ## global line
line4 = get_line( "15_bkg_substracted2.dcm", 2, -4, True ) ## global line

for i in range( len(line1) ):
    print( line1[i][0],", ",0.25*(line1[i][1] + line2[i][1] + line3[i][1] + line4[i][1]) )

