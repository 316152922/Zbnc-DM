import pandas as pd
import numpy as np
s = pd.Series([np.nan,1,7,2,3],index=['a','c','e','b','d'])    
print('按Series对象的值进行升序排序：\n',s.sort_values()) #默认是升序排序
print('按Seires对象的值进行降序排序：\n',s.sort_values(ascending=False))
