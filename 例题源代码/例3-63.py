import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
data=load_digits(n_class=5,return_X_y=False)
print(data.target[0:10]) #查看第1-10个样本的目标值
print(dir(data)) 
print('*'*80)
print(data.DESCR) 
print('*'*80)
print(data.data) 
print('*'*80)
print(data.feature_names) 
print('*'*80)
print(data.target_names) 
print('*'*80) 
print(data.target) 
print('*'*80)
print(data.target[[2,20,200]]) #查看第3、21、201个样本的目标值
print('*'*80)
print(data.images.shape) #查看数字图形的形式
print('*'*80)
plt.matshow(data.images[1]) #查看数字图像
plt.show() 
