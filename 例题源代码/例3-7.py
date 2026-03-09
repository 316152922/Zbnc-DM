import numpy as np
print(np.random.uniform())  #默认为0到1
print(np.random.uniform(1,5)) #生成1到5之间的float数
print(np.random.uniform(1,5,4)) # 生成一维数组
print(np.random.uniform(1,5,(4,3))) # 生成4×3的数组
print(np.random.uniform([1,5],[5,10]))
