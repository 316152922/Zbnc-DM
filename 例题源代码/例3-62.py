from sklearn.datasets import load_iris
data=load_iris() #加载iris数据集
print(dir(data)) #查看data所具有的属性和方法
print('*'*80)
print(data.DESCR) #查看数据集的描述
print('*'*80)
print(data.feature_names) #查看数据的特征名
print('*'*80)
print(data.target_names) #查看数据的分类名
print('*'*80) 
print(data.target) #目标标签值
print('*'*80)
print(data.target[[1,10,100]]) #查看第2、11、101个样本的目标值
