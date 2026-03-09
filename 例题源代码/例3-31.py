import pandas as pd
datas={'姓名':['许文秀','刘世元','刘德峰','于金凤'],
       '性别':['女','男','男','女'],
       '年龄':[20,21,22,20],
       '系部':['计算机系','电信系','统计系','计算机系']}
df=pd.DataFrame(datas)
def sex_map(x):    #将性别'男'改为'M','女'改为'F'
    sex='F'
    if x=='男': sex ='M'
    return sex  #该函数也可以用字典sex_map={'男':'M','女':'F'}替代
df['性别']=df['性别'].map(sex_map)
print(df)
