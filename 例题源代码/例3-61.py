import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,10,0.005) #以步长0.005绘制一个曲线
y=np.exp(-x/2.0)*np.sin(2*np.pi*x)
fig,ax=plt.subplots()
ax.plot(x,y)
ax.set_xlim(0,10)
ax.set_ylim(-1,1)
#被注释点的数据轴坐标和所在的像素
xdata,ydata=5,0
xdis,ydis=ax.transData.transform_point((xdata,ydata))
#设置注释文本的样式和箭头的样式
bbox1=dict(boxstyle='round',fc='0.8')
arrow1=dict(arrowstyle='->')
arrow2=dict(arrowstyle='->',connectionstyle='angle,angleA=0,angleB=90,rad=10') #用参数connectionstyle控制箭头弯曲
offset=72 #设置偏移量
#xycoords默认为'data'数据轴坐标，对坐标点(5,0)添加注释
#注释文本参考被注释点设置偏移量，向左2*72points，向上72points
ax.annotate('data=(%.1f,%.1f)'%(xdata,ydata),(xdata,ydata),xytext=(-2*offset,offset),textcoords='offset points',bbox=bbox1,arrowprops=arrow1)
#xycoords以绘图区左下角为参考，单位为像素
#注释文本参考被注释点设置偏移量，向左0.5*72points，向下72points
disp=ax.annotate('display=(%.1f,%.1f)'%(xdis,ydis),(xdis,ydis),xytext=(0.5*offset,-offset),xycoords='figure pixels',textcoords='offset points',bbox=bbox1,arrowprops=arrow2)
plt.show()
