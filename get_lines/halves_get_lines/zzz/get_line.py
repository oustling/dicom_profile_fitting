#!\usr\bin\python

import dicom


def get_line( file_name, offset_x, offset_y, diagonal ):
    image = dicom.read_file( file_name )

    line = []
    line_length = 1024 # remember this should be even value

    array_size = image.pixel_array.shape[0]

    start_y = array_size*0.5 - line_length*0.5 + offset_y

    # now about to extract a line and shift it 
    # each point is one pixel; one pixel is 0.2481 mm;
    for i in range( line_length ) :
        line.append( [i - line_length*0.5 , image.pixel_array[int(line_length*0.5)][int(start_y)+i] ] ) # diagonal

    return line

line = get_line( "4.dcm", 0, 0, False ) ## global line

for i in range( len(line) ):
    print( line[i][0],", ",line[i][1] )
