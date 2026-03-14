#La Fuerza de Lorentz = q(E+vxB)	con q(C)=escalar, {E(N/C);B(Ns/(Cm));v(m/s)}=vectores(R3) 

#qE es la contribución de cada cuerpo en fuerza electrica	
#q(vxB) la contribucion magnetica

#NOTA: se estan omitiendo algunas variables como phi constante dentro de sin y cos


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

L=5
# Crear una malla de puntos
x_vals = np.linspace(-L, L, L*10)
y_vals = np.linspace(-L, L, L*10)
x, y = np.meshgrid(x_vals, y_vals)

# Campo vectorial 2D en el plano z = 0, con componente z = 0
u = 1/((x**2 + y**2)**(3/2)) - (3 * x**2)/((x**2 + y**2)**(5/2))
v = -(3 * x * y)/((x**2 + y**2)**(5/2))
w = np.zeros_like(u)  # Componente z nula para mantenerlo en 2D

ax.quiver(x, y, np.zeros_like(x), u, v, w, length=0.1)

plt.show()