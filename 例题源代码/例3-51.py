import matplotlib.pyplot as plt
x=[0,1,2,3,4,5,6]  #横坐标数据
y=[0.3,0.4,2,5,3,4.5,4]  #纵坐标数据
plt.figure(figsize=(8,4)) #创建绘图对象
plt.plot(x,y,'b-',linewidth=1) #当前对象绘图
plt.show() #结果展示
