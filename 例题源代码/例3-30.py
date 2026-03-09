import numpy as np
import pandas as pd
df1=pd.DataFrame(np.arange(12).reshape((3,4)),columns=list('abcd'))
df2=pd.DataFrame(np.arange(20).reshape((4,5)),columns=list('abcde'))
print('A=\n',df1,'\nB=\n',df2)  #打印DataFrame对象
print('A+B=\n',df1.add(df2,fill_value=0)) #（或用df1+df2）输出df1与df2的和
print('A-B=\n',df1.sub(df2,fill_value=0)) #（或用df1-df2）输出df1与df2的差
print('A*B=\n',df1.mul(df2,fill_value=0)) #（或用df1*df2）输出df1与df2的积
print('A/B=\n',df1.div(df2,fill_value=0)) #（或用df1/df2）输出df1与df2的积
