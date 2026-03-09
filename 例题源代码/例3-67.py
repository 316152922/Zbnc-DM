import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
# X为样本特征，y为样本类别输出，共400个样本，每个样本2个特征，输出有3个类别，没有冗余特征，每个类别一个簇
X,y=make_classification(n_samples=400,n_features=2, n_redundant =0,n_clusters_per_class=1, n_classes=3)
print(X,'\n',y)
plt.scatter(X[:,0], X[:,1], marker='o', c=y)
plt.show()
