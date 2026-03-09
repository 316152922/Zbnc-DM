# 第2章 Python数据分析基础（2.3正则表达式与2.4文件操作）

## 课程信息

- **课程名称**：数据挖掘导论
- **本章主题**：Python数据分析基础
- **课时安排**：2学时（讲授）+ 1学时实验（可选）
- **教学对象**：已学习Python基础语法（数据类型、流程控制、函数及内置数据结构）的学生
- **教学方式**：讲授 + 代码演示 + 上机实践

---

## 一、教学目标

### 知识目标
- 掌握正则表达式的基本语法和常用字符含义
- 理解re模块中match、search、sub、findall等方法的作用与区别
- 能够使用正则表达式进行字符串匹配、提取、替换
- 掌握文件操作的基本流程（打开、读写、关闭）
- 理解不同文件打开模式（r、w、a、+、b）的适用场景
- 掌握read、readline、readlines、write、writelines等方法的使用
- 了解文件指针的移动（seek方法）

### 能力目标
- 能够编写正则表达式从文本中提取特定信息（如电话号码、邮箱、日期等）
- 能够读写文本文件并进行简单的数据处理
- 能够综合运用正则表达式和文件操作完成数据清洗任务

### 素质目标
- 培养处理文本数据的敏感性和效率意识
- 理解数据清洗在数据挖掘流程中的重要性
- 增强解决实际问题的能力

---

## 二、教学重点与难点

### 教学重点
- 正则表达式中常用元字符的含义及组合使用
- re模块中match、search、findall、sub方法的区别与应用
- 文件读写的基本操作
- 不同文件打开模式的特点

### 教学难点
- 正则表达式中贪婪匹配与非贪婪匹配的理解
- 分组提取（group方法）的使用
- 文件指针的移动（seek方法）及字节偏移的计算
- 编码问题（尤其是中文字符的处理）

---

## 三、教学内容与过程

### 第一课时：正则表达式（2.3）

#### 1. 导入（5分钟）

**情景引入**：在数据挖掘项目中，我们经常需要从大量文本中提取特定模式的信息，例如：
- 从客户信息中提取电话号码、邮箱地址
- 从日志文件中提取日期时间
- 清洗网页抓取的数据

如果使用传统的字符串方法（如`find`、`split`）会非常繁琐且容易出错。Python提供了强大的正则表达式模块`re`，可以高效地完成这些任务。

#### 2. 正则表达式基础语法（15分钟）

**常用元字符**（结合课件表格讲解）：

| 模式 | 说明 | 示例 |
|------|------|------|
| `\d` | 匹配一个数字 | `\d{3}` 匹配三位数字（如'123'） |
| `\D` | 匹配非数字 | |
| `\w` | 匹配字母、数字、下划线 | `\w+` 匹配一个单词 |
| `\W` | 匹配非字母数字下划线 | |
| `.` | 匹配除换行符外的任意字符 | |
| `\s` | 匹配空白字符（空格、制表符、换行等） | |
| `*` | 匹配前一个字符0次或多次 | `ab*c` 可匹配'ac'、'abc'、'abbc'等 |
| `+` | 匹配前一个字符1次或多次 | `ab+c` 可匹配'abc'、'abbc'，不匹配'ac' |
| `?` | 匹配前一个字符0次或1次 | `ab?c` 可匹配'ac'、'abc' |
| `{n,m}` | 匹配前一个字符n~m次 | `\d{2,4}` 匹配2~4位数字 |
| `^` | 匹配行首 | `^Hello` 匹配以Hello开头的行 |
| `$` | 匹配行尾 | `world$` 匹配以world结尾的行 |
| `|` | 匹配左右任意一个 | `(P|p)ython` 匹配'Python'或'python' |
| `[]` | 字符集 | `[0-9a-zA-Z_]` 匹配一个数字、字母或下划线 |

**重点讲解**：
- `\d{3}\s+\d{2,8}` 示例：匹配3个数字，至少一个空格，2~8个数字（如区号+电话号码）
- 字符集`[]`的使用：`[a-zA-Z_][0-9a-zA-Z_]*` 匹配变量名

