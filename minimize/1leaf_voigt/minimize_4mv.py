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

read_line("line_1leaf_4mv.csv")

line_len_2 = int(len(line_array)*0.5) ## global

def voigt( x, sigma, gamma, x_shift ):
    a = 1.0 / (sigma * sqrt(2*math.pi))
    return real( wofz((x-x_shift + 1.0j*gamma)/sigma/sqrt(2))) * a  

def p( x, B, b, x_shift ):
    if((x-x_shift < -b) or (x-x_shift > b)):
        return  0
    return B

def pi(x, b):                          #  0        1      2,    3
    # b is np.array of these parameters: [sigma_1, gamma, x_sh, B]
    Pi = []
    V = []
    PixV = []
    n_steps = 761 # 380*4 
    step_size = 0.12405 # in mm 0.2481/2
    m = -0.5*(n_steps-1)*step_size
    for i in range( n_steps ):
        x_small_step = m + i*step_size # in mm from -49.62 mm to 49.62 mm
        Pi.append( p(x_small_step,b[3], b[4] ,b[2] ) )#was 5.829 for 27.48 in 1 b[4]=b
                                                       #was 5.820 for 27.43 in 3
                                                       #was 5.800 for 27.43 in 4
                                                       #was 5.780 for 27.43 in 5
                                                       #was 5.740 for 27.436 in 6
                                                       #was 5.700 for 45.179 in 7
        V.append( voigt(x_small_step, b[0], b[1], b[2]) )
    PixV = convolve( Pi, V, 'same' )

    return PixV[int((x/(2.0*step_size))*2) + int(0.5*n_steps)] + b[5] #was 2310 in min_4mv_1for 27.48
                                                                        # 2300 for 30M in 2
                                                                        # 2340 for 29.376 in 8
                                                                        # 2320 for 27.859 in 9
                                                                        # 2250 for 25.78 in 10
                                                                        # 2200 for 25.54 in 11
                                                                        # 2170 for 25.89 in 12
                                                                        # 2100 for 28.19 in 12
                                                                        # 2210 for 25.50 in 12
def s(b):
    n_points_checked = 380
    halv = int( n_points_checked*0.5 )
    temp = 0.0
    for i in range( n_points_checked ):
        x = (i-halv)*0.2481 # x in milimiters from -8.6835 mm to 8.6835 mm
        a = pi(x, b) - line_array[ line_len_2 - halv +i ][1] 
        temp += a*a
    return temp

#          [sigma, gamma, x_sh,      B ,   b, bkg ]
x0 = array([0.69,   0.93, 2.672,    4189.8, 5.85,  2228]) # initial values for minimize


print ( x0 )
res = minimize(s, x0, method='nelder-mead', options={'xtol': 1e-2, 'disp': True, 'maxfev':1e4, 'maxiter':1e4} )
print (res.x)
print (res.fun * 1e-6)

# print out the whole line
for i in range(380):
    x = (i-190)*0.2481 # x in milimiters
    print(x,", ", line_array[line_len_2 - 190 + i][1],", ",pi(x,res.x) )

