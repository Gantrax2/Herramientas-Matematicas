
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def ordenlib(lista,rever=False):

	d=list(zip(*lista))  #Z, X, Y
	d.sort(reverse=rever)#)#
	return zip(*d)	

def norm(v):
	suma=0
	for i in v:
		suma+=i**2
	suma=(suma)**(1/2)
	return suma

xteo=np.linspace(0,100,10000)
w=2*np.pi/3
print("f:",w/(2*np.pi))
yteo=1*np.cos(xteo*w)+(1/2)*np.cos(xteo*w*2)+(1/4)*np.cos(xteo*w*4)
#yteo=np.exp(-((xteo-20)**2)/(5**2))*np.cos(xteo*2*np.pi/3)



sp = abs(np.fft.fft(yteo)/max(np.fft.fft(yteo)))
freq = np.fft.fftfreq(len(yteo),xteo[1]-xteo[0])
fig, ax=plt.subplots(2)
ax[0].plot(xteo,yteo, '-ob', ms=3)
ax[1].plot(freq[:int(len(freq)/2)], sp.real[:int(len(freq)/2)], '-or', ms=2)
plt.show()

