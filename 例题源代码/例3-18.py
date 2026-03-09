import numpy as np
arr=np.arange(12).reshape([3,4])
print(arr[1,2])  #输出下标为[1,2]的元素
print(arr[1:,2:]) #输出行标为1,2列标为2,3的元素
print(arr[::2,1]) #输出行标为0,2列标为1的元素
