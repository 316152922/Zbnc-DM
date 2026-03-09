import pandas as pd
datas =[['许文秀','女',21,'计算机系'],['于金凤','女',20,'计算机系'],['刘世元','男',22,'电信系'],['周新娥','女',20,'管理系']]
line_index=['S1','S2','S3','S4']
column_index=['姓名','性别','年龄','系部']
df =pd.DataFrame(datas,index=line_index,columns=column_index) 
print(df)
