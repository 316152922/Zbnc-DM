import pandas as pd
datas={'姓名':['许文秀','刘世元','刘德峰','于金凤'],
       '性别':['女','男','男','女'],
       '年龄':[20,21,22,20],
       '系部':['计算机系','电信系','统计系','计算机系']}
df=pd.DataFrame(datas)
df1=df.drop([2],axis=0,inplace=False) #删除序号为2的行
print('删除第3行：\n',df1)
df.drop('系部',axis=1,inplace=True) #删除系部列
print('删除系部一列：\n',df)
