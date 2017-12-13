#!\usr\bin\python

'''
This script substracts background image file from data file
then the new file is saved
'''

import dicom

image = dicom.read_file("6_leaves_15mv.dcm")
bkg   = dicom.read_file("bkg_15mv.dcm")

for i in range( 1024 ):
    for j in range( 1024 ):
#        image.pixel_array[i][j] = 65536 - image.pixel_array[i][j]
#        bkg.pixel_array[i][j] = 65536 - bkg.pixel_array[i][j]
        image.pixel_array[i][j] = image.pixel_array[i][j] - bkg.pixel_array[i][j] + 1000 
        # Sometimes  background value is greater then value in original file
        # substracting leads to value < 0 (that's not possible for .dcm)
        # therefore there is need to flat such cases to zero,
        # but better option is to shift everything by let's say 300 or 1000 up!
image.PixelData = image.pixel_array.tostring()
image.save_as("leaves_15mv_bkg_substracted_simple.dcm")
