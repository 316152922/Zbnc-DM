import pandas as pd
import numpy as np
dict = {'key1' : ['a', 'b', 'a', 'b','a', 'b', 'a', 'a'],
        'key2' : ['one', 'one', 'two', 'three','two', 'two', 'one', 'three'],
        'data1': np.random.randn(8), 'data2': np.random.randn(8)}
df= pd.DataFrame(dict)
print('\n创建的DataFrame对象：\n',df)
grouped1 = df.groupby('key1') 
print('\n第一分组均值：\n',grouped1.mean())  # dataframe根据key1进行分组
grouped2 = df['data1'].groupby(df['key1']) # dataframe的 data1 列根据 key1 进行分组
print('\n第二分组均值：\n',grouped2.mean())
print('\n分组一元素个数：\n',grouped1.size()) 
print('\n分组二元素个数：\n',grouped2.size())
