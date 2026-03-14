#La Fuerza de Lorentz = q(E+vxB)	con q(C)=escalar, {E(N/C);B(Ns/(Cm));v(m/s)}=vectores(R3) 

#qE es la contribución de cada cuerpo en fuerza electrica	
#q(vxB) la contribucion magnetica

#NOTA: se estan omitiendo algunas variables como phi constante dentro de sin y cos


from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np



from sympy import symbols, diff, Function
mpl.use('TkAgg')

x = symbols('x')  # variable simbólica
y = symbols('y')  # variable simbólica
px = symbols('px')  # variable simbólica
py = symbols('py')  # variable simbólica
T=px**2+py**2
V=(x**2+y**2)
H = T+V


PX_ACT=2
X_ACT=0
PY_ACT=0
Y_ACT=1

px_dot= -diff(H, x)

py_dot= -diff(H, y)



# Definir una bandera de control
running = [True]  # lista mutable, truco para modificar dentro de función

# Esta función se llama al cerrar la ventana
def on_close(event):
    running[0] = False





# Crear la figura y el eje
fig, ax = plt.subplots(figure=2)
# Conectar el evento de cierre
fig.canvas.mpl_connect('close_event', on_close)
line, = ax.plot([X_ACT], [Y_ACT],'or',ms=5)  # línea inicial
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
dt=0.1
# Bucle para animar
while running[0]:
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
