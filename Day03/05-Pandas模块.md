

# 3.2 Pandas 模块

Pandas 是基于 NumPy 的一种数据分析工具，专为处理结构化数据而设计，具有高效、灵活的特点。它提供了两种核心数据结构：**Series** 和 **DataFrame**。

---

## 3.2.1 Pandas 中的数据结构

### 1. Series 对象

Series 是一维带标签的数组，可以存储任意数据类型（整数、浮点数、字符串等）。它由两个数组组成：

- 主元素数组（值）
- 索引数组（标签）

**创建方式**：

- 通过列表创建：`pd.Series(data, index=index)`
- 通过字典创建：字典的键成为索引，值成为数据

```python
import pandas as pd

# 通过列表创建，指定索引
s1 = pd.Series([12, 5, 7, 21], index=[4, 2, 3, 1])
s2 = pd.Series([12, 5, 7, 21], index=['a', 'b', 'c', 'd'])

# 通过字典创建
s3 = pd.Series({'a': 21, 'b': 213, 'c': 309, 'd': 210, 'e': 111})

print("s1:\n", s1)
print("s2:\n", s2)
print("s3:\n", s3)
```

输出示例（索引顺序按字典键顺序）：

```
s1:
4    12
2     5
3     7
1    21
dtype: int64
...
```

### 2. DataFrame 对象

DataFrame 是一个二维表格型数据结构，包含行索引和列索引，可以看作由多个 Series 组成的字典。

**创建方式**：使用二维列表，并指定行索引和列标签。

```python
# 二维列表数据
dataS = [
    ['许文秀', '女', 21, '计算机系'],
    ['于金凤', '女', 20, '计算机系'],
    ['刘世元', '男', 22, '电信系'],
    ['周新娥', '女', 20, '管理系']
]

line_index = ['S1', 'S2', 'S3', 'S4']
column_index = ['姓名', '性别', '年龄', '系部']

df = pd.DataFrame(dataS, index=line_index, columns=column_index)
print(df)
```

输出：

```
    姓名 性别  年龄   系部
S1  许文秀  女  21  计算机系
S2  于金凤  女  20  计算机系
S3  刘世元  男  22   电信系
S4  周新娥  女  20   管理系
```

---

## 3.2.2 DataFrame 的基本属性

| 属性/方法 | 说明 | 示例 | 结果 |
|----------|------|------|------|
| `values` | 获取 ndarray 类型的元素 | `df.values` | `[['许文秀' '女' 21 '计算机系'] ...]` |
| `index` | 获取行索引 | `df.index` | `Index(['S1','S2','S3','S4'], dtype='object')` |
| `axes` | 获取行及列索引 | `df.axes` | `[Index(...), Index(...)]` |
| `columns` | 获取列名列表 | `df.columns` | `Index(['姓名','性别','年龄','系部'], dtype='object')` |
| `size` | 获取元素个数 | `df.size` | `16` |
| `ndim` | 获取维度 | `df.ndim` | `2` |
| `shape` | 获取形状 | `df.shape` | `(4, 4)` |

示例代码：

```python
print("values:\n", df.values)
print("index:", df.index)
print("columns:", df.columns)
print("shape:", df.shape)
```

---

## 3.2.3 DataFrame 常用方法（补充）

| 方法 | 说明 | 示例 | 结果 |
|------|------|------|------|
| `iloc[行序, 列序]` | 按整数位置索引 | `df.iloc[:, 0:2]` | 前两列数据 |
| `loc[行标签, 列标签]` | 按标签索引 | `df.loc['S2', '姓名']` | `'于金凤'` |
| `head(i)` | 显示前 i 行 | `df.head(1)` | 第一行数据 |
| `tail(i)` | 显示后 i 行 | `df.tail(1)` | 最后一行数据 |
| `describe()` | 数值列统计信息 | `df.describe()` | 年龄的 count, mean, std, min, max 等 |
| `del` | 删除指定列 | `del df['性别']` | 删除“性别”列 |
| `drop(columns=[...])` | 同时删除多列 | `df.drop(columns=['性别','系部'])` | 返回新 DataFrame |
| `rename(columns={})` | 修改列名 | `df.rename(columns={'姓名':'Name'})` | 列名更改 |
| `copy()` | 复制 DataFrame | `df1 = df.copy()` | 深拷贝 |

---

## 3.2.4 DataFrame 的数据查询与编辑

### 1. 数据查询

#### (1) 查询列数据

通过列标签或属性方式获取列，返回 Series；多列需使用列表。

