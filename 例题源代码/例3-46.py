import numpy as np
import matplotlib.pyplot as plt
x1=np.arange(-2,2,0.01)
p1=plt.figure(figsize=(8,4),dpi=80) #第一幅子图，并确定画布大小
ax1=p1.add_subplot(1,2,1) #创建一个2行1列的子图，并开始绘制第一幅
plt.title('Power Function')
plt.plot(x1,x1**2)
plt.plot(x1,x1**4)
plt.legend(['y=x^2','y=x^4'])
ax2=p1.add_subplot(1,2,2)
plt.title('e^x/log(x)')
x2=np.arange(0.1,4,0.01)
plt.plot(x2,np.exp(x2))
plt.plot(x2,np.log(x2))
plt.legend(['y=e^x','y=log(x)'])
plt.show()  # 显示绘制出的图
