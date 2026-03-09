import pandas as pd
datas={'姓名':['许文秀','刘世元','刘德峰','于金凤'],
       '性别':['女','男','男','女'],
       '年龄':[20,21,22,20],
       '系部':['计算机系','电信系','统计系','计算机系']}
df=pd.DataFrame(datas,index=['S1','S2','S3','S4'])
print('查询前两行：\n',df[:2])
print('查询第2行：\n',df[1:2])
print('查询前3行：\n',df.head(3))
print('查询后两行：\n',df.tail(2))
