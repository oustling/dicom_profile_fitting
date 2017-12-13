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
        line.append( [i - line_length*0.5 , image.pixel_array[i][int(line_length*0.5)+offset_y] ] ) # diagonal

    return line

line1 = get_line( "half_beam_6mv.dcm", 0, 0, False ) ## global line
line2 = get_line( "half_beam_6mv.dcm", 100, 100, False ) ## global line
line3 = get_line( "half_beam_6mv.dcm", -100, -100, False ) ## global line
line4 = get_line( "half_beam_6mv.dcm", 200, 200, False ) ## global line
line5 = get_line( "half_beam_6mv.dcm", -200, -200, False ) ## global line

for i in range( len(line1) ):
    print( line1[i][0],", ",0.2*line1[i][1]+0.2*line2[i][1]+0.2*line3[i][1]+0.2*line4[i][1]+0.2*line5[i][1] ) # mean of five
#    print( line1[i][0],", ",line1[i][1],", ", line2[i][1],", ", line3[i][1],", ", line4[i][1],", ", line5[i][1] )# all lines


