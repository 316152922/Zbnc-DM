import pandas as pd
datas={'姓名':['许文秀','刘世元','刘德峰','于金凤'],
       '性别':['女','男','男','女'],
       '年龄':[20,21,22,20],
       '系部':['计算机系','电信系','统计系','计算机系']}
df=pd.DataFrame(datas)
print('原数据：\n',df)
df1=df.rename({0:'S1',1:'S2',2:'S3',3:'S4'}) #修改行标题
print('修改行标题：\n',df1)
df1.rename(columns={'姓名':'name','性别':'sex','年龄':'age','系部':'dept'},inplace=True)
print('修改列标题：\n',df1)
