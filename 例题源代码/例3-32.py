import pandas as pd
import numpy as np
df=pd.DataFrame(np.arange(12).reshape((3,4)),columns=list('ABCD'))
print('df中原始数据为：\n',df)
print('计算每个元素的平方根：\n',df.apply(np.sqrt))
print('计算每一列元素的平均值:\n',df.apply(np.mean))
print('计算每一行元素的平均值:\n',df.apply(np.mean,axis = 1))
print('增加第E列，为前面四列元素之和：')
def Add_a(x):
    return x.A+x.B+x.C+x.D
df['E']=df.apply(Add_a,axis=1)
print(df)
print('列E中所有元素加5：')
df.E=df.E.apply(lambda x:x+5)
print(df)
print('第E列元素被3整除的均赋值Yes，否则赋值No：')
df.E=df.E.apply(lambda x: 'Yes' if x%3==0 else  'No')
print(df)
