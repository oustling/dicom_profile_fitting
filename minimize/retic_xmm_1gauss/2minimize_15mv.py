#!\usr\bin\python

from numpy import array
from scipy.special import erf 
from scipy.optimize import minimize 
from math import pi, sin, cos, exp, sqrt

line_array = [] ## global

def read_line (file_name ):
    with open( file_name ) as f:
        for line in f:
            line_array.append( [float( line.split()[0] ), float( line.split()[2] )] )



read_line("15mv_line.csv")

line_len_2 = int(len(line_array)*0.5) ## global



def pi(x, b):                          #  0        1     2    3  4
    # b is np.array of these parameters: [sigma_1, x_sh, bkg, B, b]
    s_1 = 0.5*b[3]/( b[0] )
    s_2 = b[0]*erf( (b[4]-x-b[1])/(sqrt(2)*b[0]) )
    s_3 = b[0]*erf( (-b[4]-x-b[1])/(sqrt(2)*b[0]) )
    return s_1*(s_2 - s_3) + b[2]     # x in mm

def s(b):
    n_points_checked = 190
    halv = int( n_points_checked*0.5 )
    temp = 0.0
    for i in range( n_points_checked ):
        x = (i-halv)*0.2481
        a = pi(x, b) - line_array[ line_len_2 - halv + i ][1] 
        temp += a*a
    return temp


#          [sigma_1, x_sh, bkg,     B,       b  ]
x0 = array([0.62,    0.04, 1151.0,  13518.0, 1.45]) # initial values for minimize


print ( x0 )
res = minimize(s, x0, method='nelder-mead', options={'xtol': 1e-2, 'disp': True, 'maxfev':1e4, 'maxiter':1e4} )
print (res.x)
print (res.fun * 1e-6)


# print out the whole line
for i in range(190):
    x = (i-95)*0.2481 # x in milimiters
    print(x,", ", line_array[ line_len_2 - 95 + i ][1],", ",pi(x,res.x) )
