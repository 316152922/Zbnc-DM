
# 3.4 Scikit-learn

Scikit-learn（简称 sklearn）是用 Python 实现的机器学习算法库，依赖于 NumPy、SciPy 和 Matplotlib，封装了大量经典及最新的机器学习模型。具备出色的接口设计和高效的学习能力。

安装方式：`pip install -U scikit-learn`

---

## 3.4.1 Scikit-learn 的主要功能

Scikit-learn 主要包含六大功能模块：

| 功能 | 说明 | 常见算法 |
|------|------|----------|
| 分类 | 对给定对象指定所属类别 | 支持向量机(SVM)、K最邻近算法(KNN) |
| 回归 | 研究因变量和自变量之间的显著关系 | 向量回归(SVR)、Lasso回归、贝叶斯回归 |
| 聚类 | 自动识别具有相似属性的对象并分组 | K-均值聚类、分层聚类、DBSCAN |
| 数据降维 | 减少随机变量个数，用于可视化和效率提升 | 主成分分析(PCA)、非负矩阵分解(NMF) |
| 模型选择 | 比较、验证和选择模型，通过参数调整提升精度 | 交叉验证、各种评估度量函数 |
| 数据预处理 | 数据清理、集成、归约、规范化等 | 标准化、归一化、缺失值处理 |

---

## 3.4.2 Scikit-learn 自带小数据集

Sklearn 的 `datasets` 模块内置了一些小规模标准数据集，无需下载即可使用。

| 数据集名称 | 说明 | 用途 | 样本×特征 |
|-----------|------|------|-----------|
| `iris()` | 鸢尾花 | 多分类任务 | 150×4 |
| `boston()` | 波士顿房价 | 回归任务 | 506×13 |
| `breast_cancer()` | 乳腺癌 | 二分类任务 | 569×30 |
| `linnerud()` | 健身 | 多变量回归 | 20×3 |
| `wine()` | 红酒 | 分类任务 | 178×13 |
| `diabetes()` | 糖尿病 | 回归分析 | 442×10 |
| `digits()` | 手写数字 | 分类任务 | 1797×64 |

### 1. 鸢尾花数据集（Iris）

150个样本，3类，每类50个，每个样本4个特征：花萼长度、花萼宽度、花瓣长度、花瓣宽度（单位：厘米）。用于预测鸢尾花的种类（Setosa、Versicolour、Virginica）。

```python
from sklearn.datasets import load_iris

# 加载数据集
data = load_iris()

# 查看数据集的属性和方法
print(dir(data))

# 查看数据集描述
print(data.DESCR)

# 查看特征名称
print(data.feature_names)

# 查看类别名称
print(data.target_names)

# 查看目标标签值
print(data.target)

# 查看第2、11、101个样本的目标值（索引1、10、100）
print(data.target[[1, 10, 100]])
```

### 2. 波士顿房价数据集（Boston）

506条数据，包含13个特征：城镇人均犯罪率、住宅用地比例、一氧化氮浓度、住宅平均房间数、到中心区域的加权距离、自住房平均房价等。

```python
from sklearn.datasets import load_boston   # 注意：新版本中load_boston已弃用，可改用fetch_openml

# 旧版本方式
boston = load_boston()
print(boston.DESCR)
```

> **注意**：从 scikit-learn 1.2 版本开始，`load_boston` 已被移除。推荐使用 `fetch_openml` 获取波士顿房价数据：
> ```python
> from sklearn.datasets import fetch_openml
> boston = fetch_openml(name='boston', version=1, as_frame=True)
> ```

### 3. 手写数字数据集（Digits）

1797个样本，每个样本是8×8的灰度图像，共64个特征，目标为0~9的数字分类。

```python
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

# 加载前5个类别的数据（可选）
data = load_digits(n_class=5, return_X_y=False)

print(data.target[0:10])          # 查看前10个样本的目标值
print(dir(data))
print(data.DESCR)
print(data.data)                   # 特征矩阵
print(data.feature_names)          # 特征名称（像素点）
print(data.target_names)           # 目标类别名称
print(data.target)                 # 所有目标值
print(data.target[[2, 20, 200]])   # 查看第3、21、201个样本的目标值
print(data.images.shape)           # 图像形状 (1797, 8, 8)

# 显示第一个数字图像
plt.imshow(data.images[0], cmap='gray')
plt.show()
```

---

## 3.4.3 Scikit-learn 生成数据集

Sklearn 提供多种生成虚拟数据集的函数，用于测试算法。

### 1. 生成聚类和分类数据集

#### (1) `make_blobs` – 生成聚类数据集

```python
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# 生成数据：100个样本，2个特征，3个中心，随机种子固定
X, y = make_blobs(n_samples=100, n_features=2, centers=3,
                  random_state=42, cluster_std=[0.8, 2, 5])

# 绘制散点图，按类别着色
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()
```

#### (2) `make_classification` – 生成分类数据集

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification

# 生成400个样本，2个特征，3个类别，每个类别一个簇
X, y = make_classification(n_samples=400, n_features=2, n_informative=2,
                           n_redundant=0, n_clusters_per_class=1,
                           n_classes=3, random_state=42)

