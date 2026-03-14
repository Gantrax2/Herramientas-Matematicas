import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit




namefile='filename.txt'  # PONER ACA EL NOMBRE DEL ARCHIVO A LEER

print('Lectura archivo',namefile)
#x,y=np.loadtxt(namefile, skiprows=1, unpack=True, delimiter=',')  #SKIPROWS=1 SOLO SI  HACE FALTA

#Funcion de pruebita
x=np.linspace(0,500,10000)
y=np.cos((x/10)*2*np.pi)*10*np.exp(((x-50)/(2*25))**2)



plt.figure(figsize=(10,6))
plt.title('Hallar_Picos: Crudo', fontsize = 14)
plt.plot(x,y, label = 'data')
plt.xlabel('Y(x)', fontsize = 14)
plt.ylabel('X', fontsize = 14)
plt.legend(fontsize = 14)
plt.savefig(namefile[:-4]+' Crudo.png')
plt.show()

def hallarpicos(x, y, minmax='min', Ncomp=4):
                xmins, ymins=[], []
                if minmax=='min':
                    for i in range(len(y)-2*Ncomp):
                        for n in range(Ncomp):
                            if y[i+Ncomp]-y[i+Ncomp+n+1]>0:
                                break
                            if y[i+Ncomp]-y[i+Ncomp-n-1]>0:
                                break
                            if n+1==Ncomp:
                                xmins.append(x[i+Ncomp])
                                ymins.append(y[i+Ncomp])
            

                elif minmax=='max':
                    for i in range(len(y)-2*Ncomp):
                        for n in range(Ncomp):
                            if y[i+Ncomp]-y[i+Ncomp+n+1]<0:
                                break
                            if y[i+Ncomp]-y[i+Ncomp-n-1]<0:
                                break
                            if n+1==Ncomp:
                                xmins.append(x[i+Ncomp])
                                ymins.append(y[i+Ncomp])

                
                    
                return xmins, ymins

def inetrpolValue(x,y,xdes):
    ydes=False
    for i in range(len(x)):
        if i>0:
            if x[i]==xdes:
                ydes=y[i]
                break
            elif x[i]>xdes:
                ydes=(y[i]-y[i-1])*(x[i]-xdes)/(x[i]-x[i-1])+y[i-1]
                break
    if ydes:
        return ydes
    else:
        return False
def Gaussian(x,a,b,c,d):
    return d+c*np.exp(-(((x-a)/b)**2)/2)



lencortes=10 #Minimo ancho para cada lado de las campanas a buscar

xext,yext=hallarpicos(x,y,'max',lencortes)

plt.figure()
plt.title('Ajustes gaussianas', fontsize = 14)
plt.plot(x,y,'ob',ms=1, label = 'Data')
fi=open('salida_frec.txt','w')
fi.write('Frec,Amp\n')
cortes={}
for i in range(len(yext)):
    indx0=min([len(x),max([0,list(x).index(xext[i])-lencortes])])
    indx1=min([len(x),max([0,list(x).index(xext[i])+lencortes])])

    popt, pcov=curve_fit(Gaussian, x[indx0:indx1], y[indx0:indx1], p0=[xext[i],(x[indx1]-x[indx0])/4,yext[i]-y[indx0],y[indx0]], maxfev=10000)
    perr=np.sqrt(np.diag(pcov))
    cortes[i]=[x[indx0:indx1], y[indx0:indx1],popt,perr, indx0, indx1]
    
    xteo=np.linspace(x[indx0],x[indx1],100)
    yteo=Gaussian(xteo,popt[0],popt[1],popt[2],popt[3])

    if i==0:
        plt.plot(popt[0], inetrpolValue(list(x),list(y),popt[0]),'or',ms=3, label =  'Máximos Hallados')
    else:
        plt.plot(popt[0], inetrpolValue(list(x),list(y),popt[0]),'or',ms=3)
    print('%i Máximo hallado : %.5f'%(i,popt[0]), 'Intensidad relativa: %.5f'%inetrpolValue(list(x),list(y),popt[0]))

    fi.write('%.8f,%.8f\n'%(popt[0],inetrpolValue(list(x),list(y),popt[0])))
    plt.plot(xteo,yteo,'-r',label = 'Ajuste parte %i'%i)
fi.close()

plt.xlabel('Y(x)', fontsize = 14)
plt.ylabel('X', fontsize = 14)
plt.show()