#### 3. re模块常用方法（20分钟）

**match()方法**：从字符串起始位置匹配
```python
import re
str1 = 'hello 123456789 word this is just a test'
pattern = r'^Hello\s\d{9}.*test$'  # 注意忽略大小写
result = re.match(pattern, str1, re.I)
if result:
    print(result.group())   # 输出匹配的整个字符串
    print(result.span())    # 输出匹配的范围 (0, 34)
```
强调：match只检查开头，开头不匹配则返回None。

**search()方法**：扫描整个字符串，返回第一个匹配
```python
line = 'In fact, cats are smarter than dogs'
result = re.search(r'(.*) are (.*?) .*', line, re.M|re.I)
if result:
    print('整个匹配:', result.group())
    print('第一个分组:', result.group(1))  # 'cats'
    print('第二个分组:', result.group(2))  # 'smarter'
```
说明：`group(0)`或`group()`返回整个匹配，`group(1)`返回第一个括号内的内容。

**match vs search**：通过例2.22对比展示。

**sub()方法**：替换
```python
phone = '0517-3214-7231 # 这是一个公司的电话号码'
num = re.sub(r'#.*$', '', phone)  # 删除注释
print(num)  # 0517-3214-7231
num = re.sub(r'\D', '', phone)    # 移除非数字
print(num)  # 051732147231
```

**findall()方法**：返回所有匹配的列表
```python
str1 = 'se234 2022-10-09 07:30:00 2022-10-10 07:25:00最新疫情'
pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
content = re.findall(pattern, str1)
print(content)  # ['2022-10-09 07:30:00', '2022-10-10 07:25:00']
```

#### 4. 综合案例：提取网页信息（15分钟）

**提取汉字**（利用Unicode范围）：
```python
str1 = '<h1>hello 你好, world世界</h1>'
chinese_pattern = '[\u4e00-\u9fa5]+'
chinese_str = re.findall(chinese_pattern, str1)
print(''.join(chinese_str))  # 你好世界
```

**提取URL**：
```python
def Find(string):
    url_pattern = r'[a-zA-Z]+://[^\s]*'  # 匹配 http:// 或 https:// 开头，不含空白
    return re.findall(url_pattern, string)

str_url = '我们常用网站很多，如Runoob：https://www.runoob.com, Google：https://www.google.com'
urls = Find(str_url)
for url in urls:
    print(url)
```

**抓取网页提取信息**（演示，需网络）：
```python
from urllib.request import urlopen
import re
text = urlopen('https://www.cnblogs.com').read().decode()
# 提取所有汉字
chinese = re.findall(r'[\u4e00-\u9fa5]+', text)
print(chinese[:10])  # 打印前10个
```

#### 5. 课堂练习（5分钟）
1. 编写正则表达式匹配邮箱地址（简单版：`\w+@\w+\.\w+`）
2. 从字符串中提取所有数字（包括整数和小数，如`3.14`）

---

### 第二课时：文件操作（2.4）

#### 1. 导入（5分钟）

**情景引入**：数据挖掘的第一步是获取数据，数据通常以文件形式存储（如CSV、TXT、日志文件等）。Python提供了内置的文件操作函数，可以方便地读写文件，为后续的数据处理打下基础。

#### 2. 文件的打开与关闭（10分钟）

**open()函数**：
```python
file = open('filename.txt', 'r', encoding='utf-8')
```
- **模式参数**（结合课件表格）：
  - `'r'`：只读（默认），文件必须存在
  - `'w'`：只写，不存在则创建，存在则清空
  - `'a'`：追加，不存在则创建
  - `'x'`：新建写入，文件存在则报错
  - `'b'`：二进制模式（如`'rb'`、`'wb'`）
  - `'+'`：读写（如`'r+'`、`'w+'`）

**关闭文件**：
```python
file.close()
```
**推荐使用`with`语句**（自动关闭）：
```python
with open('filename.txt', 'r', encoding='utf-8') as f:
    data = f.read()
```

#### 3. 读文件操作（15分钟）

