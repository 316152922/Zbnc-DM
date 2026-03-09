import pandas as pd
datas ={'姓名':['许文秀','于金凤','刘世元','周新娥'],'性别':['女','女','男','女'],'年龄':[21,20,22,20],'系部':['计算机系','电信系','计算机系','管理系']}
line_index=['S1','S2','S3','S4']
df =pd.DataFrame(datas,index=line_index) 
print(df)
