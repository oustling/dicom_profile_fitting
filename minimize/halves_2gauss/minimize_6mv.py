#!\usr\bin\python

from numpy import array
from scipy.special import erf, erfc 
from scipy.optimize import minimize 
from math import pi, sin, cos, exp, sqrt

line_array = [] ## global

def read_line (file_name ):
    with open( file_name ) as f:
        for line in f:
            line_array.append( [float( line.split()[0] ), float( line.split()[2] )] )

read_line("line_6mv.csv")

def pi(x, b): 
    s_1 = 0.5*b[5]/(abs(b[2])*b[0]+abs(1-abs(b[2]))*b[1])
    s_2 = abs(b[2])*b[0]*erfc( (-x-b[3])/(sqrt(2)*b[0]) )
    s_4 = abs(1-abs(b[2]))*b[1]*erfc( (-x-b[3])/(sqrt(2)*b[1]) )
    return s_1*(s_2 + s_4 ) + b[4]     # x in mm

def s(b):
    n_points_checked = 400
    halv = int( n_points_checked*0.5 )
    temp = 0.0
    for i in range(0, n_points_checked):
        x = (i-halv)*0.2481
        a = pi(x, b) - line_array[ 512 - halv +i ][1] 
        temp += a*a
    return temp

#          [sigma_1, sigma_2, w_1, x_sh, bkg,     B,      ]
x0 = array([22.0,     1.03,   0.05, 0.02,  20986.0, 22907.0 ]) # initial values for minimize


print ( x0 )
res = minimize(s, x0, method='nelder-mead', options={'xtol': 1e-2, 'disp': True, 'maxfev':1e4, 'maxiter':1e4} )
print (res.x)
print (res.fun * 1e-6)

# print out the whole line
for i in range( 1024 ):
    x = (i-512)*0.2481 # x in milimiters
    print(x,", ", line_array[i][1],", ",pi(x,res.x) )

