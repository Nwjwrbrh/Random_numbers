import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt

maxrange=50
x = np.linspace(-4,4,maxrange)
simlen = int(1e6)
err = []
randvar = np.loadtxt('1.1/uni.dat',dtype='double')

for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen)

def uni_cdf(x):
	if(x<=0):
		x=0
	elif(x>1):
		x=1
	return x
    
y = []
for i in range(len(x)):
	y.append(uni_cdf(x[i]))
plt.plot(x,err,'o')
plt.plot(x,y)
plt.grid()
plt.xlabel('$x_i$')
plt.ylabel('$F_X(x_i)$')
plt.legend(["Numerical","Theory"])
#plt.savefig("1.2/uni_cdf.pdf")
plt.show()