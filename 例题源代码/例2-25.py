import re
str1='<h1>hello 你好，world世界</h1>'
chinese_pattern='[\u4e00-\u9fa5]+' #汉字编码范围
chinese_str=re.findall(chinese_pattern,str1)
for ch in chinese_str:
    print(ch,end=' ')
