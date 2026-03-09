import numpy as np
print(np.random.randint(5)) #生成0~5之间的整数
print(np.random.randint(5,size=4)) #生成0~5之间的4个元素数组
print(np.random.randint(5,10,size=6)) #生成5~10之间的6个元素数组
print(np.random.randint(5,10,size=(2,3),dtype='int')) #生成5~10之间的2×3数组
