

# 3.3 Matplotlib 图表绘制基础

Matplotlib 是 Python 中最常用的数据可视化库之一，它提供了一套类似 MATLAB 的绘图接口，能够绘制高质量的二维图表。通过 Matplotlib，用户可以轻松创建折线图、散点图、柱状图、饼图、直方图、箱线图等多种图形。

---

## 3.3.1 Matplotlib 简介

Matplotlib 主要由以下模块组成：

- **pyplot**：提供了一套与 MATLAB 类似的绘图 API，是 Matplotlib 最常用的接口。
- **pylab**：将 pyplot 与 NumPy 合并到一个命名空间中，方便交互式使用，但实际开发中推荐分别导入。

---

## 3.3.2 Matplotlib 绘图基础

使用 Matplotlib 绘图通常包含三个主要步骤：

1. **创建画布与子图**
2. **绘制图形并添加修饰**
3. **存储与展示图形**

### 1. 创建画布与子图

| 函数 | 功能 |
|------|------|
| `plt.figure()` | 创建一个空白画布，可指定画布大小、分辨率等 |
| `fig.add_subplot()` | 创建并选中子图，指定子图的行数、列数与编号 |
| `plt.subplots_adjust()` | 调整子图之间的间距（`wspace` 为宽度，`hspace` 为高度） |

**示例：创建多个子图**

```python
import numpy as np
import matplotlib.pyplot as plt

# 创建画布，大小为 8x4，分辨率为 80
p1 = plt.figure(figsize=(8, 4), dpi=80)

# 第一个子图：1行2列，第1个
ax1 = p1.add_subplot(1, 2, 1)
plt.title('Power Function')
x1 = np.arange(-2, 2, 0.01)
plt.plot(x1, x1**2)
plt.plot(x1, x1**4)
plt.legend(['y = x^2', 'y = x^4'])

# 第二个子图
ax2 = p1.add_subplot(1, 2, 2)
plt.title('e^x / log(x)')
x2 = np.arange(1, 4, 0.01)
plt.plot(x2, np.exp(x2))
plt.plot(x2, np.log(x2))
plt.legend(['y = e^x', 'y = log(x)'])

plt.show()
```

### 2. 绘图及修饰

| 函数 | 功能 |
|------|------|
| `plt.title()` | 添加图形标题 |
| `plt.xlabel()` / `plt.ylabel()` | 添加 x / y 轴标签 |
| `plt.xlim()` / `plt.ylim()` | 设置坐标轴范围 |
| `plt.xticks()` / `plt.yticks()` | 设置坐标轴刻度 |
| `plt.legend()` | 添加图例 |

### 3. 存储与展示图形

| 函数 | 功能 |
|------|------|
| `plt.savefig()` | 保存图形到文件 |
| `plt.show()` | 在屏幕上显示图形 |

**示例：绘制一周温度变化曲线**

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 8)                     # 周一至周日
y = np.array([15, 20, 22, 23, 20, 18, 16])

plt.plot(x, y)
plt.show()
```

---

## 3.3.3 Matplotlib 简单绘图

### 1. pyplot 模块

#### (1) `plot()` 函数：绘制折线图

```python
plt.plot(x, y, style, linewidth, label)
```

**常用样式字符**：

| 颜色字符 | 说明 | 风格字符 | 说明 | 标记字符 | 说明 |
|----------|------|----------|------|----------|------|
| `'b'` | 蓝色 | `'-'` | 实线 | `'o'` | 实心圈 |
| `'g'` | 绿色 | `'--'` | 破折线 | `'^'` | 上三角 |
| `'r'` | 红色 | `':'` | 虚线 | `'s'` | 正方形 |
| `'c'` | 青色 | `'-.'` | 点划线 | `'*'` | 星形 |
| `'m'` | 洋红 | | | `'+'` | 十字 |
| `'y'` | 黄色 | | | `'x'` | x 标记 |
| `'k'` | 黑色 | | | `'D'` | 菱形 |
| `'w'` | 白色 | | | `'d'` | 瘦菱形 |

**示例：不同线条风格**

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)
plt.plot(x, x*1.5, 'g+:',      # 绿色 + 虚线
         x, x*2.5, 'ro-.',     # 红色 o 点划线
         x, x*3.5, 'x--',      # 蓝色 x 破折线
         x, x*4.5, 'bd-')      # 蓝色 d 实线
plt.show()
```

**示例：双 Y 轴图形**

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.01, np.e, 0.01)
y1 = np.exp(-x)
y2 = np.log(x)

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(x, y1, 'r', label='exp(-x)')
ax1.legend(bbox_to_anchor=(1, 0.5))
ax1.set_ylabel('Y values for exp(-x)', color='r')
ax1.set_xlabel('X values')
ax1.set_title('Double Y axis')

ax2 = ax1.twinx()
ax2.plot(x, y2, 'g', label='log(x)')
ax2.legend(bbox_to_anchor=(1, 0.6))
ax2.set_ylabel('Y values for log(x)', color='g')

plt.show()
```

**示例：绘制直线**

```python
import matplotlib.pyplot as plt

x = [1, 2]
y = [3, 6]
plt.plot(x, y)
plt.show()
```

**示例：绘制折线图**

```python
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5, 6]
y = [0.3, 0.4, 2, 5, 3, 4.5, 4]
plt.figure(figsize=(8, 4))
plt.plot(x, y, 'b-', linewidth=1)
plt.show()
```

**示例：正弦与余弦曲线**

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 1000)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, ls="-", lw=2, label="sin(x)")
plt.plot(x, y2, ls="-", lw=2, label="cos(x)")
plt.legend()
plt.show()
```

