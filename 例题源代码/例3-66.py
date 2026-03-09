from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt 
data,target=make_blobs(n_samples=100,n_features=2,centers=3)
# 在2D图中绘制数据样本，每个样本颜色不同
plt.scatter(data[:,0],data[:,1],c=target);
plt.show()
