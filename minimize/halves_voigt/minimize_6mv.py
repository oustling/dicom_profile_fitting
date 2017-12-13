#!\usr\bin\python

from numpy import array, sqrt, real, convolve
from scipy.special import erf, wofz 
from scipy.optimize import minimize 
import math

def voigt( x, sigma, gamma, x_shift ):
    a = 1.0 / (sigma * sqrt(2*math.pi))
    return real( wofz((x-x_shift + (0.0+1.0j)*gamma)/sigma/sqrt(2))) * a  

def p( x, B, b, x_shift ):
    if((x-x_shift < -b) or (x-x_shift > b)):
        return  0
    return B

def h( x, B, x_shift ):
    if( x-x_shift < 0 ):
        return  0
    return B

line_array = [] ## global

def read_line (file_name ):
    with open( file_name ) as f:
        for line in f:
            line_array.append( [float( line.split()[0] ), float( line.split()[2] )] )



read_line("line_6mv.csv")


def pi(x, b):                          #  0        1      2,    3    4 
    # b is np.array of these parameters: [sigma_1, gamma, x_sh, bkg, B]
    Pi = []
    V = []
    PixV = []
    n_steps = 400*8 # 2481  *2
    step_size = 0.12405 # in mm 0.2481/2
    m = -0.5*(n_steps)*step_size # was n_steps-1
    for i in range( n_steps ):
        x_small_step = m + i*step_size # in mm from -49.62 mm to 49.62 mm
        Pi.append( h( x_small_step, b[3], b[2] ) )
        V.append( voigt(x_small_step, b[0], b[1], b[2]) )
    PixV = convolve( Pi, V, 'same' )

    return PixV[int((x/(2.0*step_size))*2) + int(0.5*n_steps)] + b[4]   # x in mm
                                                      # for 1250 was 283 mln
                                                      # for 1300 was 235 mln

def s(b):
    n_points_checked = 400
    halv = int( n_points_checked*0.5 )
    temp = 0.0
    for i in range(0, n_points_checked):
        x = (i-halv)*0.2481
        a = pi(x, b) - line_array[ 512 - halv +i ][1] 
        temp += a*a
    return temp


#          [sigma, gamma, x_sh , B  ,bkg    ]
x0 = array([0.52,   1.5, 0.0, 5050  ,2000   ]) # initial values for minimize



print ( x0 )
res = minimize(s, x0, method='nelder-mead', options={'xtol': 1e-2, 'disp': True, 'maxfev':1e4, 'maxiter':1e4} )
#res = minimize(s, x0, method='Powell')
print (res.x)
print (res.fun * 1e-6)

# print out the whole line
for i in range( 1024 ):
    x = (i-512)*0.2481 # x in milimiters
    print(x,", ", line_array[i][1],", ",pi(x,res.x) )
#    print(x,", ", line_array[i][1],", ",pi(x,x0) )

