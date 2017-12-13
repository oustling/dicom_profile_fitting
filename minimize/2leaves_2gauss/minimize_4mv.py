#!\usr\bin\python

from numpy import array
from scipy.special import erf 
from scipy.optimize import minimize 
from math import pi, sin, cos, exp, sqrt
#import dicom

line_array = [] ## global

def read_line (file_name ):
    with open( file_name ) as f:
        for line in f:
            line_array.append( [float( line.split()[0] ), float( line.split()[2] )] )



read_line("line_2leaves_4mv.csv")

line_len_2 = int(len(line_array)*0.5) ## global



def pi(x, b):                          #  0        1        2    3     4    5  6
    # b is np.array of these parameters: [sigma_1, sigma_2, w_1, x_sh, bkg, B, b]
    s_1 = 0.5*b[5]/(abs(b[2])*b[0]+abs(1-abs(b[2]))*b[1])
    s_2 = abs(b[2])*b[0]*erf( (b[6]-x-b[3])/(sqrt(2)*b[0]) )
    s_3 = abs(b[2])*b[0]*erf( (-b[6]-x-b[3])/(sqrt(2)*b[0]) )
    s_4 = abs(1-abs(b[2]))*b[1]*erf( (b[6]-x-b[3])/(sqrt(2)*b[1]) )
    s_5 = abs(1-abs(b[2]))*b[1]*erf( (-b[6]-x-b[3])/(sqrt(2)*b[1]) )
    return s_1*(s_2 - s_3 + s_4 - s_5) + b[4]     # x in mm

def s(b):
    n_points_checked = 380
    halv = int( n_points_checked*0.5 )
    temp = 0.0
    for i in range( n_points_checked ):
        x = (i-halv)*0.2481
        a = pi(x, b) - line_array[ line_len_2 - halv +i ][1] 
        temp += a*a
    return temp


#          [sigma_1, sigma_2, w_1,    x_sh,   bkg,     B,       b  ]
x0 = array([4.626,   1.212,   0.058, -5.35,  3047.0, 29484.0, 5.92]) # initial values for minimize


print ( x0 )
res = minimize(s, x0, method='nelder-mead', options={'xtol': 1e-2, 'disp': True, 'maxfev':1e5, 'maxiter':1e5} )
print (res.x)
print (res.fun * 1e-6)

# print out the whole line
for i in range(380):
    x = (i-190)*0.2481 # x in milimiters
    print(x,", ", line_array[line_len_2 - 190 + i][1],", ",pi(x,res.x) )
