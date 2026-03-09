import numpy as np 
import matplotlib.pyplot as plt
plt.figure()  #创建画布
x=np.arange(1,8) #绘图及修饰
y=np.array([15,20,22,23,20,18,16])
plt.xlabel('SUNDAY')
plt.ylabel('MAX_TEMPERATURE')
plt.plot(x,y)
plt.show() #图形展示
