import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

Data = np.loadtxt('L2_L10_magnet_Z_large_sweep_topgate_18_T_412mK_1.dat')
Time = Data[:,0]
Time = np.abs(Time + 9.990000000000e-02)
Amp = Data[:,5]
noise = np.random.normal(0,0.001,10000)


n=len(noise)
dt=2.5/1000000000000
nu=np.fft.fftfreq(n,dt)
fk=np.fft.fft(noise/n)

plt.plot(nu,fk.real,'r')
plt.show()
print(dt)
