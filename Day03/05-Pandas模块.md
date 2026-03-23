

# 3.2 Pandas 模块

Pandas 是基于 NumPy 的数据分析工具，提供了高效、灵活的数据结构 Series 和 DataFrame，广泛应用于数据清洗、转换、分析和可视化。

---

## 3.2.1 Pandas 中的数据结构

### 1. Series 对象

Series 是一维带标签的数组，可以存储任意数据类型。

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

### 2. DataFrame 对象

DataFrame 是一个二维表格型数据结构，包含行索引和列索引。

```python
import pandas as pd

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

```python
import pandas as pd

df = pd.DataFrame({
    '姓名': ['许文秀', '刘世元'],
    '性别': ['女', '男'],
    '年龄': [21, 20],
    '系部': ['计算机系', '电信系']
}, index=['S1', 'S2'])

print("values:\n", df.values)
print("index:", df.index)
print("columns:", df.columns)
print("shape:", df.shape)
```

---

## 3.2.3 DataFrame 常用方法

| 方法 | 说明 | 示例 | 结果 |
|------|------|------|------|
| `iloc[行序, 列序]` | 按整数位置索引 | `df.iloc[:, 0:2]` | 前两列数据 |
| `loc[行标签, 列标签]` | 按标签索引 | `df.loc['S2', '姓名']` | `'刘世元'` |
| `head(i)` | 显示前 i 行 | `df.head(1)` | 第一行数据 |
| `tail(i)` | 显示后 i 行 | `df.tail(1)` | 最后一行数据 |
| `describe()` | 数值列统计信息 | `df.describe()` | 年龄的 count, mean, std, min, max 等 |
| `del` | 删除指定列 | `del df['性别']` | 删除“性别”列 |
| `drop(columns=[...])` | 同时删除多列 | `df.drop(columns=['性别','系部'])` | 返回新 DataFrame |
| `rename(columns={})` | 修改列名 | `df.rename(columns={'姓名':'Name'})` | 列名更改 |
| `copy()` | 复制 DataFrame | `df1 = df.copy()` | 深拷贝 |

```python
import pandas as pd

df = pd.DataFrame({
    '姓名': ['许文秀', '刘世元'],
    '性别': ['女', '男'],
    '年龄': [21, 20],
    '系部': ['计算机系', '电信系']
}, index=['S1', 'S2'])

print("iloc 前两列:\n", df.iloc[:, 0:2])
print("loc 指定行列:", df.loc['S2', '姓名'])
print("head 前1行:\n", df.head(1))
print("describe:\n", df.describe())

# 删除列
df.drop(columns=['性别'], inplace=True)
print("删除性别列后:\n", df)
```

---

## 3.2.4 DataFrame 的数据查询与编辑

### 1. 数据查询

#### (1) 查询列数据

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

```python
print("查询前两行:\n", df[:2])
print("查询第2行:\n", df[1:2])
print("查询前3行:\n", df.head(3))
print("查询后两行:\n", df.tail(2))
```

#### (3) 同时查询行和列

```python
# loc：行标签，列标签
print("查询 S1 和 S3 的姓名和系部:\n", df.loc[['S1', 'S3'], ['姓名', '系部']])

# iloc：行序号，列序号
print("查询第1和第3行的第2列（性别）:\n", df.iloc[[1, 3], [1]])
```

#### (4) 条件查询

```python
# 查询姓名为刘德峰的行
print("姓名为刘德峰:\n", df[df['姓名'] == '刘德峰'])

# 查询计算机系的女同学
print("计算机系的女同学:\n", df[(df['性别'] == '女') & (df['系部'] == '计算机系')])
```

### 2. 数据编辑

#### (1) 添加数据

```python
import pandas as pd

data = {
    '姓名': ['许文秀', '刘世元', '刘德峰', '于金凤'],
    '性别': ['女', '男', '男', '女'],
    '年龄': [20, 21, 22, 20],
    '系部': ['计算机系', '电信系', '统计系', '计算机系']
}
df = pd.DataFrame(data)

# 添加一行（使用 pd.concat，因为 append 在较新版本已弃用）
new_row = pd.DataFrame([{'姓名': '王文庆', '性别': '男', '年龄': 21, '系部': '电信系'}])
df1 = pd.concat([df, new_row], ignore_index=True)

# 添加一列
df1['籍贯'] = ['河北省', '天津市', '河北省', '重庆市', '江苏省']
print("添加新的数据行和列:\n", df1)
```

#### (2) 删除数据

```python
import pandas as pd

data = {
    '姓名': ['许文秀', '刘世元', '刘德峰', '于金凤'],
    '性别': ['女', '男', '男', '女'],
    '年龄': [20, 21, 22, 20],
    '系部': ['计算机系', '电信系', '统计系', '计算机系']
}
df = pd.DataFrame(data)

# 删除第3行（索引为2）
df1 = df.drop([2], axis=0, inplace=False)
print("删除第3行:\n", df1)

