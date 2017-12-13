#!\usr\bin\python

from numpy import array, sqrt, real, convolve
from scipy.optimize import minimize 
from scipy.special import wofz 
import math

line_array = [] ## global

def read_line (file_name ):
    with open( file_name ) as f:
        for line in f:
            line_array.append( [float( line.split()[0] ), float( line.split()[2] )] )

read_line("15mv_line.csv")

line_len_2 = int(len(line_array)*0.5) ## global

def voigt( x, sigma, gamma, x_shift ):
    a = 1.0 / (abs(sigma) * sqrt(2*math.pi))
    return real( wofz((x-x_shift + (0.0+1.0j)*abs(gamma))/abs(sigma)/sqrt(2))) * a  

def p( x, B, b, x_shift ):
    if((x-x_shift < -b) or (x-x_shift > b)):
        return  0
    return B

def pi(x, b):                          #  0        1      2,    3    4  5
    # b is np.array of these parameters: [sigma_1, gamma, x_sh, bkg, B, b]
    Pi = []
    V = []
    PixV = []
    n_steps =  381 #401  #1601
    step_size = 0.12405 # in mm 0.2481/2
    m = -0.5*(n_steps-1)*step_size
    for i in range( n_steps ):
        x_small_step = m + i*step_size # in mm from -49.62 mm to 49.62 mm
        Pi.append( p(x_small_step,b[4],b[5],b[2] ) )
        V.append( voigt(x_small_step, b[0], b[1], b[2]) )
    PixV = convolve( Pi, V, 'same' )

    return PixV[int((x/(2.0*step_size))*2) + int(0.5*n_steps)] + b[3]   # x in mm

def s(b):
    n_points_checked = 190
    halv = int( n_points_checked*0.5 )
    temp = 0.0
    for i in range( n_points_checked ):
        x = (i-halv)*0.2481 # x in milimiters from -8.6835 mm to 8.6835 mm
        a = pi(x, b) - line_array[ line_len_2 - halv +i ][1] 
        temp += a*a
    return temp

#          [sigma, gamma, x_sh,  bkg,     B,      b  ]
x0 = array([0.407,   0.233, -0.00408,   1087.0, 1834.0, 1.44]) # initial values for minimize


print ( x0 )
res = minimize(s, x0, method='nelder-mead', options={'xtol': 1e-2, 'disp': True, 'maxfev':1e4, 'maxiter':1e4} )
print (res.x)
print (res.fun * 1e-6)

# print out the whole line
for i in range(190):
    x = (i-95)*0.2481 # x in milimiters
    print(x,", ", line_array[line_len_2 - 95 + i][1],", ",pi(x,res.x) )

