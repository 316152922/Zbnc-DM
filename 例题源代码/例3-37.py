import pandas as pd
import numpy as np
data = [[9,3,1],[1,2,8],[1,0,5]]
df=pd.DataFrame(data,index=['S1','S2','S3'],columns=['c','a', 'b'])
print('按指定列的值大小顺序进行排序：\n',df.sort_values(by='c')) #默认升序
print('按指定多列的值大小顺序进行排序：\n',df.sort_values(by= ['c','a']))
#对DataFrame的值进行排序时，要使用by指定某一行（列）或者某几行（列）
print('按指定行值进行排序：\n',df.sort_values(by='S1',axis=1))
#在指定行值进行排序的时候，必须设置axis=1
