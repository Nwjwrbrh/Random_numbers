import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt

maxrange=80
maxlim=5.0
x = np.linspace(-maxlim,maxlim,maxrange)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list
h = 2*maxlim/(maxrange-1)

randvar = np.loadtxt('4.1/T.dat',dtype='double')

for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
for i in range(0,maxrange-1):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test) #storing the pdf values in a list

def T_pdf(y):
    if(y<0):
        return 0.00
    if(0<=y<=1):
        return y
    if(1<y<=2):
        return 2-y
    if(y>2):
        return 0
      

vec_T_pdf = scipy.vectorize(T_pdf)

plt.plot(x[0:(maxrange-1)].T,pdf,'o')
plt.plot(x,vec_T_pdf(x))
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')
plt.legend(["Numerical","Theory"])
#plt.savefig("4.3/T_pdf.pdf")
plt.show()