```python
import pandas as pd

data = {
    '姓名': ['许文秀', '刘世元', '刘德峰', '于金凤'],
    '性别': ['女', '男', '男', '女'],
    '年龄': [20, 21, 22, 20],
    '系部': ['计算机系', '电信系', '统计系', '计算机系']
}
df = pd.DataFrame(data, index=['S1', 'S2', 'S3', 'S4'])

print("查询姓名列:\n", df[['姓名']])
print("查询姓名和年龄列:\n", df[['姓名', '年龄']])
```

#### (2) 查询行数据

使用切片（基于位置）、`head()`、`tail()` 等方法。

```python
print("查询前两行:\n", df[:2])
print("查询第2行:\n", df[1:2])
print("查询前3行:\n", df.head(3))
print("查询后两行:\n", df.tail(2))
```

#### (3) 同时查询行和列

使用 `loc`（标签）和 `iloc`（位置）。

```python
# loc：行标签，列标签
print("查询 S1 和 S3 的姓名和系部:\n", df.loc[['S1', 'S3'], ['姓名', '系部']])

# iloc：行序号，列序号
print("查询第1和第3行的第2列（性别）:\n", df.iloc[[1, 3], [1]])
```

#### (4) 条件查询

使用布尔表达式过滤数据。

```python
# 查询姓名为刘德峰的行
print("姓名为刘德峰:\n", df[df['姓名'] == '刘德峰'])

# 查询计算机系的女同学
print("计算机系的女同学:\n", df[(df['性别'] == '女') & (df['系部'] == '计算机系')])
```

### 2. 数据编辑

#### (1) 添加数据

- 添加行：使用 `append()`（注意：`append` 在较新版本中已弃用，推荐使用 `pd.concat`）。
- 添加列：直接赋值。

```python
# 添加一行（注意：需创建新 DataFrame）
new_row = {'姓名': '王文庆', '性别': '男', '年龄': 21, '系部': '电信系'}
df1 = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

# 添加一列
df1['籍贯'] = ['河北省', '天津市', '河北省', '重庆市', '江苏省']
print(df1)
```

#### (2) 删除数据

使用 `drop()`，通过 `axis` 控制行（0）或列（1），`inplace` 控制是否修改原对象。

```python
# 删除第3行（索引为2）
df1 = df.drop([2], axis=0, inplace=False)

# 删除“系部”列（在原对象上删除）
df.drop('系部', axis=1, inplace=True)
print(df)
```

#### (3) 修改数据

修改行/列索引使用 `rename()`，修改具体值直接赋值。

```python
# 修改行索引
df1 = df.rename({0: 'S1', 1: 'S2', 2: 'S3', 3: 'S4'})

# 修改列名
df1.rename(columns={'姓名': 'name', '性别': 'sex', '年龄': 'age', '系部': 'dept'}, inplace=True)
print(df1)
```

---

## 3.2.5 Pandas 数据四则运算

两个 DataFrame 进行四则运算时，对应元素运算。对于不同维度，缺失位置用 `NaN` 填充；可通过 `fill_value` 指定填充值。

```python
import numpy as np

df1 = pd.DataFrame(np.arange(12).reshape(3, 4), columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20).reshape(4, 5), columns=list('abcde'))

print("A:\n", df1)
print("B:\n", df2)

# 加法，缺失值填充 0
print("A + B:\n", df1.add(df2, fill_value=0))

# 减法
print("A - B:\n", df1.sub(df2, fill_value=0))

# 乘法
print("A * B:\n", df1.mul(df2, fill_value=0))

# 除法
print("A / B:\n", df1.div(df2, fill_value=0))
```

---

## 3.2.6 函数变换

### `apply()`

对 DataFrame 的行或列应用函数。

```python
df = pd.DataFrame(np.arange(12).reshape(3, 4), columns=list('ABCD'))

# 对每个元素求平方根
print(df.apply(np.sqrt))

# 对每一列求平均值
print(df.apply(np.mean))

# 对每一行求平均值
print(df.apply(np.mean, axis=1))

# 增加一列 E，为前四列之和
def Add_a(x):
    return x.A + x.B + x.C + x.D
df['E'] = df.apply(Add_a, axis=1)

# 对 E 列所有元素加 5（使用 lambda）
df.E = df.E.apply(lambda x: x + 5)

# 对 E 列元素判断能否被 3 整除
df.E = df.E.apply(lambda x: 'Yes' if x % 3 == 0 else 'No')
print(df)
```

### `applymap()`

元素级操作，对 DataFrame 中每个元素应用函数。

```python
df = pd.DataFrame([[1, 2.12, 3.245], [3.356, 4.56, 2.1101]],
                  columns=list('abc'), index=[2, 3])

def f(x):
    return len(str(x))   # 计算每个元素的字符串长度

print(df.applymap(f))
```

