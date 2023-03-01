from audioop import add
from cProfile import label
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np


x=np.linspace(-10,9,20)

y=x**3
z=x**2


"""
figure=plt.figure()
axes_cube=figure.add_axes([0.1,0.1,0.8,0.8]) #düzelmin konumunu ayarlar
axes_cube.plot(x,y,"b")
axes_cube.set_xlabel("xaxis")
axes_cube.set_ylabel("yaxis")
axes_cube.set_title("cube")

axes_square=figure.add_axes([0.15,0.6,0.25,0.25])
axes_square.plot(x,z,"r")
axes_square.set_xlabel("x axis")
axes_square.set_ylabel("y axis")
axes_square.set_title("square")
"""
"""
figure=plt.figure()
axes=figure.add_axes([0,0,1,1])
axes.plot(x,z,label="square")
axes.plot(x,y,label="cube")
axes.legend(loc=4)
"""

fig,axes=plt.subplots(nrows=2,ncols=1,figsize=(4,4))
axes[0].plot(x,y)
axes[0].set_title("cube")

axes[1].plot(x,z)
axes[1].set_title("square")

plt.tight_layout()
fig.savefig("figure1.png")
plt.show()