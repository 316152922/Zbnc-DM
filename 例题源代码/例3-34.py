import pandas as pd
s = pd.Series([1,2,3],index=['a','c','b']) 
print('按Series对象的索引进行升序排序：\n',s.sort_index()) #默认是升序
print('按Series对象的索引进行降序排序：\n',s.sort_index(ascending=False))
