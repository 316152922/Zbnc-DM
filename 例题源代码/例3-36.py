import numpy as np
import pandas as pd
a = np.arange(9).reshape(3,3)
data=pd.DataFrame(a,index=['0','2','1'],columns=['c','a','b'])
print('按行的索引升序进行排序:\n',data.sort_index()) #默认按行升序
print('按行的索引降序进行排序:\n',data.sort_index(ascending= False))
print('按列的索引升序进行排序:\n',data.sort_index(axis=1)) #默认升序
print('按列的索引降序进行排序：\n',data.sort_index(axis=1, ascending=False))
