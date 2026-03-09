import pylab as pl
x = range(10)  # 横轴的数据
y = [i*i for i in x]  # 纵轴的数据
pl.rcParams['font.family']='STSong' #图形中显示汉字
pl.rcParams['font.size']=12  #显示汉字字体
pl.plot(x,y,'ob-',label='y=x^2曲线图')  # 调用pylab的plot函数绘制曲线
pl.xlabel('x轴')
pl.ylabel('y轴') 
pl.legend() #图例生效
pl.show()  # 显示绘制出的图
