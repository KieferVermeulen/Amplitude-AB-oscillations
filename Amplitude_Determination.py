








import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

noise = np.random.normal(0,0.001,10000)


n=len(noise)
dt=2.5/1000000000000
nu=np.fft.fftfreq(n,dt)
fk=np.fft.fft(noise/n)

plt.plot(nu,fk.real,'r')
plt.show()
print(dt)
