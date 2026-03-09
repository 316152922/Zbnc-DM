import pandas as pd
head=['学号','姓名','性别','年龄','系部']
data=[['S1','许文秀','女',20,'计算机系'],
      ['S2','刘德峰','男',21,'电信系'],
      ['S3','刘世元','男',22,'管理系'],
      ['S4','于金凤','女',21,'计算机系']]
df=pd.DataFrame(data,columns=head)
file='D:\\Data_Mining\stud11.xlsx'
df.to_excel(file)
