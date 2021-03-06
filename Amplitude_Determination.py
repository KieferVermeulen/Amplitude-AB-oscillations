import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pylab as plb
from scipy.optimize import curve_fit
from scipy import asarray as ar,exp
import scipy.signal
Data = np.loadtxt('L2_L10_magnet_Z_large_sweep_topgate_18_T_412mK_1.dat')
Time = Data[:,0]
Time = np.abs(Time + 9.990000000000e-02)
Amp = Data[:,5]*12000
print(Amp)

n=len(Time)
Amp = scipy.signal.savgol_filter(Amp,125, 2, deriv=0, delta=1.0, axis=-1, mode='interp', cval=0.0)-Amp
Amp = np.pad(Amp, 5000, 'constant')
Time = np.pad(Time,5000,'linear_ramp')
plt.plot(Time,Amp)
n=len(Time)
plt.show()
dt=1/150
nu=np.fft.fftfreq(n,dt)
fk=np.fft.fft(Amp)/n

plt.plot(nu,fk.real,'r')
plt.plot(nu,fk.imag,'r')
plt.show()
n = len(nu)                          #the number of data
# mean = sum(nu*fk)/n                   #note this correction
# sigma = sum(fk*(nu-mean)**2)/n        #note this correction
#
# def gaus(x,a,x0,sigma):
#     return a*exp(-(nu-x0)**2/(2*sigma**2))
#
# popt,pcov = curve_fit(gaus,nu,fk,p0=[1,mean,sigma])
#
# plt.plot(nu,fk,'b+:',label='data')
# plt.plot(nu,gaus(nu,*popt),'ro:',label='fit')
# plt.legend()
# plt.title('Fig. 3 - Fit for Time Constant')
# plt.xlabel('Time (s)')
# plt.ylabel('Voltage (V)')
# plt.show()
