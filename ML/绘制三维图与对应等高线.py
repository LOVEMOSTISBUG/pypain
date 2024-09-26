from matplotlib import pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax1 = plt.axes(projection = "3d") #创建三维格式对象Axes3D

ww = np.arange(-10,10,0.1)
bb = np.arange(-10,10,0.1)
W,B = np.meshgrid(ww,bb)#创建两个二维数组
Z = W**2+B**2

#ax1.plot_surface(W,B,Z,rstride=1,cstride=1,cmap="rainbow") #精细作图
#ax1.plot_wireframe(W,B,Z)#网格图
ax1.plot_surface(W,B,Z,alpha=0.6,cmap="winter")
ax1.contourf(W,B,Z,zdir="",offset=-3,cmap="rainbow") #Z轴投影到WB上


plt.show()
