import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
#生成圆环形状数据集
X,y=make_circles(n_samples=1000,factor=0.6,noise=0.1)
plt.scatter(X[:,0],X[:,1],c=y,s=25)
plt.show()
