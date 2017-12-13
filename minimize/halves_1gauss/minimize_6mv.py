#!\usr\bin\python

from numpy import array
from scipy.special import erf , erfc
from scipy.optimize import minimize 
from math import pi, sin, cos, exp, sqrt

line_array = [] ## global

def read_line (file_name ):
    with open( file_name ) as f:
        for line in f:
            line_array.append( [float( line.split()[0] ), float( line.split()[2] )] )



read_line("line_6mv.csv")

def pi(x, b):                          #  0        1     2    3
    # b is np.array of these parameters: [sigma_1, x_sh, bkg, A]
    s_1 = 0.5*b[3]
    s_2 = erfc( (-x-b[1])/(sqrt(2)*b[0]) )
    return s_1*s_2 + b[2]     # x in mm

def s(b):
    n_points_checked = 400
    halv = int( n_points_checked*0.5 )
    temp = 0.0
    for i in range( n_points_checked ):
        x = (i-halv)*0.2481
        a = pi(x, b) - line_array[ 512 - halv +i ][1] 
        temp += a*a
    return temp


#          [sigma_1,  x_sh, bkg,     B  ]
x0 = array([0.73,     0.0,  1000.0, 14000.00]) # initial values for minimize


print ( x0 )
res = minimize(s, x0, method='nelder-mead', options={'xtol': 1e-2, 'disp': True, 'maxfev':1e5, 'maxiter':1e5} )
print (res.x)
print (res.fun * 1e-6)

# print out the whole line
for i in range( 1024 ):
    x = (i-512)*0.2481 # x in milimiters
    print(x,", ", line_array[i][1],", ",pi(x,res.x) )

