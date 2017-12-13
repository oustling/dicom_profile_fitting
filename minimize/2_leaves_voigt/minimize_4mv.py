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

read_line("line_2leaves_4mv.csv")

line_len_2 = int(len(line_array)*0.5) ## global

def voigt( x, sigma, gamma, x_shift ):
    a = 1.0 / (sigma * sqrt(2*math.pi))
    return real( wofz((x-x_shift + 1.0j*gamma)/sigma/sqrt(2))) * a  

def p( x, B, b, x_shift ):
    if((x-x_shift < -b) or (x-x_shift > b)):
        return  0
    return B

def pi(x, b):                          #  0        1      2,    3    4  5
    # b is np.array of these parameters: [sigma_1, gamma, x_sh, bkg, B, b]
    Pi = []
    V = []
    PixV = []
    n_steps =  761 # 2481  *2 # 1601 # 2481 * 2 for zeus
    step_size = 0.12405 # in mm 0.2481/2
    m = -0.5*(n_steps-1)*step_size
    for i in range( n_steps ):
        x_small_step = m + i*step_size # in mm from -49.62 mm to 49.62 mm
        Pi.append( p(x_small_step,b[3], b[4], b[2] ) )
                                                        # 10.0 for 617 in 2
                                                        # 10.8 for 34.739 in 3
                                                        # 10.7 for 48.149 in 3
                                                        # 10.9 for 47.26 in 5
                                                        # 10.85 for 34.91 in 6
                                                        # 10.82 for 34.739 in 7
                                                        # 10.85 for ?? in ??
        V.append( voigt(x_small_step, b[0], b[1], b[2]) )
    PixV = convolve( Pi, V, 'same' )

    return PixV[int((x/(2.0*step_size))*2) + int(0.5*n_steps)] + b[5]   # x in mm
                                                        # 2331 for 34.739 in 7
                                                        # 2400 for 36.114 in 8
                                                        # 2500 for 40.89  in 8
                                                        # 2300 for 34.635  in 9
                                                        # 2250 for 35.14  in 10
                                                        # 2310 for 34.634  in 11
                                                        # 2413 for ??  in ??

def s(b):
    n_points_checked = 380
    halv = int( n_points_checked*0.5 )
    temp = 0.0
    for i in range( n_points_checked ):
        x = (i-halv)*0.2481 # x in milimiters from -8.6835 mm to 8.6835 mm
        a = pi(x, b) - line_array[ line_len_2 - halv +i ][1] 
        temp += a*a
    return temp

#          [sigma, gamma, x_sh,   B,   , b,    bkg]
x0 = array([0.3938,   0.99, 0.123, 4270, 10.82, 2310]) # initial values for minimize


print ( x0 )
res = minimize(s, x0, method='nelder-mead', options={'xtol': 1e-2, 'disp': True, 'maxfev':1e4, 'maxiter':1e4} )
print (res.x)
print (res.fun * 1e-6)

# print out the whole line
for i in range(380):
    x = (i-190)*0.2481 # x in milimiters
    print(x,", ", line_array[line_len_2 - 190 + i][1],", ",pi(x,res.x) )