#### (2) `scatter()` 函数：绘制散点图

```python
plt.scatter(x, y, s=20, c='b', marker='o')
```

- `s`：点的大小
- `c`：点的颜色
- `marker`：点的形状

**示例：绘制散点图**

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(100)
y = np.random.randn(100)
plt.scatter(x, y, s=30, c='r', marker='o')
plt.show()
```

#### (3) `bar()` 函数：绘制条形图

```python
plt.bar(x, height, width=0.8, color='b', label='')
```

**示例：销售数据对比条形图**

```python
import numpy as np
import matplotlib.pyplot as plt

x_data = ['2017', '2018', '2019', '2020', '2021', '2022', '2023']
y_data1 = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]

bar_width = 0.3
plt.rcParams['font.family'] = 'STSong'   # 显示中文
plt.rcParams['font.size'] = 12

plt.bar(x=np.arange(len(x_data)), height=y_data1, width=bar_width, label='数据库技术')
plt.bar(x=np.arange(len(x_data)) + bar_width, height=y_data2, width=bar_width, label='数据挖掘')

# 添加数值标签
for x, y in enumerate(y_data1):
    plt.text(x, y + 100, f'{y}', ha='center', va='bottom')
for x, y in enumerate(y_data2):
    plt.text(x + bar_width, y + 100, f'{y}', ha='center', va='top')

plt.title('数据库技术与数据挖掘销售对比')
plt.xlabel('年份')
plt.ylabel('销量')
plt.legend()
plt.show()
```

#### (4) `pie()` 函数：绘制饼图

```python
plt.pie(x, labels=None, explode=None, autopct='%3.1f%%', shadow=False)
```

**示例：绘制饼图**

```python
import matplotlib.pyplot as plt

fracs = [15, 30.6, 44.4, 10]
explode = [0, 0.1, 0, 0]
labels = ['A', 'B', 'C', 'D']

plt.pie(x=fracs, autopct='%3.1f%%', explode=explode, labels=labels, shadow=True)
plt.show()
```

#### (5) `hist()` 函数：绘制直方图

```python
plt.hist(x, bins=10, range=None, color='b')
```

**示例：绘制正态分布直方图**

```python
import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(0, 1, 10000)
plt.hist(data, bins=50)
plt.show()
```

#### (6) `boxplot()` 函数：绘制箱线图

```python
plt.boxplot(x, notch=False, sym='+', vert=True, whis=1.5)
```

**示例：绘制箱线图**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dt = pd.DataFrame(np.random.rand(4, 4))
plt.boxplot(x=dt.values, labels=dt.columns, widths=0.5)
plt.show()
```

### 2. pylab 模块

pylab 将 pyplot 与 NumPy 合并，适合交互式环境，但实际开发中推荐分别导入。

**示例：使用 pylab 绘图**

```python
import pylab as pl

x = range(10)
y = [i * i for i in x]

pl.rcParams['font.family'] = 'STSong'
pl.rcParams['font.size'] = 12

pl.plot(x, y, 'ob-', label='y = x² 曲线图')
pl.xlabel('x 轴')
pl.ylabel('y 轴')
pl.legend()
pl.show()
```

---

## 3.3.4 文本注解

### 1. `text()` 函数：无指向型注释

```python
plt.text(x, y, string, weight='bold', color='b')
```

**示例：添加文本注释**

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 11, 1)
y = x ** 2
plt.plot(x, y)
plt.text(-3, 20, 'Function: y = x²', size=12)
plt.show()
```

### 2. `annotate()` 函数：指向型注释

```python
plt.annotate(text, xy=(x, y), xytext=(x_text, y_text),
             xycoords='data', textcoords='offset points',
             arrowprops=dict(arrowstyle='->'))
```

**常用坐标系属性**：

| 属性值 | 说明 |
|--------|------|
| `'figure points'` | 以绘图区左下角为参考，单位：点数 |
| `'figure pixels'` | 以绘图区左下角为参考，单位：像素 |
| `'figure fraction'` | 以绘图区左下角为参考，单位：百分比 |
| `'axes points'` | 以子图左下角为参考，单位：点数 |
| `'axes pixels'` | 以子图左下角为参考，单位：像素 |
| `'axes fraction'` | 以子图左下角为参考，单位：百分比 |
| `'data'` | 以被注释点的数据坐标（默认） |

**示例：带箭头的注释**

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.005)
y = np.exp(-x / 2.0) * np.sin(2 * np.pi * x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)

# 注释点
xdata, ydata = 5, 0
bbox1 = dict(boxstyle='round', fc='0.8')
arrow1 = dict(arrowstyle='->')
arrow2 = dict(arrowstyle='->', connectionstyle='angle,angleA=0,angleB=90,rad=10')

ax.annotate('local max', xy=(3, 0.5), xytext=(5, 0.8),
            arrowprops=arrow1, bbox=bbox1)

plt.show()
```

---

**说明**：以上示例均基于 Matplotlib 常用函数编写，可根据实际需求调整参数（如图形大小、颜色、样式等）。在绘图前建议设置中文字体支持，避免中文显示乱码：

```python
plt.rcParams['font.sans-serif'] = ['SimHei']      # 黑体
plt.rcParams['axes.unicode_minus'] = False        # 正常显示负号
```
