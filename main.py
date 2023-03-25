import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import time

def text_screen(texto):
	for palavra in texto:
		print(palavra, end='', flush= True)
		time.sleep(0.01)

def torus(precision, c, a):
    U = np.linspace(0, 2*np.pi, precision)
    V = np.linspace(0, 2*np.pi, precision)
    U, V = np.meshgrid(U, V)
    X = (c+a*np.cos(V))*np.cos(U)
    Y = (c+a*np.cos(V))*np.sin(U)
    Z = a*np.sin(V)
    return X, Y, Z


def sphere(precision):
    a = np.linspace(0, 2 * np.pi, precision);
    b = np.linspace(0, np.pi, precision);
    x = np.outer(np.cos(a), np.sin(b))
    y = np.outer(np.sin(a), np.sin(b))
    z = np.outer(np.ones(np.size(a)), np.cos(b))
    return x,y,z

def geometric_plots(x,y,z, xp, yp, zp,OUTPUT):
    fig= plt.figure()
    ax  = fig.add_subplot(111, projection = '3d')
    ax.plot_surface(x,y,z,cmap="jet")#,rstride=1, cstride=1, linewidth=0, antialiased=False)
    ax.scatter(xp, yp, zp,marker='o', color='black')
    ax.grid(True)
    plt.savefig(OUTPUT)

text_screen(" =========================================== \n")
text_screen(" ==          Welcome to Raffa_V1.0        == \n")
text_screen(" ==            Builder to plot            == \n")
text_screen(" =========================================== \n")

text_screen(" Wait, generate the Sphere...\n")
x1,x2,x3 = sphere(250)

text_screen(" Wait, Build the sphere and points in our surface ...\n")
geometric_plots(x1,x2,x3,1,1,1,'Resultados_1.png')

x4,x5,x6 = torus(250, 1.0, 0.6)
geometric_plots(x4,x5,x6,1,1,1,'Resultados_2.png')

text_screen(" =========================================== \n")
text_screen(" ==          Desenvolvido por:            == \n")
text_screen(" ==        Dr. Mauricio A. Ribeiro        == \n")
text_screen(" ==    email: mau.ap.ribeiro@gmail.com    == \n")
text_screen(" =========================================== \n")
