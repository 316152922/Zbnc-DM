import pandas as pd
import numpy as np
dict = {'key1' : ['a', 'b', 'a', 'b','a', 'b', 'a', 'a'],
        'key2' : ['one', 'one', 'two', 'three','two','two', 'one', 'three'],
        'data1': np.random.randn(8),'data2': np.random.randn(8)}
df = pd.DataFrame(dict)
print(df)
#使用聚合函数
print(df.groupby('key1').sum())
print(df.groupby('key1').max())
print(df.groupby('key1').min())
print(df.groupby('key1').mean())
print(df.groupby('key1').size())
print(df.groupby('key1').count())
print(df.groupby('key1').describe())