### `map()`

仅用于 Series，对每个元素应用函数。

```python
# 示例：将性别映射为 0/1
df['性别码'] = df['性别'].map({'女': 0, '男': 1})
```

### 三者区别总结

| 函数 | 作用对象 | 说明 |
|------|----------|------|
| `map()` | Series 元素 | 逐个元素处理 |
| `apply()` | Series 或 DataFrame 的行/列 | 可进行聚合或逐行/列操作 |
| `applymap()` | DataFrame 元素 | 逐个元素处理 |

---

## 3.2.7 排序

### `sort_index()`：按索引排序

```python
s = pd.Series([1, 2, 3], index=['a', 'c', 'b'])
print("升序:\n", s.sort_index())
print("降序:\n", s.sort_index(ascending=False))
```

### `sort_values()`：按值排序

```python
s = pd.Series([np.nan, 1, 7, 2, 3], index=['a', 'c', 'e', 'b', 'd'])
print("升序:\n", s.sort_values())      # NaN 排在最后
print("降序:\n", s.sort_values(ascending=False))
```

---

## 3.2.8 汇总与统计

### 常用统计方法

```python
df = pd.DataFrame([[np.nan, 1, 3], [4, 5, 6]], index=['S1', 'S2'], columns=['c', 'a', 'b'])

print("count:\n", df.count())          # 非 NaN 个数
print("describe:\n", df.describe())    # 汇总统计
print("max:\n", df.max())              # 最大值
print("sum:\n", df.sum())              # 求和
print("mean:\n", df.mean())            # 平均值
print("median:\n", df.median())        # 中位数
print("var:\n", df.var())              # 方差
print("std:\n", df.std())              # 标准差
print("diff:\n", df.diff())            # 一阶差分
```

### 协方差与相关系数

- **协方差**：反映两个变量同向或反向变化的程度。
- **相关系数**：标准化后的协方差，范围 [-1, 1]。

```python
df = pd.DataFrame({
    "年龄": [8, 9, 10, 11, 12],
    "身高": [130, 135, 140, 141, 150]
})

print("协方差:", df['年龄'].cov(df['身高']))
print("相关系数:", df['年龄'].corr(df['身高']))
```

---

## 3.2.9 数据分组与聚合

使用 `groupby()` 对数据进行分组，然后应用聚合函数。

```python
import numpy as np

dict_data = {
    'key1': ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'a'],
    'key2': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
    'data1': np.random.randn(8),
    'data2': np.random.randn(8)
}
df = pd.DataFrame(dict_data)

print("原始数据:\n", df)

# 按 key1 分组，计算均值
grouped1 = df.groupby('key1')
print("按 key1 分组均值:\n", grouped1.mean())

# 对 data1 列按 key1 分组
grouped2 = df['data1'].groupby(df['key1'])
print("data1 按 key1 分组均值:\n", grouped2.mean())

# 分组大小
print("分组大小:\n", grouped1.size())

# 多聚合
print("sum:\n", df.groupby('key1').sum())
print("max:\n", df.groupby('key1').max())
print("describe:\n", df.groupby('key1').describe())
```

---

## 3.2.10 Pandas 数据读取与存储

### 1. CSV 文件

```python
import os

# 设置工作目录
os.chdir('D:\\Data_mining')

# 写入 CSV（先创建数据）
head = ['学号', '姓名', '性别', '年龄', '系部']
data = [
    ['S1', '许文秀', '女', 20, '计算机系'],
    ['S2', '刘德峰', '男', 21, '电信系'],
    ['S3', '刘世元', '男', 22, '管理系'],
    ['S4', '于金凤', '女', 21, '计算机系']
]
df = pd.DataFrame(data, columns=head)
df.to_csv('test.csv', index=False, encoding='utf-8-sig')

# 读取 CSV
df_read = pd.read_csv('test.csv', encoding='utf-8-sig')
print(df_read)
```

### 2. Excel 文件

Pandas 依赖 `xlrd`（读取）和 `openpyxl`（写入）。注意：`xlrd` 1.2.0 之后不支持 `.xlsx`，推荐使用 `openpyxl`。

```python
# 写入 Excel
df.to_excel('stud.xlsx', index=False, engine='openpyxl')

# 读取 Excel
df_excel = pd.read_excel('stud.xlsx', engine='openpyxl')
print(df_excel)
```

### 3. MySQL 数据库

需要安装 `pymysql` 或 `sqlalchemy`。

```python
import pymysql

# 建立连接
con = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='test',
    port=3306,
    charset='utf8'
)

# 读取表数据
sql = 'SELECT * FROM a'
df_sql = pd.read_sql(sql, con)

con.close()
print(df_sql)
```

