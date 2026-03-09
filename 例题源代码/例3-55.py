import matplotlib.pyplot as plt
import numpy as np
x_data=['2016','2017','2018','2019','2020','2021','2022']
y_data1=[58000,60200,63000,71000,84000,90500,107000]
y_data2=[52000,54200,51500,58300,56800,59500,62700]
bar_width=0.3
plt.rcParams['font.family']='STSong' #图形中显示汉字
plt.rcParams['font.size']=12  #显示汉字字体
plt.bar(x=np.arange(len(x_data)),height=y_data1,label='数据库技术',color='blue',alpha=0.8,width=bar_width)
plt.bar(x=np.arange(len(x_data))+bar_width,height=y_data2,label='数据挖掘',color='red',alpha=0.8,width=bar_width)
for x,y in enumerate(y_data1):
    plt.text(x,y+100,'%s'% y,ha='center',va='bottom')
for x,y in enumerate(y_data2):
    plt.text(x+bar_width,y+100,'%s'% y,ha='center',va='top')
plt.title('数据库技术与数据挖掘销售对比')
plt.xlabel('2016~2022年度')
plt.ylabel('销量')
plt.legend()
plt.show()
