# dicom_profile_fitting
Tools for viewing and manipulating dicom images acquired by Elekta iViewGT system.

There are following scripts:

• 3d_view - converts the contents of a dicom file to a .csv text file, then generates from that .csv file graphic .png file

• bkg_subtracting - subtracts two dicom images from each other then adds some value, so the result is positive (size of both files must be 1024 times 1024 pixels),

• get_lines - saves the pixel lines extracted from the dicom file as a .csv text file,

• minimize - matches some theoretical curves to the points stored in a file containing a line of pixels (line extracted by get_lines)