**三种读方法**：
- `read(size)`：读取指定字节数，不指定则读取整个文件
- `readline()`：读取一行（包括换行符）
- `readlines()`：读取所有行，返回列表（每行包括换行符）

**示例**（读取诗歌文件）：
```python
file_path = 'D:\\Data_Mining\\poetry.txt'
with open(file_path, 'r', encoding='utf-8') as f:
    first_line = f.readline()          # 读取第一行
    print('第一行:', first_line)
    rest = f.read()                     # 读取剩余所有内容
    print('剩余内容:', rest)
```
注意：`read()`后文件指针移到末尾，再次读取为空。

**逐行读取推荐方式**：
```python
with open(file_path, 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())  # 去除末尾换行符
```

#### 4. 写文件操作（10分钟）

**写方法**：
- `write(str)`：写入字符串
- `writelines(list)`：写入字符串列表（不会自动添加换行符）

**示例**：
```python
lines = ['第一行\n', '第二行\n', '第三行\n']
with open('output.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)
```
注意：`'w'`模式会覆盖原文件；若想追加，使用`'a'`模式。

#### 5. 文件指针移动（10分钟）

**seek(offset, whence)**：
- `whence=0`：从文件开头偏移（默认）
- `whence=1`：从当前位置偏移
- `whence=2`：从文件末尾偏移

**示例**（重新读取第一行）：
```python
with open('poetry.txt', 'r+', encoding='utf-8') as f:
    line = f.readline()
    print('第一行:', line)
    f.seek(0, 0)          # 移动到文件开头
    line2 = f.readline()
    print('再次读取第一行:', line2)
```

#### 6. 综合练习（10分钟）

编写程序：统计文本文件中单词出现的频率，并将结果写入另一个文件。

**参考代码**：
```python
def word_count(input_file, output_file):
    word_dict = {}
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            words = line.split()
            for word in words:
                # 去除标点符号并转为小写
                word = word.strip('.,!?"\'').lower()
                if word:
                    word_dict[word] = word_dict.get(word, 0) + 1
    with open(output_file, 'w', encoding='utf-8') as f:
        for word, count in word_dict.items():
            f.write(f'{word}: {count}\n')
```

#### 7. 课堂小结（5分钟）
- 文件操作流程：打开→操作→关闭
- 牢记不同模式的含义
- 推荐使用`with`语句确保资源释放
- 文件指针移动可用于随机读写

---

## 四、实验课安排（1学时）

### 实验目的
- 掌握正则表达式进行文本匹配与提取
- 掌握文件读写操作
- 综合运用两者解决实际问题

### 实验题目

1. **正则表达式练习**：
   - 从给定的字符串中提取所有手机号码（11位数字，以1开头）。
   - 提取所有日期（格式：YYYY-MM-DD 或 YYYY/MM/DD）。

2. **文件读写练习**：
   - 创建一个文本文件，写入若干行学生信息（姓名,年龄,成绩）。
   - 读取该文件，计算平均成绩，并将成绩大于80分的学生信息写入另一个文件。

3. **综合应用**：
   - 给定一个日志文件（log.txt），每行包含时间戳、级别和消息，例如：
     `2023-05-10 08:23:45 INFO User login`
   - 使用正则表达式提取所有ERROR级别的行，并写入error.log文件。

### 实验要求
- 代码规范，有适当注释
- 提交.py文件和运行结果截图
- 简要说明遇到的问题及解决方法

---

## 五、课后作业

### 理论作业
1. 简述`match()`和`search()`的区别。
2. 写出正则表达式匹配以下模式：
   - 身份证号码（18位，最后一位可能是数字或X）
   - IP地址（如192.168.1.1）
3. 文件操作中，`'w'`和`'a'`模式有什么区别？
4. 解释`seek(0, 2)`的作用。

### 编程作业
1. 编写程序，读取一个文本文件，统计其中字母（a-z，忽略大小写）出现的次数，并将结果按字母顺序写入另一个文件。
2. 使用正则表达式，从HTML文件中提取所有超链接（`<a href="...">`中的URL）。
3. 模拟一个简单的日志分析器：读取日志文件，统计每个级别的出现次数（INFO、WARNING、ERROR），并输出到屏幕。

---