plt.scatter(X[:, 0], X[:, 1], marker='o', c=y)
plt.show()
```

### 2. 生成环形和月亮形状数据集

#### (1) `make_circles` – 环形数据

```python
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles

# 生成1000个样本，内外圆比例0.5，无噪声
X, y = make_circles(n_samples=1000, factor=0.5, noise=0.0)

plt.scatter(X[:, 0], X[:, 1], c=y, s=25)
plt.show()
```

#### (2) `make_moons` – 月亮形状数据

```python
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons

# 生成1000个样本，添加0.1的噪声
X, y = make_moons(n_samples=1000, noise=0.1)

plt.scatter(X[:, 0], X[:, 1], c=y, s=25)
plt.show()
```

### 3. 生成高斯分位数数据集

```python
import matplotlib.pyplot as plt
from sklearn.datasets import make_gaussian_quantiles

# 生成2维正态分布，按分位数分成3组，1000个样本，均值[1,2]，协方差系数2
X, y = make_gaussian_quantiles(n_samples=1000, n_features=2,
                               n_classes=3, mean=[1, 2], cov=2)

plt.scatter(X[:, 0], X[:, 1], c=y, marker='o')
plt.show()
```

### 4. 生成回归数据集

```python
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression

# 生成100个样本，1个特征，噪声10，返回回归系数
X, y, coef = make_regression(n_samples=100, n_features=1,
                              noise=10, coef=True, random_state=42)

plt.scatter(X, y)
plt.show()
```

---

# 3.5 股票数据简单分析
#### 代码可详见 - [获取源代码](例题源代码/3.5代码-股票数据的简单分析.md)
本部分演示如何通过网络爬虫获取股票数据，并进行简单的可视化分析。

---

## 3.5.1 抓取股票数据

使用 `urllib` 抓取证券之星网站上的 A 股数据，并保存为 CSV 文件。

```python
import urllib.request
import re
import csv
import os

# 目标网址（证券之星A股排名页）
url = 'http://quote.stockstar.com/stock/ranklist_a_3_1_1.html'

# 伪装浏览器请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'}

# 请求网页
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('gbk')   # 网页编码为gbk

# 提取表格体内容
pattern = re.compile('tbody[\s\S]*</tbody>')
body = re.findall(pattern, str(content))

# 提取所有标签之间的文本
pattern = re.compile('>(.*?)<')
stock_page = re.findall(pattern, body[0])

# 清理空字符串
stock_last = [x for x in stock_page if x != '']

# 表头
head = ['代码', '简称', '最新价', '涨跌幅', '涨跌额', '5分钟涨幅']

# 按每6个一组组织数据
lst = []
for i in range(0, len(stock_last), 6):
    lst.append(stock_last[i:i+6])

# 设置保存路径（请根据实际情况修改）
os.chdir('D:\\data_mining\\gupiaoshujufenxi')

# 写入CSV文件
with open('test.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(head)
    writer.writerows(lst)

print("数据抓取并保存完成！")
```

> **说明**：实际运行前请确保目标网址有效，并安装必要的库（标准库无需额外安装）。

---

## 3.5.2 股票数据各指标折线图

以顺序号为横坐标，绘制“最新价”“涨跌幅”“涨跌额”三条折线图，观察整体趋势。

```python
import pandas as pd
import matplotlib.pyplot as plt
import os

# 设置路径
os.chdir('D:\\data_mining\\gupiaoshujufenxi')

# 读取CSV文件
data = pd.read_csv('test.csv', encoding='utf-8-sig')

# 设置中文字体
plt.rcParams['font.family'] = 'STSong'
plt.rcParams['font.size'] = 12

# 绘制折线图
data['最新价'].plot(grid=True)
data['涨跌幅'].plot(grid=True)
data['涨跌额'].plot(grid=True)

plt.legend(['最新价', '涨跌幅', '涨跌额'])
plt.show()
```

---

## 3.5.3 各股票5分钟涨幅柱状图

每6只股票为一组，绘制“5分钟涨幅”的柱状图。

```python
import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir('D:\\data_mining\\gupiaoshujufenxi')
data = pd.read_csv('test.csv', encoding='utf-8-sig')

plt.rcParams['font.family'] = 'STSong'
plt.rcParams['font.size'] = 12

# 每6只股票为一组
for i in range(0, len(data), 6):
    group = data.iloc[i:i+6]
    names = group['简称']
    values = group['5分钟涨幅']

    plt.figure()
    plt.bar(names, values, width=0.5)
    plt.title(f'第{i//6 + 1}张图')
    plt.legend(['5分钟涨幅'])
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
```

---

## 3.5.4 股票各指标之间关系对比

使用 `pandas.plotting.scatter_matrix` 绘制各指标之间的散点矩阵图，对角线为直方图，便于观察相关性。

```python
import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir('D:\\data_mining\\gupiaoshujufenxi')
data = pd.read_csv('test.csv', encoding='utf-8-sig')

plt.rcParams['font.family'] = 'STSong'
plt.rcParams['font.size'] = 12

# 选取需要分析的指标列
small = data[['最新价', '涨跌幅', '涨跌额', '5分钟涨幅']]

# 绘制散点矩阵
pd.plotting.scatter_matrix(small, alpha=0.5, figsize=(10, 10))
plt.show()
```

