import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import time

def text_screen(texto):
	for palavra in texto:
		print(palavra, end='', flush= True)
		time.sleep(0.01)

def sphere(N_D):
    a = np.linspace(0, 2 * np.pi, N_D);
    b = np.linspace(0, np.pi, N_D);
    x = np.outer(np.cos(a), np.sin(b))
    y = np.outer(np.sin(a), np.sin(b))
    z = np.outer(np.ones(np.size(a)), np.cos(b))
    return x,y,z

def sphere_plots(x,y,z, xp, yp, zp,OUTPUT):
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
sphere_plots(x1,x2,x3,1,1,1,'Resultados_1.png')


text_screen(" =========================================== \n")
text_screen(" ==          Desenvolvido por:            == \n")
text_screen(" ==        Dr. Mauricio A. Ribeiro        == \n")
text_screen(" ==    email: mau.ap.ribeiro@gmail.com    == \n")
text_screen(" =========================================== \n")