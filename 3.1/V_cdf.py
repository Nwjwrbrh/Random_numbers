import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt

maxrange=50
maxlim=8.0
x=np.linspace(-maxlim,maxlim,maxrange)
x1=np.linspace(-maxlim,maxlim,maxrange*4)
simlen=int(1e6)
err=[]
randvar=np.loadtxt('3.1/V.dat',dtype='double')

for i in range (0,maxrange):
    err_ind=np.nonzero(randvar<x[i])
    err_n=np.size(err_ind)
    err.append(err_n/simlen)

def uni_cdf(x):
    if x<0:
        x=0 # The function is constant so it's value can be taken to be 0
    return 1-np.exp(-x/2)

vec_cdf = np.vectorize(uni_cdf)
plt.plot(x,err,'o')
plt.plot(x1,vec_cdf(x1))
plt.grid()
plt.xlabel('$x_i$')
plt.ylabel('$F_X(x_i)$')
plt.legend(["Numerical","Theory"])
#plt.savefig('3.1/V_cdf.pdf')
plt.show()