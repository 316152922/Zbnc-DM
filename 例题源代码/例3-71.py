import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
X, y, coef =make_regression(n_samples=1000, n_features=1, noise=20, coef=True) #共1000个样本，每个样本1个特征
plt.scatter(X, y,  color='black')  
plt.plot(X, X*coef, color='blue',linewidth=3)
plt.show()

