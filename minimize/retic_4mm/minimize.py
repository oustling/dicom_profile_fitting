#!\usr\bin\python
'''
This script loads a line from file and then tries to fit 4mm figure blurred with
sum of two gaussians, guessing gaussians parameters.
The best fit is printed out.
Use it from some shell as follows: python3.x > minimized_function.csv
'''

from numpy import array
from scipy.special import erf 
from scipy.optimize import minimize 
from math import pi, sin, cos, exp, sqrt
import dicom

line_array = [] ## global

def read_line (file_name ):
    with open( file_name ) as f:
        for line in f:
            line_array.append( [float( line.split()[0] ), float( line.split()[2] )] )



read_line("4mv_line.csv")

line_len_2 = int(len(line_array)*0.5) ## global

def pi(x, b):                           #  0        1        2    3     4    5 
    # b is np.array of these parameters: [sigma_1, sigma_2, w_1, x_sh, bkg, B]
    s_1 = 0.5*b[5]/(abs(b[2])*b[0]+abs(1-abs(b[2]))*b[1])
    s_2 = abs(b[2])*b[0]*erf( (2-x-b[3])/(sqrt(2)*b[0]) )
    s_3 = abs(b[2])*b[0]*erf( (-2-x-b[3])/(sqrt(2)*b[0]) )
    s_4 = abs(1-abs(b[2]))*b[1]*erf( (2-x-b[3])/(sqrt(2)*b[1]) )
    s_5 = abs(1-abs(b[2]))*b[1]*erf( (-2-x-b[3])/(sqrt(2)*b[1]) )
    return s_1*(s_2 - s_3 + s_4 - s_5) + b[4]     # x in mm

def s(b):
    n_points_checked = 190
    halv = int( n_points_checked*0.5 )
    temp = 0.0
    for i in range( n_points_checked ):
        x = ( i-halv )*0.2481 # x in milimiters
        a = pi(x, b) - line_array[ line_len_2 - halv + i ][1]
        temp += a*a
    return temp



#          [sigma_1, sigma_2, w_1, x_sh, bkg,     B]
x0 = array([2.2,     0.6,     0.1, 0.0,  1000.0, 14000.0]) #initial values


print ( x0 )
res = minimize(s, x0, method='nelder-mead', options={'xtol': 1e-2, 'disp': True, 'maxfev':1e4, 'maxiter':1e4} )
print (res.x)

for i in range(190):
    x = (i-95)*0.2481 # x in milimiters
    print(x,", ", line_array[ line_len_2 - 95 + i ][1],", ",pi(x,res.x) )

