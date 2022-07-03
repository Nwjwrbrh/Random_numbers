#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt

maxrange=50
maxlim=4.0
x = np.linspace(-maxlim,maxlim,maxrange)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('1.1/uni.dat',dtype='double')

for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen)

plt.plot(x,err,'o')
plt.plot(x,err)#plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$F_X(x_i)$')
plt.legend(["points","line"])
#plt.savefig("1.2/uni_cdf.pdf") #to save the fig
plt.show()