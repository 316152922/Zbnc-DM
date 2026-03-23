

# 第3章 Python数据挖掘中的常用模块

Python 拥有强大的扩展能力，尤其在数据挖掘与数据分析领域，常用模块几乎可以满足各种需求：

- **NumPy**：科学计算模块，提供高效的矩阵运算；
- **Pandas**：基于 NumPy 的数据分析处理模块，提供数据挖掘工具；
- **Matplotlib**：数据可视化模块，具有类似 MATLAB 的绘图功能；
- **Scikit-learn**：机器学习模块，提供分类、回归、聚类等常用算法。

---

## 3.1 NumPy 模块

### 3.1.1 NumPy 数据类型

NumPy（Numerical Python）是一个开源数值计算扩展模块，用于存储和处理大型矩阵，支持大维度数组与矩阵运算，并提供了大量数学函数库。

#### ndarray 对象

NumPy 的核心数据结构是 `ndarray`（n-dimensional array），用于存储相同类型的元素集合，数组下标从 0 开始。

**导入方式**：

```python
import numpy as np          # 推荐方式
import numpy                 # 使用 numpy. 前缀
from numpy import *          # 不推荐，容易命名冲突
```

#### 创建 ndarray 对象

**1. 使用列表创建数组**

```python
import numpy as np
data = [3, -4, 7, 12]
x = np.array(data)          # 一维数组
print(x)

data2 = [[1, 2], [3, 4], [5, 6]]
y = np.array(data2)         # 二维数组
print(y)
```

**2. 使用 `range()` 和 `arange()` 创建一维数组**

- `range(start, end, step)`：返回 Python 列表，仅支持整数。
- `arange(start, end, step)`：返回 NumPy 数组，支持浮点数。

```python
a = np.arange(0, 1, 0.1)
print(a)
```

**3. 使用 `arange()` 和 `reshape()` 创建多维数组**

```python
b = np.arange(10).reshape(2, 5)   # 2行5列
print(b)
```

#### matrix 对象

`matrix` 是 `ndarray` 的子类，支持矩阵乘法运算符 `*`。

**创建方式**：

```python
a = np.mat('1 2 3; 4 5 6')               # 字符串形式
b = np.mat([[1, 2], [3, 4]])             # 嵌套列表
c = np.mat(np.random.rand(3, 4))         # 数组转换
```

**常用矩阵创建示例**：

```python
data1 = np.mat(np.zeros((3, 3)))         # 3x3 零矩阵
data2 = np.mat(np.ones((2, 4)))          # 2x4 全1矩阵
data3 = np.mat(np.random.rand(2, 2))     # 2x2 随机浮点矩阵
data4 = np.mat(np.random.randint(10, size=(3, 3)))  # 随机整数矩阵
data5 = np.mat(np.diag([1, 2, 3]))       # 对角矩阵
```

#### 列表与数组的区别

| 特性 | Python 列表 | NumPy 数组 |
|------|-------------|------------|
| 元素类型 | 可不同 | 必须相同 |
| 内存地址 | 不连续 | 连续 |
| 长度 | 可变 | 固定 |
| 运算支持 | 不支持矢量化 | 支持矢量化 |
| 方法 | 有 `append()` | 无 `append()` |
| 打印风格 | 逗号分隔 | 空格分隔 |

---

### 3.1.2 NumPy 基本运算

#### ndarray 基本运算（按元素）

```python
a = np.arange(3, 11, 2)   # [3, 5, 7, 9]
b = np.array([1, 4, 3, 2])
```

| 运算符 | 说明 | 示例 | 结果 |
|--------|------|------|------|
| `+` | 加法 | `a + b` | [4, 9, 10, 11] |
| `-` | 减法 | `a - b` | [2, 1, 4, 7] |
| `*` | 乘法 | `a * b` | [3, 20, 21, 18] |
| `/` | 除法 | `a / b` | [3, 1.25, 2.33, 4.5] |
| `%` | 取余 | `b % a` | [1, 1, 1, 1] |
| `**` | 幂运算 | `a ** 3` | [27, 125, 343, 729] |

**多维数组运算示例**：

