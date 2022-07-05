from cmath import sqrt
import numpy as np
import matplotlib.pyplot as plt
import math
import mpmath
import scipy
def cdf(x):
    if(x<0):
        x=0
    if(0<=x<=1):
        x=x*x/2
    if(1<x<=2):
        x=1-((2-x)**2)/2
    if(x>2):
        x=1
    return x

x = np.linspace(-2,5,50)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
randvar = np.loadtxt('4.1/T.dat',dtype='double')
for i in range(0,50):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list
vec_gau_cdf = scipy.vectorize(cdf)
plt.plot(x.T,err,"o")
plt.plot(x.T,vec_gau_cdf(x))
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Numerical","Theory"])
#plt.savefig("4.2/T_cdf.pdf")
plt.show()