import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
#生成月亮数据集
X,y=make_moons(n_samples=1000,noise=0.1)
plt.scatter(X[:,0],X[:,1],c=y,s=25)
plt.show()
