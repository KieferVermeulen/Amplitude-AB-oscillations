import numpy as np

Data = np.loadtxt('L2_L10_magnet_Z_large_sweep_topgate_18_T_412mK_1.dat')
Time = Data[:,0]
Time = np.abs(Time + 9.990000000000e-02)
Amp = Data[:,5]
