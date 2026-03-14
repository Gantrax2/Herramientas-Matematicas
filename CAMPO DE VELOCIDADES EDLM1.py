#La Fuerza de Lorentz = q(E+vxB)	con q(C)=escalar, {E(N/C);B(Ns/(Cm));v(m/s)}=vectores(R3) 

#qE es la contribución de cada cuerpo en fuerza electrica	
#q(vxB) la contribucion magnetica

#NOTA: se estan omitiendo algunas variables como phi constante dentro de sin y cos



from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

#ax = fig.gca(projection='3d')

U=10
A=np.pi/4
rad=1
S=3
dif=0.5
X, Y = np.arange(-S, S, dif),np.arange(-S, S, dif)
x, y =np.meshgrid(X, Y)
print(x, y)
for i in range(len(x)):
	for n in range(len(x[0])):
		if x[i][n]**2+ y[i][n]**2 > rad**2:
			pass
		else:
			if n==0:

				x[i]=np.array([rad]+list(x[i])[n+1:])
				y[i]=np.array([rad]+list(y[i])[n+1:])
			elif n==len(x[0])-1:

				x[i]=np.array(list(x[i])[:n]+[rad])
				y[i]=np.array(list(y[i])[:n]+[rad])

			else:
				
				x[i]=np.array(list(x[i])[:n]+[rad]+list(x[i])[n+1:])
				y[i]=np.array(list(y[i])[:n]+[rad]+list(y[i])[n+1:])

u = U*(1-(rad**2)*(x**2-y**2)/((x**2-y**2)**2+(2*x*y)**2))
v = U*(-(rad**2)*(2*x*y)/((x**2-y**2)**2+(2*x*y)**2))

fig = plt.figure(figsize =(6, 6))
plt.quiver(x,y, u, v)

plt.show()