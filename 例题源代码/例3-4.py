import numpy as np
a=np.array([0,1,2,3])
b=np.array([2,1,3,-2])
c=np.array([[4, 3], [2, 1]])
d=np.array([[1, 2], [3, 4]])
print('一维数组乘法：',a*b)
print('一维数组点积：',np.dot(a,b))
print('二维数组乘法：\n',c*d)
print('二维数组点积：\n',np.dot(c,d))

