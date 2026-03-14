#La Fuerza de Lorentz = q(E+vxB)	con q(C)=escalar, {E(N/C);B(Ns/(Cm));v(m/s)}=vectores(R3) 

#qE es la contribución de cada cuerpo en fuerza electrica	
#q(vxB) la contribucion magnetica

#NOTA: se estan omitiendo algunas variables como phi constante dentro de sin y cos


from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from numpy.random import rand
from IPython import display

import time
from datetime import datetime

ahora = datetime.now()

L=15
H = 0
S= np.random.choice([-1, 1], size=[L,L])

def mcmove(S, beta):
	mem=np.zeros(9,dtype=float)
	mem[8]=np.exp(-8*beta)
	mem[4]=np.exp(-4*beta)
	mem[0]=1.
	
	for i in range(L):
		for j in range(L):
			a=np.random.randint(0,L)
			b=np.random.randint(0,L)
			s=S[a,b]
			nb=S[(a+1)%L,b]+S[a,(b+1)%L]+S[(a-1)%L,b]+S[a,(b-1)%L]
			cost=2*s*nb
			if cost<0:
				s*=-1
			elif rand() < mem[cost]:
				s*=-1
			S[a,b]=s
	return S

def calcEnergy(S):
	E=0

	for i in range(L):
		for j in range(L):
			s=S[i,j]
			nb=S[(i+1)%L,j]+S[i,(j+1)%L]+S[(i-1)%L,j]+S[i,(j-1)%L]
			E+= -nb*s
	return E/4

def calcM(S):
	M=np.sum(S)
	return M

kT0=0.1
kT1=5
#kT=2.269
#kT=20

step=240 #600  para una convergencia mas notable
stepKT=50 #250
jump=20
paso=np.arange(int(step/jump))*jump
ener=np.zeros(int(step/jump))
magn=np.zeros(int(step/jump))


# Definir una bandera de control
running = [True]  # lista mutable, truco para modificar dentro de función

# Esta función se llama al cerrar la ventana
def on_close(event):
    running[0] = False

kTL=[]
EL=[]
ML=[]
for n in range(stepKT):
	t0=time.time()
	print(n)
	kT=kT0+(kT1-kT0)*n/(stepKT-1)
	kTL.append(kT)

	#fig=plt.figure(figsize=(7,7))
	for k in range(step):
		S=mcmove(S,1./kT)


		if k%jump==0:
			ener[int(k/jump)]=calcEnergy(S)
			magn[int(k/jump)]=calcM(S)
			#plt.imshow(S)
			#plt.gcf().set_size_inches(7,7)
			#display.display(plt.gcf())
			#display.clear_output(wait=True)
			#plt.pause(0.01)


	EL.append(np.mean(ener[int(step/jump/2):])/L**2)
	ML.append(np.mean(magn[int(step/jump/2):])/L**2)

	t1=time.time()
	print('Tiempo restante...',(t1-t0)*(stepKT-2-n))

fig=plt.figure(figsize=(7,7))
plt.title("Energia. kT en (%.2f - %.2f), J=1 "%(kT0,kT1))
plt.plot(kTL,EL)
plt.xlabel('Paso', fontsize=16)
plt.ylabel('E', fontsize=16)
plt.savefig("barrido_E_vs_kT_%s"%ahora.strftime("%Y_%m_%d_%H_%M_%S"))
plt.show()


fig=plt.figure(figsize=(7,7))
plt.title("Magnet. kT en (%.2f - %.2f), J=1"%(kT0,kT1))
plt.plot(kTL,ML)
plt.xlabel('Paso', fontsize=16)
plt.ylabel('M', fontsize=16)
plt.savefig("barrido_M_vs_kT_%s"%ahora.strftime("%Y_%m_%d_%H_%M_%S"))
plt.show()

'''

# Crear la figura y el eje
fig, ax = plt.subplots(figsize=(7,7))
# Conectar el evento de cierre
fig.canvas.mpl_connect('close_event', on_close)
line, = ax.plot([X_ACT], [Y_ACT],'or',ms=5)  # línea inicial
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
dt=0.1
# Bucle para animar
h0=0



while running[0] or h0<step:
	print('exist?',running[0])
	PX_ACT=PX_ACT+px_dot.subs({x:X_ACT,y:Y_ACT,px:PX_ACT,py:PY_ACT}).evalf()
	PY_ACT=PY_ACT+py_dot.subs({x:X_ACT,y:Y_ACT,px:PX_ACT,py:PY_ACT}).evalf()

	X_ACT = X_ACT+PX_ACT*dt  # función que cambia con el tiempo
	Y_ACT = Y_ACT+PY_ACT*dt  # función que cambia con el tiempo
	line.set_xdata([X_ACT]) 
	line.set_ydata([Y_ACT])
	plt.pause(0.05)# pausa de 50 ms
	plt.draw()

plt.close(fig)
'''