```python
a = np.array([[1, 2, 3], [3, 4, 1]])
b = np.arange(6).reshape(2, 3)

print(a + b)
print(a * b)
print(a ** 3)
```

**点积运算**：

```python
a = np.array([0, 1, 2, 3])
b = np.array([2, 1, 3, -2])
print(np.dot(a, b))       # 一维点积

c = np.array([[4, 3], [2, 1]])
d = np.array([[1, 2], [3, 4]])
print(np.dot(c, d))       # 矩阵乘法
```

#### matrix 基本运算

**矩阵乘法**：

```python
a = np.mat([[1, 2], [3, 4]])
b = np.mat([[2, 0], [1, 3]])
print(a * b)              # 矩阵乘法
print(np.multiply(a, b))  # 对应元素相乘
```

**矩阵转置**：

```python
a = np.mat([[4, 3, 5, -4], [2, 1, 4, 0]])
print(a.transpose())
print(a.T)
```

**逆矩阵**：

```python
from numpy.linalg import inv

a = np.mat([[1, 0, 0], [3, 4, 0], [1, 2, 3]])
print(inv(a))
print(a.I)
```

---

### 3.1.3 生成随机数常用函数

#### `uniform()`：生成浮点型随机数

```python
np.random.uniform(low=0.0, high=1.0, size=None)
```

**示例**：

```python
print(np.random.uniform())           # 0~1
print(np.random.uniform(1, 5))       # 1~5
print(np.random.uniform(1, 5, 4))    # 一维数组
print(np.random.uniform(1, 5, (4, 3)))  # 4x3 数组
```

#### `randint()`：生成整型随机数

```python
np.random.randint(low, high=None, size=None, dtype='l')
```

**示例**：

```python
print(np.random.randint(5))          # 0~4
print(np.random.randint(5, size=4))  # 一维数组
print(np.random.randint(5, 10, size=(2, 3)))  # 2x3 数组
```

#### 案例：生成随机验证码

```python
import random

def gen_code(n):
    s = 'er0dfsdafxcvbn7f989fd'
    code = ''
    for i in range(n):
        r = random.randint(0, len(s) - 1)
        code += s[r]
    return code

username = input("输入用户名：")
passwd = input("输入密码：")
code = gen_code(5)
print("验证码是:", code)
code1 = input("输入验证码:")
if code.lower() == code1.lower():
    if username == 'knn' and passwd == 'abc':
        print("Login success!")
    else:
        print("username or password error!")
else:
    print("check code error!")
```

---

### 3.1.4 对象转换

#### 列表与字符串转换

**列表 → 字符串**：

```python
lst1 = ['This', 'is', 'a', 'apple']
print(''.join(lst1))

lst2 = ['S6', '许文秀', '女', 21, '计算机系']
print(''.join([str(x) for x in lst2]))
```

**字符串 → 列表**：

```python
str1 = 'Python program'
print(list(str1))
print(str1.split())
print(str1.split(','))
```

#### 数组与字符串转换

```python
lst = ['This', 'is', 'a', 'program']
arr = np.array(lst)
str1 = ''.join(arr)
print(str1)
```

#### 列表与数组转换

```python
lst = [-3, 4, 8, 6]
arr = np.array(lst)
print(arr)

# 数组转列表
lst2 = arr.tolist()
```

#### 列表与矩阵转换

```python
lst = [[1, 2, 3], [4, 5, 6]]
matr = np.mat(lst)
print(matr)
```

#### 数组与矩阵转换

```python
arr = np.array([[1, 2], [3, 4]])
matr = np.mat(arr)          # 数组转矩阵
arr2 = np.array(matr)       # 矩阵转数组
```

---

### 3.1.5 数组元素和切片

#### 一维数组

```python
arr = np.array([-4, 8, 12, 6, 9, 11, 25])
print(arr[4])          # 9
print(arr[2:5])        # [12, 6, 9]
print(arr[1:5:2])      # [8, 6]
```

#### 多维数组

```python
arr = np.arange(12).reshape([3, 4])
print(arr[1, 2])        # 第2行第3列
print(arr[1:, 2:])      # 行1~2，列2~3
print(arr[::2, 1])      # 行0、2，列1
```

