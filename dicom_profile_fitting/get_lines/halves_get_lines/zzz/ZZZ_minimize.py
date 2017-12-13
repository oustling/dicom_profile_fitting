#!\usr\bin\python

from numpy import array
from scipy.special import erf 
from scipy.optimize import minimize 
from math import pi, sin, cos, exp, sqrt
import dicom

line_array = [] ## global

def read_line (file_name ):
    with open( file_name ) as f:
        for line in f:
            line_array.append( [float( line.split()[0] ), float( line.split()[1] )] )

'''
def get_line( file_name, offset_x, offset_y, diagonal ):
    image = dicom.read_file( file_name )

    #get a 80 of middle diagonal points including offset and print them
    line = []
    line_length = 80 # remember this should be even value

    array_size = image.pixel_array.shape[0]
    if( diagonal ):
        start_x = array_size*0.5 - line_length*0.5 + offset_x # diagonal
    else:
        start_x = -( array_size*0.5 - line_length*0.5 ) + offset_x # anti - diagonal


    start_y = array_size*0.5 - line_length*0.5 + offset_y

    # now about to extract diagonal line and shift it 
    # each point is one pixel; one pixel is 0.2481 mm;
    for i in range(0,line_length) :
        if( diagonal ):
            line.append( [i - line_length*0.5 , image.pixel_array[int(start_x)+i][int(start_y)+i] ] ) # diagonal
        else:
            line.append( [-(i - line_length*0.5) , image.pixel_array[int(start_x)-i][int(start_y)+i] ] ) # anti - diagonal

    return line

line = get_line( "s1_15mv.dcm", 1, -5, False ) ## global line
'''

line = read_line("4mv_leaves.csv")
print( line )

def pi(x, b):                          #  0        1        2    3     4    5  6
    # b is np.array of these parameters: [sigma_1, sigma_2, w_1, x_sh, bkg, B, b]
    # for 1 Gauss only w_2 is equal zero. w_1 = 1,
    s_1 = 0.5*b[5]/( b[0] )
    s_2 = b[0]*erf( (b[6]-x-b[3])/(sqrt(2)*b[0]) )
    s_3 = b[0]*erf( (-b[6]-x-b[3])/(sqrt(2)*b[0]) )
    return s_1*(s_2 - s_3) + b[4]     # x in mm

def s(b):
    n_points_checked = 60
    halv = int( n_points_checked*0.5 )
    temp = 0.0
    for i in range(0, n_points_checked):
        x = (i-halv)*0.2481
        a = pi(x, b) - line[ 40 - halv +i ][1] 
        temp += a*a
    return temp

'''
#          [sigma_1, sigma_2, w_1, x_sh, bkg,     B,       b  ]
x0 = array([2.2,     0.2,     0.5, 0.0,  26000.0, 14000.0, 2.0]) # initial values for minimize


print ( x0 )
res = minimize(s, x0, method='nelder-mead', options={'xtol': 1e-2, 'disp': True, 'maxfev':1e4, 'maxiter':1e4} )
print (res.x)

# print out the whole line
for i in range(80):
    x = (i-40)*0.2481 # x in milimiters
    print(x,", ", line[i][1],", ",pi(x,res.x) )
'''
