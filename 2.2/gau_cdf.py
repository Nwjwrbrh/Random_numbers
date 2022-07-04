import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-4,4,30)
simlen=int(1e6)
err=[]
randvar=np.loadtxt('1.1/gau.dat',dtype='double')

for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen)
 
plt.plot(x,err,'o')
plt.plot(x,err)#plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["points","line"])
plt.savefig('2.2/gau_cdf.pdf') #to save graph as pdf
plt.show()