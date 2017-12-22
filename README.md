# dicom_profile_fitting
Tools for viewing and manipulating dicom images acquired by Elekta iViewGT system.

Altogether it is a scripts chain that allows one to check if structure imaged by iViewGT has Gaussian or Voigt profile shape. 

Separately each part can be used to achieve some dicom file manipulation.

There are four following scripts:

• 3d_view - python file converts the contents of a .dicom file to a .csv text file (ready to use with gnuplot pm3d), gnuplot file generates from .csv file graphic file (.png one),

• bkg_subtracting - subtracts two dicom images from each other then adds some value, so the result is positive (size of both files must be 1024 times 1024 pixels), it can be used to eliminate background or some artifacts,

• get_lines - saves the pixel lines extracted from the dicom file as a .csv text file,

• minimize - matches some theoretical curves to the points stored in a file containing a line of pixels (line extracted by get_lines)
