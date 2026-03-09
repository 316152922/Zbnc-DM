import pandas as pd
import os
os.chdir('D:\\Data_Mining') #设置当前路径
data = pd.read_csv('test.csv',encoding = 'gb18030')  # 读取文件数据
print(data)