# 删除“系部”列（在原对象上删除）
df.drop('系部', axis=1, inplace=True)
print("删除系部列后:\n", df)
```

#### (3) 修改数据

```python
import pandas as pd

datas = {
    '姓名': ['许文秀', '刘世元', '刘德峰', '于金凤'],
    '性别': ['女', '男', '男', '女'],
    '年龄': [20, 21, 22, 20],
    '系部': ['计算机系', '电信系', '统计系', '计算机系']
}
df = pd.DataFrame(datas)
print("原数据:\n", df)

# 修改行标题
df1 = df.rename({0: 'S1', 1: 'S2', 2: 'S3', 3: 'S4'})
print("修改行标题:\n", df1)

# 修改列标题
df1.rename(columns={'姓名': 'name', '性别': 'sex', '年龄': 'age', '系部': 'dept'}, inplace=True)
print("修改列标题:\n", df1)
```

---

## 3.2.5 Pandas 数据四则运算

两个 DataFrame 进行四则运算时，对应元素运算。对于不同维度，缺失位置用 `NaN` 填充；可通过 `fill_value` 指定填充值。

```python
import numpy as np
import pandas as pd

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

### `apply()` 函数

对 DataFrame 的行或列应用函数。

```python
import numpy as np
import pandas as pd

df = pd.DataFrame(np.arange(12).reshape(3, 4), columns=list('ABCD'))
print("df中原始数据为:\n", df)

# 对每个元素求平方根
print("计算每个元素的平方根:\n", df.apply(np.sqrt))

# 对每一列求平均值
print("计算每一列元素的平均值:\n", df.apply(np.mean))

# 对每一行求平均值
print("计算每一行元素的平均值:\n", df.apply(np.mean, axis=1))

# 增加第E列，为前面四列元素之和
def Add_a(x):
    return x.A + x.B + x.C + x.D
df['E'] = df.apply(Add_a, axis=1)

print("增加第E列:\n", df)

# 列E中所有元素加5
df.E = df.E.apply(lambda x: x + 5)
print("列E中所有元素加5:\n", df)

# 第E列元素被3整除的均赋值Yes，否则赋值No
df.E = df.E.apply(lambda x: 'Yes' if x % 3 == 0 else 'No')
print("第E列元素被3整除的均赋值Yes，否则赋值No:\n", df)
```

### `applymap()` 函数

元素级操作，对 DataFrame 中每个元素应用函数。

```python
import pandas as pd

df = pd.DataFrame([[1, 2.12, 3.245], [3.356, 4.56, 2.1101]],
                  columns=list('abc'), index=[2, 3])

def f(x):
    return len(str(x))   # 计算每个元素的字符串长度

print(df.applymap(f))
```

### `map()` 函数

仅用于 Series，对每个元素应用函数。

```python
import pandas as pd

df = pd.DataFrame({'性别': ['女', '男', '男', '女']})
df['性别码'] = df['性别'].map({'女': 0, '男': 1})
print(df)
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
import pandas as pd

s = pd.Series([1, 2, 3], index=['a', 'c', 'b'])
print("升序:\n", s.sort_index())
print("降序:\n", s.sort_index(ascending=False))
```

### `sort_values()`：按值排序

```python
import numpy as np
import pandas as pd

s = pd.Series([np.nan, 1, 7, 2, 3], index=['a', 'c', 'e', 'b', 'd'])
print("升序（NaN 排在最后）:\n", s.sort_values())
print("降序（NaN 排在最后）:\n", s.sort_values(ascending=False))
```

---

## 3.2.8 汇总与统计

### 常用统计方法

```python
import numpy as np
import pandas as pd

df = pd.DataFrame([[np.nan, 1, 3], [4, 5, 6]], index=['S1', 'S2'], columns=['c', 'a', 'b'])

print("count (非NaN个数):\n", df.count())
print("describe:\n", df.describe())
print("max:\n", df.max())
print("sum:\n", df.sum())
print("mean:\n", df.mean())
print("median:\n", df.median())
print("var:\n", df.var())
print("std:\n", df.std())
print("diff (一阶差分):\n", df.diff())
```

### 协方差与相关系数

```python
import pandas as pd

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
import pandas as pd

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
import pandas as pd

# 设置工作目录（请根据实际情况修改路径）
os.chdir('D:\\Data_mining')

# 写入 CSV
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

Pandas 依赖 `openpyxl` 或 `xlrd` 处理 Excel。注意：`xlrd` 1.2.0 之后不支持 `.xlsx`，推荐使用 `openpyxl`。

```python
import pandas as pd

# 写入 Excel（需要安装 openpyxl）
df.to_excel('stud.xlsx', index=False, engine='openpyxl')

# 读取 Excel
df_excel = pd.read_excel('stud.xlsx', engine='openpyxl')
print(df_excel)
```

### 3. MySQL 数据库

需要安装 `pymysql` 或 `sqlalchemy`。

```python
import pandas as pd
import pymysql

# 建立连接（请修改为实际数据库参数）
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

